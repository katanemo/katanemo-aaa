// Generated from WhereCondition.g4 by ANTLR 4.7.

package parser // WhereCondition
import (
	"fmt"
	"reflect"
	"strconv"

	"github.com/antlr/antlr4/runtime/Go/antlr"
)

// Suppress unused import errors
var _ = fmt.Printf
var _ = reflect.Copy
var _ = strconv.Itoa

var parserATN = []uint16{
	3, 24715, 42794, 33075, 47597, 16764, 15335, 30598, 22884, 3, 18, 70, 4,
	2, 9, 2, 4, 3, 9, 3, 4, 4, 9, 4, 4, 5, 9, 5, 4, 6, 9, 6, 4, 7, 9, 7, 3,
	2, 7, 2, 16, 10, 2, 12, 2, 14, 2, 19, 11, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3,
	3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 30, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
	3, 3, 3, 7, 3, 38, 10, 3, 12, 3, 14, 3, 41, 11, 3, 3, 4, 3, 4, 3, 4, 3,
	4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4, 51, 10, 4, 3, 5, 3, 5, 3, 5, 3, 5, 3,
	6, 3, 6, 3, 6, 3, 6, 7, 6, 61, 10, 6, 12, 6, 14, 6, 64, 11, 6, 3, 6, 3,
	6, 3, 7, 3, 7, 3, 7, 2, 3, 4, 8, 2, 4, 6, 8, 10, 12, 2, 3, 4, 2, 12, 13,
	15, 17, 2, 70, 2, 17, 3, 2, 2, 2, 4, 29, 3, 2, 2, 2, 6, 50, 3, 2, 2, 2,
	8, 52, 3, 2, 2, 2, 10, 56, 3, 2, 2, 2, 12, 67, 3, 2, 2, 2, 14, 16, 5, 4,
	3, 2, 15, 14, 3, 2, 2, 2, 16, 19, 3, 2, 2, 2, 17, 15, 3, 2, 2, 2, 17, 18,
	3, 2, 2, 2, 18, 20, 3, 2, 2, 2, 19, 17, 3, 2, 2, 2, 20, 21, 7, 2, 2, 3,
	21, 3, 3, 2, 2, 2, 22, 23, 8, 3, 1, 2, 23, 30, 5, 6, 4, 2, 24, 30, 5, 8,
	5, 2, 25, 26, 7, 10, 2, 2, 26, 27, 5, 4, 3, 2, 27, 28, 7, 11, 2, 2, 28,
	30, 3, 2, 2, 2, 29, 22, 3, 2, 2, 2, 29, 24, 3, 2, 2, 2, 29, 25, 3, 2, 2,
	2, 30, 39, 3, 2, 2, 2, 31, 32, 12, 7, 2, 2, 32, 33, 7, 4, 2, 2, 33, 38,
	5, 4, 3, 8, 34, 35, 12, 6, 2, 2, 35, 36, 7, 5, 2, 2, 36, 38, 5, 4, 3, 7,
	37, 31, 3, 2, 2, 2, 37, 34, 3, 2, 2, 2, 38, 41, 3, 2, 2, 2, 39, 37, 3,
	2, 2, 2, 39, 40, 3, 2, 2, 2, 40, 5, 3, 2, 2, 2, 41, 39, 3, 2, 2, 2, 42,
	43, 5, 12, 7, 2, 43, 44, 7, 9, 2, 2, 44, 45, 5, 12, 7, 2, 45, 51, 3, 2,
	2, 2, 46, 47, 7, 10, 2, 2, 47, 48, 5, 6, 4, 2, 48, 49, 7, 11, 2, 2, 49,
	51, 3, 2, 2, 2, 50, 42, 3, 2, 2, 2, 50, 46, 3, 2, 2, 2, 51, 7, 3, 2, 2,
	2, 52, 53, 5, 12, 7, 2, 53, 54, 7, 6, 2, 2, 54, 55, 5, 10, 6, 2, 55, 9,
	3, 2, 2, 2, 56, 57, 7, 10, 2, 2, 57, 62, 7, 13, 2, 2, 58, 59, 7, 3, 2,
	2, 59, 61, 7, 13, 2, 2, 60, 58, 3, 2, 2, 2, 61, 64, 3, 2, 2, 2, 62, 60,
	3, 2, 2, 2, 62, 63, 3, 2, 2, 2, 63, 65, 3, 2, 2, 2, 64, 62, 3, 2, 2, 2,
	65, 66, 7, 11, 2, 2, 66, 11, 3, 2, 2, 2, 67, 68, 9, 2, 2, 2, 68, 13, 3,
	2, 2, 2, 8, 17, 29, 37, 39, 50, 62,
}
var deserializer = antlr.NewATNDeserializer(nil)
var deserializedATN = deserializer.DeserializeFromUInt16(parserATN)

