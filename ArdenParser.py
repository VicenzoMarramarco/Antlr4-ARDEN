# Generated from Arden.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
try:
    from typing import TextIO
except Exception:
    import typing as _typing
    TextIO = _typing.IO

def serializedATN():
    return [
        4,1,24,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,5,4,35,8,4,10,4,12,4,38,9,4,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,51,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,71,8,6,10,6,12,6,
        74,9,6,1,6,0,1,12,7,0,2,4,6,8,10,12,0,4,1,0,6,8,1,0,9,10,1,0,11,
        14,1,0,15,16,78,0,14,1,0,0,0,2,19,1,0,0,0,4,23,1,0,0,0,6,27,1,0,
        0,0,8,31,1,0,0,0,10,39,1,0,0,0,12,50,1,0,0,0,14,15,3,2,1,0,15,16,
        3,4,2,0,16,17,3,6,3,0,17,18,5,0,0,1,18,1,1,0,0,0,19,20,5,1,0,0,20,
        21,3,8,4,0,21,22,5,2,0,0,22,3,1,0,0,0,23,24,5,3,0,0,24,25,3,8,4,
        0,25,26,5,2,0,0,26,5,1,0,0,0,27,28,5,4,0,0,28,29,3,8,4,0,29,30,5,
        2,0,0,30,7,1,0,0,0,31,36,3,10,5,0,32,33,5,5,0,0,33,35,3,10,5,0,34,
        32,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,9,1,0,0,
        0,38,36,1,0,0,0,39,40,3,12,6,0,40,11,1,0,0,0,41,42,6,6,-1,0,42,43,
        5,19,0,0,43,51,3,12,6,4,44,45,5,20,0,0,45,46,3,12,6,0,46,47,5,21,
        0,0,47,51,1,0,0,0,48,51,5,22,0,0,49,51,5,23,0,0,50,41,1,0,0,0,50,
        44,1,0,0,0,50,48,1,0,0,0,50,49,1,0,0,0,51,72,1,0,0,0,52,53,10,10,
        0,0,53,54,7,0,0,0,54,71,3,12,6,11,55,56,10,9,0,0,56,57,7,1,0,0,57,
        71,3,12,6,10,58,59,10,8,0,0,59,60,7,2,0,0,60,71,3,12,6,9,61,62,10,
        7,0,0,62,63,7,3,0,0,63,71,3,12,6,8,64,65,10,6,0,0,65,66,5,17,0,0,
        66,71,3,12,6,7,67,68,10,5,0,0,68,69,5,18,0,0,69,71,3,12,6,6,70,52,
        1,0,0,0,70,55,1,0,0,0,70,58,1,0,0,0,70,61,1,0,0,0,70,64,1,0,0,0,
        70,67,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,13,1,
        0,0,0,74,72,1,0,0,0,4,36,50,70,72
    ]

class ArdenParser ( Parser ):

    grammarFileName = "Arden.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'data:'", "';'", "'logic:'", "'action:'", 
                     "','", "'*'", "'/'", "'%'", "'+'", "'-'", "'>'", "'<'", 
                     "'>='", "'<='", "'=='", "'!='", "'&&'", "'||'", "'!'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "WS" ]

    RULE_module = 0
    RULE_dataBlock = 1
    RULE_logicBlock = 2
    RULE_actionBlock = 3
    RULE_statementList = 4
    RULE_statement = 5
    RULE_expr = 6

    ruleNames =  [ "module", "dataBlock", "logicBlock", "actionBlock", "statementList", 
                   "statement", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    ID=22
    INT=23
    WS=24

    def __init__(self, input:TokenStream, output=None):
        if output is None:
            output = sys.stdout
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ModuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataBlock(self):
            return self.getTypedRuleContext(ArdenParser.DataBlockContext,0)


        def logicBlock(self):
            return self.getTypedRuleContext(ArdenParser.LogicBlockContext,0)


        def actionBlock(self):
            return self.getTypedRuleContext(ArdenParser.ActionBlockContext,0)


        def EOF(self):
            return self.getToken(ArdenParser.EOF, 0)

        def getRuleIndex(self):
            return ArdenParser.RULE_module

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule" ):
                listener.enterModule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule" ):
                listener.exitModule(self)




    def module(self):

        localctx = ArdenParser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.dataBlock()
            self.state = 15
            self.logicBlock()
            self.state = 16
            self.actionBlock()
            self.state = 17
            self.match(ArdenParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(ArdenParser.StatementListContext,0)


        def getRuleIndex(self):
            return ArdenParser.RULE_dataBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataBlock" ):
                listener.enterDataBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataBlock" ):
                listener.exitDataBlock(self)




    def dataBlock(self):

        localctx = ArdenParser.DataBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dataBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(ArdenParser.T__0)
            self.state = 20
            self.statementList()
            self.state = 21
            self.match(ArdenParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(ArdenParser.StatementListContext,0)


        def getRuleIndex(self):
            return ArdenParser.RULE_logicBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicBlock" ):
                listener.enterLogicBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicBlock" ):
                listener.exitLogicBlock(self)




    def logicBlock(self):

        localctx = ArdenParser.LogicBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_logicBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(ArdenParser.T__2)
            self.state = 24
            self.statementList()
            self.state = 25
            self.match(ArdenParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(ArdenParser.StatementListContext,0)


        def getRuleIndex(self):
            return ArdenParser.RULE_actionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionBlock" ):
                listener.enterActionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionBlock" ):
                listener.exitActionBlock(self)




    def actionBlock(self):

        localctx = ArdenParser.ActionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_actionBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(ArdenParser.T__3)
            self.state = 28
            self.statementList()
            self.state = 29
            self.match(ArdenParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArdenParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArdenParser.StatementContext,i)


        def getRuleIndex(self):
            return ArdenParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = ArdenParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.statement()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 32
                self.match(ArdenParser.T__4)
                self.state = 33
                self.statement()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ArdenParser.ExprContext,0)


        def getRuleIndex(self):
            return ArdenParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ArdenParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArdenParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IntegerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArdenParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ArdenParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)


    class NotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArdenParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArdenParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)


    class IdentifierContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArdenParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ArdenParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)


    class OrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArdenParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArdenParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArdenParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArdenParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArdenParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArdenParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArdenParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArdenParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArdenParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArdenParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArdenParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArdenParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArdenParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArdenParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class AndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArdenParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArdenParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArdenParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)


    class EqualityContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArdenParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArdenParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArdenParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArdenParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = ArdenParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 42
                self.match(ArdenParser.T__18)
                self.state = 43
                self.expr(4)
                pass
            elif token in [20]:
                localctx = ArdenParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(ArdenParser.T__19)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(ArdenParser.T__20)
                pass
            elif token in [22]:
                localctx = ArdenParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(ArdenParser.ID)
                pass
            elif token in [23]:
                localctx = ArdenParser.IntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(ArdenParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 70
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ArdenParser.MulDivContext(self, ArdenParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 53
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = ArdenParser.AddSubContext(self, ArdenParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 56
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = ArdenParser.ComparisonContext(self, ArdenParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = ArdenParser.EqualityContext(self, ArdenParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 62
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 63
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = ArdenParser.AndContext(self, ArdenParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 64
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 65
                        localctx.op = self.match(ArdenParser.T__16)
                        self.state = 66
                        self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = ArdenParser.OrContext(self, ArdenParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 67
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 68
                        localctx.op = self.match(ArdenParser.T__17)
                        self.state = 69
                        self.expr(6)
                        pass

             
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         




