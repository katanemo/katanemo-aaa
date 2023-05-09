// Generated from WhereCondition.g4 by ANTLR 4.7.

package parser // WhereCondition
import "github.com/antlr/antlr4/runtime/Go/antlr"

// WhereConditionListener is a complete listener for a parse tree produced by WhereConditionParser.
type WhereConditionListener interface {
	antlr.ParseTreeListener

	// EnterWhere_clause is called when entering the where_clause production.
	EnterWhere_clause(c *Where_clauseContext)

	// EnterComparisonExpression is called when entering the ComparisonExpression production.
	EnterComparisonExpression(c *ComparisonExpressionContext)

	// EnterLogicalExpressionInParen is called when entering the LogicalExpressionInParen production.
	EnterLogicalExpressionInParen(c *LogicalExpressionInParenContext)

	// EnterInExpression is called when entering the InExpression production.
	EnterInExpression(c *InExpressionContext)

	// EnterLogicalExpressionAnd is called when entering the LogicalExpressionAnd production.
	EnterLogicalExpressionAnd(c *LogicalExpressionAndContext)

	// EnterLogicalExpressionOr is called when entering the LogicalExpressionOr production.
	EnterLogicalExpressionOr(c *LogicalExpressionOrContext)

	// EnterComparisonExpressionWithOperator is called when entering the ComparisonExpressionWithOperator production.
	EnterComparisonExpressionWithOperator(c *ComparisonExpressionWithOperatorContext)

	// EnterComparisonExpressionParens is called when entering the ComparisonExpressionParens production.
	EnterComparisonExpressionParens(c *ComparisonExpressionParensContext)

	// EnterIn_expression is called when entering the in_expression production.
	EnterIn_expression(c *In_expressionContext)

	// EnterIn_list is called when entering the in_list production.
	EnterIn_list(c *In_listContext)

	// EnterComparison_operand is called when entering the comparison_operand production.
	EnterComparison_operand(c *Comparison_operandContext)

	// ExitWhere_clause is called when exiting the where_clause production.
	ExitWhere_clause(c *Where_clauseContext)

	// ExitComparisonExpression is called when exiting the ComparisonExpression production.
	ExitComparisonExpression(c *ComparisonExpressionContext)

	// ExitLogicalExpressionInParen is called when exiting the LogicalExpressionInParen production.
	ExitLogicalExpressionInParen(c *LogicalExpressionInParenContext)

	// ExitInExpression is called when exiting the InExpression production.
	ExitInExpression(c *InExpressionContext)

	// ExitLogicalExpressionAnd is called when exiting the LogicalExpressionAnd production.
	ExitLogicalExpressionAnd(c *LogicalExpressionAndContext)

	// ExitLogicalExpressionOr is called when exiting the LogicalExpressionOr production.
	ExitLogicalExpressionOr(c *LogicalExpressionOrContext)

	// ExitComparisonExpressionWithOperator is called when exiting the ComparisonExpressionWithOperator production.
	ExitComparisonExpressionWithOperator(c *ComparisonExpressionWithOperatorContext)

	// ExitComparisonExpressionParens is called when exiting the ComparisonExpressionParens production.
	ExitComparisonExpressionParens(c *ComparisonExpressionParensContext)

	// ExitIn_expression is called when exiting the in_expression production.
	ExitIn_expression(c *In_expressionContext)

	// ExitIn_list is called when exiting the in_list production.
	ExitIn_list(c *In_listContext)

	// ExitComparison_operand is called when exiting the comparison_operand production.
	ExitComparison_operand(c *Comparison_operandContext)
}
