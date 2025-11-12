grammar Arden_augmented;

// This is an "augmented" version of the grammar showing where semantic actions
// (in target language Python) might be inserted if using translation-directed-by-syntax.

// High-level structure remains identical to the clean grammar used to generate the parser.
// The actual semantic execution is implemented in the Python visitor `ArdenExecutor` (main.py).
module: dataBlock logicBlock actionBlock EOF;

dataBlock: 'data:' statementList ';'  // action: register variables
// Visitor action (Python): for each ID in the data block, register variable with default value if missing.
// See main.py -> ArdenExecutor._process_data
;

logicBlock: 'logic:' statementList ';'  // action: evaluate conditions
// Visitor action (Python): evaluate each expression to boolean, TRUE if any is true.
// See main.py -> ArdenExecutor._process_logic and _eval_expr for detailed rule logs.
;

actionBlock: 'action:' statementList ';' // action: perform mapped actions
// Visitor action (Python): map each ID to a Python function and execute.
// See main.py -> ArdenExecutor._process_actions
;

statementList: statement (',' statement)*;
statement: expr; // could carry action or expression

expr: expr op=('*' | '/' | '%') expr        # MulDiv
    | expr op=('+' | '-') expr              # AddSub
    | expr op=('>' | '<' | '>=' | '<=') expr # Comparison
    | expr op=('==' | '!=') expr            # Equality
    | expr op='&&' expr                     # And
    | expr op='||' expr                     # Or
    | '!' expr                              # Not
    | '(' expr ')'                          # Parens
    | ID                                    # Identifier
    | INT                                   # Integer
    ;

// Example of added semantic action: logging every operation
// Implemented in visitor (Python): main.py -> ArdenExecutor._eval_expr prints:
// - Rule And/Or/Not, Rule AddSub/MulDiv, Rule Comparison/Equality, Rule Parens, and ID resolution.
// Example embedded action (illustrative only, commented to keep grammar buildable):
//    | expr op=('+' | '-') expr              # AddSub
//      { print("[SEMANTIC ACTION] Add/Sub fired") }
// If targeting Python, adapt content accordingly; keep commented unless generating with that target.

ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