var literalNames = []string{
	"", "','", "'AND'", "'OR'", "'IN'", "'true'", "'false'", "'='", "'('",
	"')'",
}
var symbolicNames = []string{
	"", "", "AND", "OR", "IN", "TRUE", "FALSE", "EQ", "LPAREN", "RPAREN", "IDENTIFIER",
	"STRING", "TAG_KEY", "RESOURCETAGS", "PRINCIPALTAGS", "REQUEST", "WS",
}

var ruleNames = []string{
	"where_clause", "logical_expr", "comparison_expr", "in_expression", "in_list",
	"comparison_operand",
}
var decisionToDFA = make([]*antlr.DFA, len(deserializedATN.DecisionToState))

func init() {
	for index, ds := range deserializedATN.DecisionToState {
		decisionToDFA[index] = antlr.NewDFA(ds, index)
	}
}

type WhereConditionParser struct {
	*antlr.BaseParser
}

func NewWhereConditionParser(input antlr.TokenStream) *WhereConditionParser {
	this := new(WhereConditionParser)

	this.BaseParser = antlr.NewBaseParser(input)

	this.Interpreter = antlr.NewParserATNSimulator(this, deserializedATN, decisionToDFA, antlr.NewPredictionContextCache())
	this.RuleNames = ruleNames
	this.LiteralNames = literalNames
	this.SymbolicNames = symbolicNames
	this.GrammarFileName = "WhereCondition.g4"

	return this
}

// WhereConditionParser tokens.
const (
	WhereConditionParserEOF           = antlr.TokenEOF
	WhereConditionParserT__0          = 1
	WhereConditionParserAND           = 2
	WhereConditionParserOR            = 3
	WhereConditionParserIN            = 4
	WhereConditionParserTRUE          = 5
	WhereConditionParserFALSE         = 6
	WhereConditionParserEQ            = 7
	WhereConditionParserLPAREN        = 8
	WhereConditionParserRPAREN        = 9
	WhereConditionParserIDENTIFIER    = 10
	WhereConditionParserSTRING        = 11
	WhereConditionParserTAG_KEY       = 12
	WhereConditionParserRESOURCETAGS  = 13
	WhereConditionParserPRINCIPALTAGS = 14
	WhereConditionParserREQUEST       = 15
	WhereConditionParserWS            = 16
)

// WhereConditionParser rules.
const (
	WhereConditionParserRULE_where_clause       = 0
	WhereConditionParserRULE_logical_expr       = 1
	WhereConditionParserRULE_comparison_expr    = 2
	WhereConditionParserRULE_in_expression      = 3
	WhereConditionParserRULE_in_list            = 4
	WhereConditionParserRULE_comparison_operand = 5
)

// IWhere_clauseContext is an interface to support dynamic dispatch.
type IWhere_clauseContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsWhere_clauseContext differentiates from other interfaces.
	IsWhere_clauseContext()
}

