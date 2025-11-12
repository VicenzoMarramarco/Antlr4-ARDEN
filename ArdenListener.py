# Generated from Arden.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ArdenParser import ArdenParser
else:
    from ArdenParser import ArdenParser

# This class defines a complete listener for a parse tree produced by ArdenParser.
class ArdenListener(ParseTreeListener):

    # Enter a parse tree produced by ArdenParser#module.
    def enterModule(self, ctx:ArdenParser.ModuleContext):
        pass

    # Exit a parse tree produced by ArdenParser#module.
    def exitModule(self, ctx:ArdenParser.ModuleContext):
        pass


    # Enter a parse tree produced by ArdenParser#dataBlock.
    def enterDataBlock(self, ctx:ArdenParser.DataBlockContext):
        pass

    # Exit a parse tree produced by ArdenParser#dataBlock.
    def exitDataBlock(self, ctx:ArdenParser.DataBlockContext):
        pass


    # Enter a parse tree produced by ArdenParser#logicBlock.
    def enterLogicBlock(self, ctx:ArdenParser.LogicBlockContext):
        pass

    # Exit a parse tree produced by ArdenParser#logicBlock.
    def exitLogicBlock(self, ctx:ArdenParser.LogicBlockContext):
        pass


    # Enter a parse tree produced by ArdenParser#actionBlock.
    def enterActionBlock(self, ctx:ArdenParser.ActionBlockContext):
        pass

    # Exit a parse tree produced by ArdenParser#actionBlock.
    def exitActionBlock(self, ctx:ArdenParser.ActionBlockContext):
        pass


    # Enter a parse tree produced by ArdenParser#statementList.
    def enterStatementList(self, ctx:ArdenParser.StatementListContext):
        pass

    # Exit a parse tree produced by ArdenParser#statementList.
    def exitStatementList(self, ctx:ArdenParser.StatementListContext):
        pass


    # Enter a parse tree produced by ArdenParser#statement.
    def enterStatement(self, ctx:ArdenParser.StatementContext):
        pass

    # Exit a parse tree produced by ArdenParser#statement.
    def exitStatement(self, ctx:ArdenParser.StatementContext):
        pass


    # Enter a parse tree produced by ArdenParser#Integer.
    def enterInteger(self, ctx:ArdenParser.IntegerContext):
        pass

    # Exit a parse tree produced by ArdenParser#Integer.
    def exitInteger(self, ctx:ArdenParser.IntegerContext):
        pass


    # Enter a parse tree produced by ArdenParser#Not.
    def enterNot(self, ctx:ArdenParser.NotContext):
        pass

    # Exit a parse tree produced by ArdenParser#Not.
    def exitNot(self, ctx:ArdenParser.NotContext):
        pass


    # Enter a parse tree produced by ArdenParser#Identifier.
    def enterIdentifier(self, ctx:ArdenParser.IdentifierContext):
        pass

    # Exit a parse tree produced by ArdenParser#Identifier.
    def exitIdentifier(self, ctx:ArdenParser.IdentifierContext):
        pass


    # Enter a parse tree produced by ArdenParser#Or.
    def enterOr(self, ctx:ArdenParser.OrContext):
        pass

    # Exit a parse tree produced by ArdenParser#Or.
    def exitOr(self, ctx:ArdenParser.OrContext):
        pass


    # Enter a parse tree produced by ArdenParser#MulDiv.
    def enterMulDiv(self, ctx:ArdenParser.MulDivContext):
        pass

    # Exit a parse tree produced by ArdenParser#MulDiv.
    def exitMulDiv(self, ctx:ArdenParser.MulDivContext):
        pass


    # Enter a parse tree produced by ArdenParser#AddSub.
    def enterAddSub(self, ctx:ArdenParser.AddSubContext):
        pass

    # Exit a parse tree produced by ArdenParser#AddSub.
    def exitAddSub(self, ctx:ArdenParser.AddSubContext):
        pass


    # Enter a parse tree produced by ArdenParser#Comparison.
    def enterComparison(self, ctx:ArdenParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ArdenParser#Comparison.
    def exitComparison(self, ctx:ArdenParser.ComparisonContext):
        pass


    # Enter a parse tree produced by ArdenParser#Parens.
    def enterParens(self, ctx:ArdenParser.ParensContext):
        pass

    # Exit a parse tree produced by ArdenParser#Parens.
    def exitParens(self, ctx:ArdenParser.ParensContext):
        pass


    # Enter a parse tree produced by ArdenParser#And.
    def enterAnd(self, ctx:ArdenParser.AndContext):
        pass

    # Exit a parse tree produced by ArdenParser#And.
    def exitAnd(self, ctx:ArdenParser.AndContext):
        pass


    # Enter a parse tree produced by ArdenParser#Equality.
    def enterEquality(self, ctx:ArdenParser.EqualityContext):
        pass

    # Exit a parse tree produced by ArdenParser#Equality.
    def exitEquality(self, ctx:ArdenParser.EqualityContext):
        pass



del ArdenParser