grammar Arden;

module: dataBlock logicBlock actionBlock EOF;

dataBlock: 'data:' statementList ';';
logicBlock: 'logic:' statementList ';';
actionBlock: 'action:' statementList ';';

statementList: statement (',' statement)*;
statement: expr;

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

ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;