type Where_clauseContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyWhere_clauseContext() *Where_clauseContext {
	var p = new(Where_clauseContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = WhereConditionParserRULE_where_clause
	return p
}

func (*Where_clauseContext) IsWhere_clauseContext() {}

func NewWhere_clauseContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *Where_clauseContext {
	var p = new(Where_clauseContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = WhereConditionParserRULE_where_clause

	return p
}

func (s *Where_clauseContext) GetParser() antlr.Parser { return s.parser }

func (s *Where_clauseContext) EOF() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserEOF, 0)
}

func (s *Where_clauseContext) AllLogical_expr() []ILogical_exprContext {
	var ts = s.GetTypedRuleContexts(reflect.TypeOf((*ILogical_exprContext)(nil)).Elem())
	var tst = make([]ILogical_exprContext, len(ts))

	for i, t := range ts {
		if t != nil {
			tst[i] = t.(ILogical_exprContext)
		}
	}

	return tst
}

func (s *Where_clauseContext) Logical_expr(i int) ILogical_exprContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*ILogical_exprContext)(nil)).Elem(), i)

	if t == nil {
		return nil
	}

	return t.(ILogical_exprContext)
}

func (s *Where_clauseContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *Where_clauseContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *Where_clauseContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.EnterWhere_clause(s)
	}
}

func (s *Where_clauseContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.ExitWhere_clause(s)
	}
}

func (p *WhereConditionParser) Where_clause() (localctx IWhere_clauseContext) {
	localctx = NewWhere_clauseContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 0, WhereConditionParserRULE_where_clause)
	var _la int

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	p.SetState(15)
	p.GetErrorHandler().Sync(p)
	_la = p.GetTokenStream().LA(1)

	for ((_la)&-(0x1f+1)) == 0 && ((1<<uint(_la))&((1<<WhereConditionParserLPAREN)|(1<<WhereConditionParserIDENTIFIER)|(1<<WhereConditionParserSTRING)|(1<<WhereConditionParserRESOURCETAGS)|(1<<WhereConditionParserPRINCIPALTAGS)|(1<<WhereConditionParserREQUEST))) != 0 {
		{
			p.SetState(12)
			p.logical_expr(0)
		}

		p.SetState(17)
		p.GetErrorHandler().Sync(p)
		_la = p.GetTokenStream().LA(1)
	}
	{
		p.SetState(18)
		p.Match(WhereConditionParserEOF)
	}

	return localctx
}

// ILogical_exprContext is an interface to support dynamic dispatch.
type ILogical_exprContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsLogical_exprContext differentiates from other interfaces.
	IsLogical_exprContext()
}

type Logical_exprContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyLogical_exprContext() *Logical_exprContext {
	var p = new(Logical_exprContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = WhereConditionParserRULE_logical_expr
	return p
}

func (*Logical_exprContext) IsLogical_exprContext() {}

func NewLogical_exprContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *Logical_exprContext {
	var p = new(Logical_exprContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = WhereConditionParserRULE_logical_expr

	return p
}

func (s *Logical_exprContext) GetParser() antlr.Parser { return s.parser }

func (s *Logical_exprContext) CopyFrom(ctx *Logical_exprContext) {
	s.BaseParserRuleContext.CopyFrom(ctx.BaseParserRuleContext)
}

func (s *Logical_exprContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *Logical_exprContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

type ComparisonExpressionContext struct {
	*Logical_exprContext
}

func NewComparisonExpressionContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *ComparisonExpressionContext {
	var p = new(ComparisonExpressionContext)

	p.Logical_exprContext = NewEmptyLogical_exprContext()
	p.parser = parser
	p.CopyFrom(ctx.(*Logical_exprContext))

	return p
}

func (s *ComparisonExpressionContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ComparisonExpressionContext) Comparison_expr() IComparison_exprContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IComparison_exprContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IComparison_exprContext)
}

func (s *ComparisonExpressionContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.EnterComparisonExpression(s)
	}
}

func (s *ComparisonExpressionContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.ExitComparisonExpression(s)
	}
}

