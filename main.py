from antlr4 import *
from ArdenLexer import ArdenLexer
from ArdenParser import ArdenParser
from ArdenVisitor import ArdenVisitor
import sys


class ArdenExecutor(ArdenVisitor):
    """Visitor-based executor for the simplified Arden DSL in this repo.

    Semantics implemented:
    - `data:` block lists variable names that the executor may use (prepopulated defaults used when present).
    - `logic:` block contains one or more boolean expressions (comma separated). If ANY expression evaluates to True, the actions are executed.
    - `action:` block lists action identifiers (IDs). Executor maps those IDs to Python functions that print a human-friendly effect.
    """

    def __init__(self, variables=None):
        # default domain values (can be extended by the user)
        self.variables = {'glucose': 250, 'age': 45}
        if variables:
            self.variables.update(variables)
        # map action names (IDs) to functions
        self.actions = {
            'alert': lambda: print(f"ACTION: ALERT — glucose={self.variables.get('glucose')}") ,
            'notify_guardian': lambda: print("ACTION: Notify guardian (simulated)"),
            'recommend_test': lambda: print("ACTION: Recommend further testing"),
            'log_metrics': self._action_log_metrics
        }
        # simple metrics for demonstration of an extra semantic action
        self.metrics = { 'arithmetic_ops': 0 }

    def execute(self, moduleCtx):
        # Process data block
        self._process_data(moduleCtx.dataBlock())
        # Evaluate logic
        logic_result = self._process_logic(moduleCtx.logicBlock())
        # Run actions if logic true
        if logic_result:
            self._process_actions(moduleCtx.actionBlock())
        else:
            print("No action executed: logic conditions evaluated to False")
        # Extra semantic action result: print a tiny summary
        print(f"Execution summary: arithmetic_ops={self.metrics['arithmetic_ops']}")

    def _process_data(self, ctx):
        # dataBlock: 'data:' statementList ';'
        # Register IDs listed in data block as known variables (default 0 if not present)
        registered = []
        for s in ctx.statementList().statement():
            e = s.expr()
            if hasattr(e, 'ID') and e.ID() is not None:
                name = e.ID().getText()
                if name not in self.variables:
                    self.variables[name] = 0
                registered.append(name)
        if registered:
            print(f"DataBlock: registered variables {registered} | current values: { {k:self.variables[k] for k in registered} }")
        return True

    def _process_logic(self, ctx):
        # Returns True if any statement in the logic block evaluates truthy
        bools = []
        for s in ctx.statementList().statement():
            val_tuple = self._eval_expr(s.expr())
            val = val_tuple[0] if isinstance(val_tuple, tuple) else val_tuple
            bools.append(bool(val))
        any_true = any(bools)
        print(f"Logic evaluation results: {bools} -> {any_true}")
        return any_true

    def _process_actions(self, ctx):
        # Execute each action ID listed in the statementList
        for s in ctx.statementList().statement():
            e = s.expr()
            if hasattr(e, 'ID') and e.ID() is not None:
                name = e.ID().getText()
                fn = self.actions.get(name)
                if fn:
                    print(f"ActionBlock: executing action '{name}'")
                    fn()
                else:
                    print(f"Unknown action '{name}' (no-op)")
        return True

    def visitStatementList(self, ctx):
        # Generic evaluation (used only for debugging if called directly)
        out = []
        for s in ctx.statement():
            out.append(self.visit(s))
        return out

    def visitStatement(self, ctx):
        # statement: expr;
        val = self.visit(ctx.expr())
        # We tag IDs specially: if the ctx has ID terminal, return (name,'ID') else (value,'VAL')
        # But expr visitor will return either (name,'ID') for standalone IDs or numeric/bool values
        return val

    def _eval_expr(self, ctx):
        # Handle terminals via generic child inspection
        if ctx.getChildCount() == 1:
            child = ctx.getChild(0)
            text = child.getText()
            # Try INT first
            if text.isdigit():
                return (int(text), 'VAL')
            # Otherwise treat as identifier
            name = text
            value = self.variables.get(name, 0)
            print(f"Expr: ID '{name}' -> {value}")
            return (value, 'VAL')

        # unary not
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '!':
            inner = self._eval_expr(ctx.expr(0))
            v = inner[0] if isinstance(inner, tuple) else inner
            res = (not bool(v), 'VAL')
            print(f"Rule Not: !{v} -> {res[0]}")
            return res

        # parenthesis
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            inner = self._eval_expr(ctx.expr(0))
            val = inner[0] if isinstance(inner, tuple) else inner
            print(f"Rule Parens: ({val}) -> {val}")
            return inner

        # binary operators
        if ctx.op is not None:
            left = self._eval_expr(ctx.expr(0))
            right = self._eval_expr(ctx.expr(1))
            lval = left[0] if isinstance(left, tuple) else left
            rval = right[0] if isinstance(right, tuple) else right
            op = ctx.op.text
            try:
                # safe eval for the limited set of operators in grammar
                if op == '&&':
                    res = (bool(lval) and bool(rval), 'VAL')
                    print(f"Rule And: {lval} && {rval} -> {res[0]}")
                    return res
                if op == '||':
                    res = (bool(lval) or bool(rval), 'VAL')
                    print(f"Rule Or: {lval} || {rval} -> {res[0]}")
                    return res
                if op in ('>', '<', '>=', '<=', '==', '!='):
                    res_val = eval(f"{lval} {op} {rval}")
                    print(f"Rule {'Equality' if op in ('==','!=') else 'Comparison'}: {lval} {op} {rval} -> {res_val}")
                    return (res_val, 'VAL')
                if op in ('+', '-', '*', '/', '%'):
                    res_val = eval(f"{lval} {op} {rval}")
                    print(f"Rule {'AddSub' if op in ('+','-') else 'MulDiv'}: {lval} {op} {rval} -> {res_val}")
                    # extra semantic action: count arithmetic operations
                    self.metrics['arithmetic_ops'] = self.metrics.get('arithmetic_ops', 0) + 1
                    return (res_val, 'VAL')
            except Exception as e:
                print(f"Error evaluating {lval} {op} {rval}: {e}")
                return (0, 'VAL')

        # fallback
        return (0, 'VAL')

    def _action_log_metrics(self):
        print(f"ACTION: Metrics snapshot -> {self.variables}")


def run_file(path):
    # Show input text content (requirement a)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        print("\n=== Input Text ===")
        print(content.rstrip('\n'))
        print("=== End Input ===\n")
    except Exception as e:
        print(f"Could not read input file '{path}': {e}")

    input_stream = FileStream(path)
    lexer = ArdenLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ArdenParser(stream)
    tree = parser.module()
    # Debug: show parse tree string
    try:
        print(tree.toStringTree(recog=parser))
    except Exception:
        pass
    executor = ArdenExecutor()
    executor.execute(tree)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = 'exemplo1.mlm'
    print(f"Running Arden executor on: {path}")
    run_file(path)