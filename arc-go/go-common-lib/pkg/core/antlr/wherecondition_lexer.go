// Generated from WhereCondition.g4 by ANTLR 4.7.

package parser

import (
	"fmt"
	"unicode"

	"github.com/antlr/antlr4/runtime/Go/antlr"
)

// Suppress unused import error
var _ = fmt.Printf
var _ = unicode.IsLetter

var serializedLexerAtn = []uint16{
	3, 24715, 42794, 33075, 47597, 16764, 15335, 30598, 22884, 2, 18, 129,
	8, 1, 4, 2, 9, 2, 4, 3, 9, 3, 4, 4, 9, 4, 4, 5, 9, 5, 4, 6, 9, 6, 4, 7,
	9, 7, 4, 8, 9, 8, 4, 9, 9, 9, 4, 10, 9, 10, 4, 11, 9, 11, 4, 12, 9, 12,
	4, 13, 9, 13, 4, 14, 9, 14, 4, 15, 9, 15, 4, 16, 9, 16, 4, 17, 9, 17, 3,
	2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 4, 3, 4, 3, 5, 3, 5, 3, 5, 3,
	6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 8, 3,
	8, 3, 9, 3, 9, 3, 10, 3, 10, 3, 11, 3, 11, 7, 11, 67, 10, 11, 12, 11, 14,
	11, 70, 11, 11, 3, 12, 3, 12, 3, 12, 3, 12, 3, 13, 3, 13, 3, 13, 3, 14,
	3, 14, 3, 14, 3, 14, 3, 14, 3, 14, 3, 14, 3, 14, 3, 14, 3, 14, 3, 14, 3,
	14, 3, 14, 3, 14, 3, 14, 3, 14, 3, 15, 3, 15, 3, 15, 3, 15, 3, 15, 3, 15,
	3, 15, 3, 15, 3, 15, 3, 15, 3, 15, 3, 15, 3, 15, 3, 15, 3, 15, 3, 15, 3,
	15, 3, 16, 3, 16, 3, 16, 3, 16, 3, 16, 3, 16, 3, 16, 3, 16, 3, 16, 3, 16,
	3, 16, 3, 17, 6, 17, 124, 10, 17, 13, 17, 14, 17, 125, 3, 17, 3, 17, 2,
	2, 18, 3, 3, 5, 4, 7, 5, 9, 6, 11, 7, 13, 8, 15, 9, 17, 10, 19, 11, 21,
	12, 23, 13, 25, 14, 27, 15, 29, 16, 31, 17, 33, 18, 3, 2, 5, 5, 2, 67,
	92, 97, 97, 99, 124, 8, 2, 48, 48, 50, 59, 67, 92, 94, 94, 97, 97, 99,
	124, 5, 2, 11, 12, 14, 15, 34, 34, 2, 130, 2, 3, 3, 2, 2, 2, 2, 5, 3, 2,
	2, 2, 2, 7, 3, 2, 2, 2, 2, 9, 3, 2, 2, 2, 2, 11, 3, 2, 2, 2, 2, 13, 3,
	2, 2, 2, 2, 15, 3, 2, 2, 2, 2, 17, 3, 2, 2, 2, 2, 19, 3, 2, 2, 2, 2, 21,
	3, 2, 2, 2, 2, 23, 3, 2, 2, 2, 2, 25, 3, 2, 2, 2, 2, 27, 3, 2, 2, 2, 2,
	29, 3, 2, 2, 2, 2, 31, 3, 2, 2, 2, 2, 33, 3, 2, 2, 2, 3, 35, 3, 2, 2, 2,
	5, 37, 3, 2, 2, 2, 7, 41, 3, 2, 2, 2, 9, 44, 3, 2, 2, 2, 11, 47, 3, 2,
	2, 2, 13, 52, 3, 2, 2, 2, 15, 58, 3, 2, 2, 2, 17, 60, 3, 2, 2, 2, 19, 62,
	3, 2, 2, 2, 21, 64, 3, 2, 2, 2, 23, 71, 3, 2, 2, 2, 25, 75, 3, 2, 2, 2,
	27, 78, 3, 2, 2, 2, 29, 94, 3, 2, 2, 2, 31, 111, 3, 2, 2, 2, 33, 123, 3,
	2, 2, 2, 35, 36, 7, 46, 2, 2, 36, 4, 3, 2, 2, 2, 37, 38, 7, 67, 2, 2, 38,
	39, 7, 80, 2, 2, 39, 40, 7, 70, 2, 2, 40, 6, 3, 2, 2, 2, 41, 42, 7, 81,
	2, 2, 42, 43, 7, 84, 2, 2, 43, 8, 3, 2, 2, 2, 44, 45, 7, 75, 2, 2, 45,
	46, 7, 80, 2, 2, 46, 10, 3, 2, 2, 2, 47, 48, 7, 118, 2, 2, 48, 49, 7, 116,
	2, 2, 49, 50, 7, 119, 2, 2, 50, 51, 7, 103, 2, 2, 51, 12, 3, 2, 2, 2, 52,
	53, 7, 104, 2, 2, 53, 54, 7, 99, 2, 2, 54, 55, 7, 110, 2, 2, 55, 56, 7,
	117, 2, 2, 56, 57, 7, 103, 2, 2, 57, 14, 3, 2, 2, 2, 58, 59, 7, 63, 2,
	2, 59, 16, 3, 2, 2, 2, 60, 61, 7, 42, 2, 2, 61, 18, 3, 2, 2, 2, 62, 63,
	7, 43, 2, 2, 63, 20, 3, 2, 2, 2, 64, 68, 9, 2, 2, 2, 65, 67, 9, 3, 2, 2,
	66, 65, 3, 2, 2, 2, 67, 70, 3, 2, 2, 2, 68, 66, 3, 2, 2, 2, 68, 69, 3,
	2, 2, 2, 69, 22, 3, 2, 2, 2, 70, 68, 3, 2, 2, 2, 71, 72, 7, 41, 2, 2, 72,
	73, 5, 21, 11, 2, 73, 74, 7, 41, 2, 2, 74, 24, 3, 2, 2, 2, 75, 76, 7, 60,
	2, 2, 76, 77, 5, 21, 11, 2, 77, 26, 3, 2, 2, 2, 78, 79, 7, 38, 2, 2, 79,
	80, 7, 116, 2, 2, 80, 81, 7, 103, 2, 2, 81, 82, 7, 117, 2, 2, 82, 83, 7,
	113, 2, 2, 83, 84, 7, 119, 2, 2, 84, 85, 7, 116, 2, 2, 85, 86, 7, 101,
	2, 2, 86, 87, 7, 103, 2, 2, 87, 88, 7, 86, 2, 2, 88, 89, 7, 99, 2, 2, 89,
	90, 7, 105, 2, 2, 90, 91, 7, 117, 2, 2, 91, 92, 3, 2, 2, 2, 92, 93, 5,
	25, 13, 2, 93, 28, 3, 2, 2, 2, 94, 95, 7, 38, 2, 2, 95, 96, 7, 114, 2,
	2, 96, 97, 7, 116, 2, 2, 97, 98, 7, 107, 2, 2, 98, 99, 7, 112, 2, 2, 99,
	100, 7, 101, 2, 2, 100, 101, 7, 107, 2, 2, 101, 102, 7, 114, 2, 2, 102,
	103, 7, 99, 2, 2, 103, 104, 7, 110, 2, 2, 104, 105, 7, 86, 2, 2, 105, 106,
	7, 99, 2, 2, 106, 107, 7, 105, 2, 2, 107, 108, 7, 117, 2, 2, 108, 109,
	3, 2, 2, 2, 109, 110, 5, 25, 13, 2, 110, 30, 3, 2, 2, 2, 111, 112, 7, 38,
	2, 2, 112, 113, 7, 116, 2, 2, 113, 114, 7, 103, 2, 2, 114, 115, 7, 115,
	2, 2, 115, 116, 7, 119, 2, 2, 116, 117, 7, 103, 2, 2, 117, 118, 7, 117,
	2, 2, 118, 119, 7, 118, 2, 2, 119, 120, 3, 2, 2, 2, 120, 121, 5, 25, 13,
	2, 121, 32, 3, 2, 2, 2, 122, 124, 9, 4, 2, 2, 123, 122, 3, 2, 2, 2, 124,
	125, 3, 2, 2, 2, 125, 123, 3, 2, 2, 2, 125, 126, 3, 2, 2, 2, 126, 127,
	3, 2, 2, 2, 127, 128, 8, 17, 2, 2, 128, 34, 3, 2, 2, 2, 5, 2, 68, 125,
	3, 8, 2, 2,
}