type LogicalExpressionInParenContext struct {
	*Logical_exprContext
}

func NewLogicalExpressionInParenContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *LogicalExpressionInParenContext {
	var p = new(LogicalExpressionInParenContext)

	p.Logical_exprContext = NewEmptyLogical_exprContext()
	p.parser = parser
	p.CopyFrom(ctx.(*Logical_exprContext))

	return p
}

func (s *LogicalExpressionInParenContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *LogicalExpressionInParenContext) LPAREN() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserLPAREN, 0)
}

func (s *LogicalExpressionInParenContext) Logical_expr() ILogical_exprContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*ILogical_exprContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(ILogical_exprContext)
}

func (s *LogicalExpressionInParenContext) RPAREN() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserRPAREN, 0)
}

func (s *LogicalExpressionInParenContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.EnterLogicalExpressionInParen(s)
	}
}

func (s *LogicalExpressionInParenContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.ExitLogicalExpressionInParen(s)
	}
}

type InExpressionContext struct {
	*Logical_exprContext
}

func NewInExpressionContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *InExpressionContext {
	var p = new(InExpressionContext)

	p.Logical_exprContext = NewEmptyLogical_exprContext()
	p.parser = parser
	p.CopyFrom(ctx.(*Logical_exprContext))

	return p
}

func (s *InExpressionContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *InExpressionContext) In_expression() IIn_expressionContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IIn_expressionContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IIn_expressionContext)
}

func (s *InExpressionContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.EnterInExpression(s)
	}
}

func (s *InExpressionContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.ExitInExpression(s)
	}
}

type LogicalExpressionAndContext struct {
	*Logical_exprContext
}

func NewLogicalExpressionAndContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *LogicalExpressionAndContext {
	var p = new(LogicalExpressionAndContext)

	p.Logical_exprContext = NewEmptyLogical_exprContext()
	p.parser = parser
	p.CopyFrom(ctx.(*Logical_exprContext))

	return p
}

func (s *LogicalExpressionAndContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *LogicalExpressionAndContext) AllLogical_expr() []ILogical_exprContext {
	var ts = s.GetTypedRuleContexts(reflect.TypeOf((*ILogical_exprContext)(nil)).Elem())
	var tst = make([]ILogical_exprContext, len(ts))

	for i, t := range ts {
		if t != nil {
			tst[i] = t.(ILogical_exprContext)
		}
	}

	return tst
}

func (s *LogicalExpressionAndContext) Logical_expr(i int) ILogical_exprContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*ILogical_exprContext)(nil)).Elem(), i)

	if t == nil {
		return nil
	}

	return t.(ILogical_exprContext)
}

func (s *LogicalExpressionAndContext) AND() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserAND, 0)
}

func (s *LogicalExpressionAndContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.EnterLogicalExpressionAnd(s)
	}
}

func (s *LogicalExpressionAndContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.ExitLogicalExpressionAnd(s)
	}
}

type LogicalExpressionOrContext struct {
	*Logical_exprContext
}

func NewLogicalExpressionOrContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *LogicalExpressionOrContext {
	var p = new(LogicalExpressionOrContext)

	p.Logical_exprContext = NewEmptyLogical_exprContext()
	p.parser = parser
	p.CopyFrom(ctx.(*Logical_exprContext))

	return p
}

func (s *LogicalExpressionOrContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *LogicalExpressionOrContext) AllLogical_expr() []ILogical_exprContext {
	var ts = s.GetTypedRuleContexts(reflect.TypeOf((*ILogical_exprContext)(nil)).Elem())
	var tst = make([]ILogical_exprContext, len(ts))

	for i, t := range ts {
		if t != nil {
			tst[i] = t.(ILogical_exprContext)
		}
	}

	return tst
}

func (s *LogicalExpressionOrContext) Logical_expr(i int) ILogical_exprContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*ILogical_exprContext)(nil)).Elem(), i)

	if t == nil {
		return nil
	}

	return t.(ILogical_exprContext)
}

