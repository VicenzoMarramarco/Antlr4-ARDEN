from antlr4 import ParseTreeVisitor


class ArdenVisitor(ParseTreeVisitor):
    # Generated-style visitor skeleton matching Arden.g4 rules
    def visitModule(self, ctx):
        return self.visitChildren(ctx)

    def visitDataBlock(self, ctx):
        return self.visitChildren(ctx)

    def visitLogicBlock(self, ctx):
        return self.visitChildren(ctx)

    def visitActionBlock(self, ctx):
        return self.visitChildren(ctx)

    def visitStatementList(self, ctx):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    def visitExpr(self, ctx):
        return self.visitChildren(ctx)