var lexerDeserializer = antlr.NewATNDeserializer(nil)
var lexerAtn = lexerDeserializer.DeserializeFromUInt16(serializedLexerAtn)

var lexerChannelNames = []string{
	"DEFAULT_TOKEN_CHANNEL", "HIDDEN",
}

var lexerModeNames = []string{
	"DEFAULT_MODE",
}

var lexerLiteralNames = []string{
	"", "','", "'AND'", "'OR'", "'IN'", "'true'", "'false'", "'='", "'('",
	"')'",
}

var lexerSymbolicNames = []string{
	"", "", "AND", "OR", "IN", "TRUE", "FALSE", "EQ", "LPAREN", "RPAREN", "IDENTIFIER",
	"STRING", "TAG_KEY", "RESOURCETAGS", "PRINCIPALTAGS", "REQUEST", "WS",
}

var lexerRuleNames = []string{
	"T__0", "AND", "OR", "IN", "TRUE", "FALSE", "EQ", "LPAREN", "RPAREN", "IDENTIFIER",
	"STRING", "TAG_KEY", "RESOURCETAGS", "PRINCIPALTAGS", "REQUEST", "WS",
}

type WhereConditionLexer struct {
	*antlr.BaseLexer
	channelNames []string
	modeNames    []string
	// TODO: EOF string
}