func (s *LogicalExpressionOrContext) OR() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserOR, 0)
}

func (s *LogicalExpressionOrContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.EnterLogicalExpressionOr(s)
	}
}

func (s *LogicalExpressionOrContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.ExitLogicalExpressionOr(s)
	}
}

func (p *WhereConditionParser) Logical_expr() (localctx ILogical_exprContext) {
	return p.logical_expr(0)
}

func (p *WhereConditionParser) logical_expr(_p int) (localctx ILogical_exprContext) {
	var _parentctx antlr.ParserRuleContext = p.GetParserRuleContext()
	_parentState := p.GetState()
	localctx = NewLogical_exprContext(p, p.GetParserRuleContext(), _parentState)
	var _prevctx ILogical_exprContext = localctx
	var _ antlr.ParserRuleContext = _prevctx // TODO: To prevent unused variable warning.
	_startState := 2
	p.EnterRecursionRule(localctx, 2, WhereConditionParserRULE_logical_expr, _p)

	defer func() {
		p.UnrollRecursionContexts(_parentctx)
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	var _alt int

	p.EnterOuterAlt(localctx, 1)
	p.SetState(27)
	p.GetErrorHandler().Sync(p)
	switch p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 1, p.GetParserRuleContext()) {
	case 1:
		localctx = NewComparisonExpressionContext(p, localctx)
		p.SetParserRuleContext(localctx)
		_prevctx = localctx

		{
			p.SetState(21)
			p.Comparison_expr()
		}

	case 2:
		localctx = NewInExpressionContext(p, localctx)
		p.SetParserRuleContext(localctx)
		_prevctx = localctx
		{
			p.SetState(22)
			p.In_expression()
		}

	case 3:
		localctx = NewLogicalExpressionInParenContext(p, localctx)
		p.SetParserRuleContext(localctx)
		_prevctx = localctx
		{
			p.SetState(23)
			p.Match(WhereConditionParserLPAREN)
		}
		{
			p.SetState(24)
			p.logical_expr(0)
		}
		{
			p.SetState(25)
			p.Match(WhereConditionParserRPAREN)
		}

	}
	p.GetParserRuleContext().SetStop(p.GetTokenStream().LT(-1))
	p.SetState(37)
	p.GetErrorHandler().Sync(p)
	_alt = p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 3, p.GetParserRuleContext())

	for _alt != 2 && _alt != antlr.ATNInvalidAltNumber {
		if _alt == 1 {
			if p.GetParseListeners() != nil {
				p.TriggerExitRuleEvent()
			}
			_prevctx = localctx
			p.SetState(35)
			p.GetErrorHandler().Sync(p)
			switch p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 2, p.GetParserRuleContext()) {
			case 1:
				localctx = NewLogicalExpressionAndContext(p, NewLogical_exprContext(p, _parentctx, _parentState))
				p.PushNewRecursionContext(localctx, _startState, WhereConditionParserRULE_logical_expr)
				p.SetState(29)

				if !(p.Precpred(p.GetParserRuleContext(), 5)) {
					panic(antlr.NewFailedPredicateException(p, "p.Precpred(p.GetParserRuleContext(), 5)", ""))
				}
				{
					p.SetState(30)
					p.Match(WhereConditionParserAND)
				}
				{
					p.SetState(31)
					p.logical_expr(6)
				}

			case 2:
				localctx = NewLogicalExpressionOrContext(p, NewLogical_exprContext(p, _parentctx, _parentState))
				p.PushNewRecursionContext(localctx, _startState, WhereConditionParserRULE_logical_expr)
				p.SetState(32)

				if !(p.Precpred(p.GetParserRuleContext(), 4)) {
					panic(antlr.NewFailedPredicateException(p, "p.Precpred(p.GetParserRuleContext(), 4)", ""))
				}
				{
					p.SetState(33)
					p.Match(WhereConditionParserOR)
				}
				{
					p.SetState(34)
					p.logical_expr(5)
				}

			}

		}
		p.SetState(39)
		p.GetErrorHandler().Sync(p)
		_alt = p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 3, p.GetParserRuleContext())
	}

	return localctx
}

