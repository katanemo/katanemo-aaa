// Generated from WhereCondition.g4 by ANTLR 4.7.

package parser // WhereCondition
import "github.com/antlr/antlr4/runtime/Go/antlr"

// BaseWhereConditionListener is a complete listener for a parse tree produced by WhereConditionParser.
type BaseWhereConditionListener struct{}

var _ WhereConditionListener = &BaseWhereConditionListener{}

// VisitTerminal is called when a terminal node is visited.
func (s *BaseWhereConditionListener) VisitTerminal(node antlr.TerminalNode) {}

// VisitErrorNode is called when an error node is visited.
func (s *BaseWhereConditionListener) VisitErrorNode(node antlr.ErrorNode) {}

// EnterEveryRule is called when any rule is entered.
func (s *BaseWhereConditionListener) EnterEveryRule(ctx antlr.ParserRuleContext) {}

// ExitEveryRule is called when any rule is exited.
func (s *BaseWhereConditionListener) ExitEveryRule(ctx antlr.ParserRuleContext) {}

// EnterWhere_clause is called when production where_clause is entered.
func (s *BaseWhereConditionListener) EnterWhere_clause(ctx *Where_clauseContext) {}

// ExitWhere_clause is called when production where_clause is exited.
func (s *BaseWhereConditionListener) ExitWhere_clause(ctx *Where_clauseContext) {}

// EnterComparisonExpression is called when production ComparisonExpression is entered.
func (s *BaseWhereConditionListener) EnterComparisonExpression(ctx *ComparisonExpressionContext) {}

// ExitComparisonExpression is called when production ComparisonExpression is exited.
func (s *BaseWhereConditionListener) ExitComparisonExpression(ctx *ComparisonExpressionContext) {}

// EnterLogicalExpressionInParen is called when production LogicalExpressionInParen is entered.
func (s *BaseWhereConditionListener) EnterLogicalExpressionInParen(ctx *LogicalExpressionInParenContext) {
}

// ExitLogicalExpressionInParen is called when production LogicalExpressionInParen is exited.
func (s *BaseWhereConditionListener) ExitLogicalExpressionInParen(ctx *LogicalExpressionInParenContext) {
}

// EnterInExpression is called when production InExpression is entered.
func (s *BaseWhereConditionListener) EnterInExpression(ctx *InExpressionContext) {}

// ExitInExpression is called when production InExpression is exited.
func (s *BaseWhereConditionListener) ExitInExpression(ctx *InExpressionContext) {}

// EnterLogicalExpressionAnd is called when production LogicalExpressionAnd is entered.
func (s *BaseWhereConditionListener) EnterLogicalExpressionAnd(ctx *LogicalExpressionAndContext) {}

// ExitLogicalExpressionAnd is called when production LogicalExpressionAnd is exited.
func (s *BaseWhereConditionListener) ExitLogicalExpressionAnd(ctx *LogicalExpressionAndContext) {}

// EnterLogicalExpressionOr is called when production LogicalExpressionOr is entered.
func (s *BaseWhereConditionListener) EnterLogicalExpressionOr(ctx *LogicalExpressionOrContext) {}

// ExitLogicalExpressionOr is called when production LogicalExpressionOr is exited.
func (s *BaseWhereConditionListener) ExitLogicalExpressionOr(ctx *LogicalExpressionOrContext) {}

// EnterComparisonExpressionWithOperator is called when production ComparisonExpressionWithOperator is entered.
func (s *BaseWhereConditionListener) EnterComparisonExpressionWithOperator(ctx *ComparisonExpressionWithOperatorContext) {
}

// ExitComparisonExpressionWithOperator is called when production ComparisonExpressionWithOperator is exited.
func (s *BaseWhereConditionListener) ExitComparisonExpressionWithOperator(ctx *ComparisonExpressionWithOperatorContext) {
}

// EnterComparisonExpressionParens is called when production ComparisonExpressionParens is entered.
func (s *BaseWhereConditionListener) EnterComparisonExpressionParens(ctx *ComparisonExpressionParensContext) {
}

// ExitComparisonExpressionParens is called when production ComparisonExpressionParens is exited.
func (s *BaseWhereConditionListener) ExitComparisonExpressionParens(ctx *ComparisonExpressionParensContext) {
}

// EnterIn_expression is called when production in_expression is entered.
func (s *BaseWhereConditionListener) EnterIn_expression(ctx *In_expressionContext) {}

// ExitIn_expression is called when production in_expression is exited.
func (s *BaseWhereConditionListener) ExitIn_expression(ctx *In_expressionContext) {}

// EnterIn_list is called when production in_list is entered.
func (s *BaseWhereConditionListener) EnterIn_list(ctx *In_listContext) {}

// ExitIn_list is called when production in_list is exited.
func (s *BaseWhereConditionListener) ExitIn_list(ctx *In_listContext) {}

// EnterComparison_operand is called when production comparison_operand is entered.
func (s *BaseWhereConditionListener) EnterComparison_operand(ctx *Comparison_operandContext) {}

// ExitComparison_operand is called when production comparison_operand is exited.
func (s *BaseWhereConditionListener) ExitComparison_operand(ctx *Comparison_operandContext) {}
