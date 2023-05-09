grammar WhereCondition;

/* Lexical rules */

AND : 'AND' ;
OR  : 'OR' ;
IN  : 'IN';
TRUE  : 'true' ;
FALSE : 'false' ;

EQ : '=' ;

LPAREN : '(' ;
RPAREN : ')' ;


IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9\\.]* ;
STRING : '\''IDENTIFIER'\'';

TAG_KEY : ':'IDENTIFIER;
RESOURCETAGS : '$resourceTags'TAG_KEY;
PRINCIPALTAGS : '$principalTags'TAG_KEY;
REQUEST : '$request'TAG_KEY;

WS : [ \r\t\u000C\n]+ -> skip ;


where_clause : logical_expr* EOF ;

logical_expr
 : logical_expr AND logical_expr # LogicalExpressionAnd
 | logical_expr OR logical_expr  # LogicalExpressionOr
 | comparison_expr               # ComparisonExpression
 | in_expression                  # InExpression
 | LPAREN logical_expr RPAREN    # LogicalExpressionInParen
 ;

comparison_expr : comparison_operand EQ comparison_operand
                    # ComparisonExpressionWithOperator
                | LPAREN comparison_expr RPAREN # ComparisonExpressionParens
                ;
in_expression : comparison_operand IN in_list;
in_list: '(' STRING (',' STRING)* ')';

comparison_operand : (RESOURCETAGS | REQUEST | PRINCIPALTAGS | IDENTIFIER | STRING)
                   ;