// IComparison_exprContext is an interface to support dynamic dispatch.
type IComparison_exprContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsComparison_exprContext differentiates from other interfaces.
	IsComparison_exprContext()
}

type Comparison_exprContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyComparison_exprContext() *Comparison_exprContext {
	var p = new(Comparison_exprContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = WhereConditionParserRULE_comparison_expr
	return p
}

func (*Comparison_exprContext) IsComparison_exprContext() {}

func NewComparison_exprContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *Comparison_exprContext {
	var p = new(Comparison_exprContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = WhereConditionParserRULE_comparison_expr

	return p
}

func (s *Comparison_exprContext) GetParser() antlr.Parser { return s.parser }

func (s *Comparison_exprContext) CopyFrom(ctx *Comparison_exprContext) {
	s.BaseParserRuleContext.CopyFrom(ctx.BaseParserRuleContext)
}

func (s *Comparison_exprContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *Comparison_exprContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

type ComparisonExpressionParensContext struct {
	*Comparison_exprContext
}

func NewComparisonExpressionParensContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *ComparisonExpressionParensContext {
	var p = new(ComparisonExpressionParensContext)

	p.Comparison_exprContext = NewEmptyComparison_exprContext()
	p.parser = parser
	p.CopyFrom(ctx.(*Comparison_exprContext))

	return p
}

func (s *ComparisonExpressionParensContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ComparisonExpressionParensContext) LPAREN() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserLPAREN, 0)
}

func (s *ComparisonExpressionParensContext) Comparison_expr() IComparison_exprContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IComparison_exprContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IComparison_exprContext)
}

func (s *ComparisonExpressionParensContext) RPAREN() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserRPAREN, 0)
}

func (s *ComparisonExpressionParensContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.EnterComparisonExpressionParens(s)
	}
}

func (s *ComparisonExpressionParensContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.ExitComparisonExpressionParens(s)
	}
}

type ComparisonExpressionWithOperatorContext struct {
	*Comparison_exprContext
}

func NewComparisonExpressionWithOperatorContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *ComparisonExpressionWithOperatorContext {
	var p = new(ComparisonExpressionWithOperatorContext)

	p.Comparison_exprContext = NewEmptyComparison_exprContext()
	p.parser = parser
	p.CopyFrom(ctx.(*Comparison_exprContext))

	return p
}

func (s *ComparisonExpressionWithOperatorContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ComparisonExpressionWithOperatorContext) AllComparison_operand() []IComparison_operandContext {
	var ts = s.GetTypedRuleContexts(reflect.TypeOf((*IComparison_operandContext)(nil)).Elem())
	var tst = make([]IComparison_operandContext, len(ts))

	for i, t := range ts {
		if t != nil {
			tst[i] = t.(IComparison_operandContext)
		}
	}

	return tst
}

func (s *ComparisonExpressionWithOperatorContext) Comparison_operand(i int) IComparison_operandContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IComparison_operandContext)(nil)).Elem(), i)

	if t == nil {
		return nil
	}

	return t.(IComparison_operandContext)
}

func (s *ComparisonExpressionWithOperatorContext) EQ() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserEQ, 0)
}

func (s *ComparisonExpressionWithOperatorContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.EnterComparisonExpressionWithOperator(s)
	}
}

func (s *ComparisonExpressionWithOperatorContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.ExitComparisonExpressionWithOperator(s)
	}
}