var lexerDecisionToDFA = make([]*antlr.DFA, len(lexerAtn.DecisionToState))

func init() {
	for index, ds := range lexerAtn.DecisionToState {
		lexerDecisionToDFA[index] = antlr.NewDFA(ds, index)
	}
}

func NewWhereConditionLexer(input antlr.CharStream) *WhereConditionLexer {

	l := new(WhereConditionLexer)

	l.BaseLexer = antlr.NewBaseLexer(input)
	l.Interpreter = antlr.NewLexerATNSimulator(l, lexerAtn, lexerDecisionToDFA, antlr.NewPredictionContextCache())

	l.channelNames = lexerChannelNames
	l.modeNames = lexerModeNames
	l.RuleNames = lexerRuleNames
	l.LiteralNames = lexerLiteralNames
	l.SymbolicNames = lexerSymbolicNames
	l.GrammarFileName = "WhereCondition.g4"
	// TODO: l.EOF = antlr.TokenEOF

	return l
}

// WhereConditionLexer tokens.
const (
	WhereConditionLexerT__0          = 1
	WhereConditionLexerAND           = 2
	WhereConditionLexerOR            = 3
	WhereConditionLexerIN            = 4
	WhereConditionLexerTRUE          = 5
	WhereConditionLexerFALSE         = 6
	WhereConditionLexerEQ            = 7
	WhereConditionLexerLPAREN        = 8
	WhereConditionLexerRPAREN        = 9
	WhereConditionLexerIDENTIFIER    = 10
	WhereConditionLexerSTRING        = 11
	WhereConditionLexerTAG_KEY       = 12
	WhereConditionLexerRESOURCETAGS  = 13
	WhereConditionLexerPRINCIPALTAGS = 14
	WhereConditionLexerREQUEST       = 15
	WhereConditionLexerWS            = 16
)