func (p *WhereConditionParser) Comparison_expr() (localctx IComparison_exprContext) {
	localctx = NewComparison_exprContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 4, WhereConditionParserRULE_comparison_expr)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.SetState(48)
	p.GetErrorHandler().Sync(p)

	switch p.GetTokenStream().LA(1) {
	case WhereConditionParserIDENTIFIER, WhereConditionParserSTRING, WhereConditionParserRESOURCETAGS, WhereConditionParserPRINCIPALTAGS, WhereConditionParserREQUEST:
		localctx = NewComparisonExpressionWithOperatorContext(p, localctx)
		p.EnterOuterAlt(localctx, 1)
		{
			p.SetState(40)
			p.Comparison_operand()
		}
		{
			p.SetState(41)
			p.Match(WhereConditionParserEQ)
		}
		{
			p.SetState(42)
			p.Comparison_operand()
		}

	case WhereConditionParserLPAREN:
		localctx = NewComparisonExpressionParensContext(p, localctx)
		p.EnterOuterAlt(localctx, 2)
		{
			p.SetState(44)
			p.Match(WhereConditionParserLPAREN)
		}
		{
			p.SetState(45)
			p.Comparison_expr()
		}
		{
			p.SetState(46)
			p.Match(WhereConditionParserRPAREN)
		}

	default:
		panic(antlr.NewNoViableAltException(p, nil, nil, nil, nil, nil))
	}

	return localctx
}

// IIn_expressionContext is an interface to support dynamic dispatch.
type IIn_expressionContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsIn_expressionContext differentiates from other interfaces.
	IsIn_expressionContext()
}

type In_expressionContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyIn_expressionContext() *In_expressionContext {
	var p = new(In_expressionContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = WhereConditionParserRULE_in_expression
	return p
}

func (*In_expressionContext) IsIn_expressionContext() {}

func NewIn_expressionContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *In_expressionContext {
	var p = new(In_expressionContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = WhereConditionParserRULE_in_expression

	return p
}

func (s *In_expressionContext) GetParser() antlr.Parser { return s.parser }

func (s *In_expressionContext) Comparison_operand() IComparison_operandContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IComparison_operandContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IComparison_operandContext)
}

func (s *In_expressionContext) IN() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserIN, 0)
}

func (s *In_expressionContext) In_list() IIn_listContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IIn_listContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IIn_listContext)
}

func (s *In_expressionContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *In_expressionContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *In_expressionContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.EnterIn_expression(s)
	}
}

func (s *In_expressionContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.ExitIn_expression(s)
	}
}

func (p *WhereConditionParser) In_expression() (localctx IIn_expressionContext) {
	localctx = NewIn_expressionContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 6, WhereConditionParserRULE_in_expression)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(50)
		p.Comparison_operand()
	}
	{
		p.SetState(51)
		p.Match(WhereConditionParserIN)
	}
	{
		p.SetState(52)
		p.In_list()
	}

	return localctx
}

// IIn_listContext is an interface to support dynamic dispatch.
type IIn_listContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsIn_listContext differentiates from other interfaces.
	IsIn_listContext()
}

type In_listContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyIn_listContext() *In_listContext {
	var p = new(In_listContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = WhereConditionParserRULE_in_list
	return p
}

func (*In_listContext) IsIn_listContext() {}

func NewIn_listContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *In_listContext {
	var p = new(In_listContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = WhereConditionParserRULE_in_list

	return p
}

func (s *In_listContext) GetParser() antlr.Parser { return s.parser }

func (s *In_listContext) AllSTRING() []antlr.TerminalNode {
	return s.GetTokens(WhereConditionParserSTRING)
}

func (s *In_listContext) STRING(i int) antlr.TerminalNode {
	return s.GetToken(WhereConditionParserSTRING, i)
}

func (s *In_listContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *In_listContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *In_listContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.EnterIn_list(s)
	}
}

func (s *In_listContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.ExitIn_list(s)
	}
}

func (p *WhereConditionParser) In_list() (localctx IIn_listContext) {
	localctx = NewIn_listContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 8, WhereConditionParserRULE_in_list)
	var _la int

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(54)
		p.Match(WhereConditionParserLPAREN)
	}
	{
		p.SetState(55)
		p.Match(WhereConditionParserSTRING)
	}
	p.SetState(60)
	p.GetErrorHandler().Sync(p)
	_la = p.GetTokenStream().LA(1)

	for _la == WhereConditionParserT__0 {
		{
			p.SetState(56)
			p.Match(WhereConditionParserT__0)
		}
		{
			p.SetState(57)
			p.Match(WhereConditionParserSTRING)
		}

		p.SetState(62)
		p.GetErrorHandler().Sync(p)
		_la = p.GetTokenStream().LA(1)
	}
	{
		p.SetState(63)
		p.Match(WhereConditionParserRPAREN)
	}

	return localctx
}

// IComparison_operandContext is an interface to support dynamic dispatch.
type IComparison_operandContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsComparison_operandContext differentiates from other interfaces.
	IsComparison_operandContext()
}

type Comparison_operandContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyComparison_operandContext() *Comparison_operandContext {
	var p = new(Comparison_operandContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = WhereConditionParserRULE_comparison_operand
	return p
}

func (*Comparison_operandContext) IsComparison_operandContext() {}

func NewComparison_operandContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *Comparison_operandContext {
	var p = new(Comparison_operandContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = WhereConditionParserRULE_comparison_operand

	return p
}

func (s *Comparison_operandContext) GetParser() antlr.Parser { return s.parser }

func (s *Comparison_operandContext) RESOURCETAGS() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserRESOURCETAGS, 0)
}

func (s *Comparison_operandContext) REQUEST() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserREQUEST, 0)
}

func (s *Comparison_operandContext) PRINCIPALTAGS() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserPRINCIPALTAGS, 0)
}

func (s *Comparison_operandContext) IDENTIFIER() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserIDENTIFIER, 0)
}

func (s *Comparison_operandContext) STRING() antlr.TerminalNode {
	return s.GetToken(WhereConditionParserSTRING, 0)
}

func (s *Comparison_operandContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *Comparison_operandContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *Comparison_operandContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.EnterComparison_operand(s)
	}
}

func (s *Comparison_operandContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(WhereConditionListener); ok {
		listenerT.ExitComparison_operand(s)
	}
}

func (p *WhereConditionParser) Comparison_operand() (localctx IComparison_operandContext) {
	localctx = NewComparison_operandContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 10, WhereConditionParserRULE_comparison_operand)
	var _la int

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	p.SetState(65)
	_la = p.GetTokenStream().LA(1)

	if !(((_la)&-(0x1f+1)) == 0 && ((1<<uint(_la))&((1<<WhereConditionParserIDENTIFIER)|(1<<WhereConditionParserSTRING)|(1<<WhereConditionParserRESOURCETAGS)|(1<<WhereConditionParserPRINCIPALTAGS)|(1<<WhereConditionParserREQUEST))) != 0) {
		p.GetErrorHandler().RecoverInline(p)
	} else {
		p.GetErrorHandler().ReportMatch(p)
		p.Consume()
	}

	return localctx
}

func (p *WhereConditionParser) Sempred(localctx antlr.RuleContext, ruleIndex, predIndex int) bool {
	switch ruleIndex {
	case 1:
		var t *Logical_exprContext = nil
		if localctx != nil {
			t = localctx.(*Logical_exprContext)
		}
		return p.Logical_expr_Sempred(t, predIndex)

	default:
		panic("No predicate with index: " + fmt.Sprint(ruleIndex))
	}
}

func (p *WhereConditionParser) Logical_expr_Sempred(localctx antlr.RuleContext, predIndex int) bool {
	switch predIndex {
	case 0:
		return p.Precpred(p.GetParserRuleContext(), 5)

	case 1:
		return p.Precpred(p.GetParserRuleContext(), 4)

	default:
		panic("No predicate with index: " + fmt.Sprint(predIndex))
	}
}
