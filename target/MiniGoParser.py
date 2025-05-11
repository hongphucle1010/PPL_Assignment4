# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u0235\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\5\2\u0084\n")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u008c\n\3\3\4\3\4\3\4\3")
        buf.write("\4\5\4\u0092\n\4\3\4\3\4\3\4\3\4\5\4\u0098\n\4\3\4\5\4")
        buf.write("\u009b\n\4\5\4\u009d\n\4\3\5\3\5\3\5\3\5\3\5\5\5\u00a4")
        buf.write("\n\5\3\5\3\5\3\5\3\5\5\5\u00aa\n\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\5\7\u00b5\n\7\3\7\3\7\5\7\u00b9\n\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\5\b\u00c0\n\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\5\n\u00c8\n\n\3\13\3\13\3\13\3\13\3\13\5\13\u00cf\n")
        buf.write("\13\3\13\3\13\5\13\u00d3\n\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\5\16")
        buf.write("\u00e6\n\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\5\21\u00f5\n\21\3\22\3\22\3\22")
        buf.write("\5\22\u00fa\n\22\3\22\3\22\5\22\u00fe\n\22\3\23\3\23\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\24\5\24\u0108\n\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0114\n")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0127\n\27\f")
        buf.write("\27\16\27\u012a\13\27\3\30\3\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u0135\n\31\3\31\5\31\u0138\n\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0141\n\32\3\33\3")
        buf.write("\33\3\33\5\33\u0146\n\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\5\35\u014f\n\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u015e\n\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\5\37\u0168\n\37\3")
        buf.write("\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3\"\3\"\3#\3#\5#\u0177")
        buf.write("\n#\3$\3$\5$\u017b\n$\3%\3%\3&\3&\5&\u0181\n&\3\'\3\'")
        buf.write("\5\'\u0185\n\'\3(\3(\5(\u0189\n(\3)\3)\3)\3)\3)\3)\3)")
        buf.write("\5)\u0192\n)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\5,\u01a0")
        buf.write("\n,\3-\3-\5-\u01a4\n-\3.\3.\3.\5.\u01a9\n.\3/\3/\3/\5")
        buf.write("/\u01ae\n/\3\60\3\60\3\60\5\60\u01b3\n\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\5\61\u01ba\n\61\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\5\63\u01c5\n\63\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\7\64\u01cd\n\64\f\64\16\64\u01d0\13\64\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\7\65\u01d8\n\65\f\65\16\65")
        buf.write("\u01db\13\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\7\66\u01e4")
        buf.write("\n\66\f\66\16\66\u01e7\13\66\3\67\3\67\38\38\38\38\38")
        buf.write("\38\38\78\u01f2\n8\f8\168\u01f5\138\39\39\3:\3:\3:\3:")
        buf.write("\3:\3:\3:\7:\u0200\n:\f:\16:\u0203\13:\3;\3;\3<\3<\3<")
        buf.write("\5<\u020a\n<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\5=\u0218")
        buf.write("\n=\7=\u021a\n=\f=\16=\u021d\13=\3>\3>\3>\3>\3>\3>\3>")
        buf.write("\5>\u0226\n>\3?\3?\3?\5?\u022b\n?\3?\3?\3@\3@\3@\3@\3")
        buf.write("A\3A\3A\2\t,fhjnrxB\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("prtvxz|~\u0080\2\t\4\2\"\"$(\4\2\13\r\25\25\3\2\34!\3")
        buf.write("\2\27\30\3\2\31\33\4\2\30\30++\3\2\669\2\u023c\2\u0083")
        buf.write("\3\2\2\2\4\u008b\3\2\2\2\6\u009c\3\2\2\2\b\u00a9\3\2\2")
        buf.write("\2\n\u00ab\3\2\2\2\f\u00b0\3\2\2\2\16\u00bc\3\2\2\2\20")
        buf.write("\u00c1\3\2\2\2\22\u00c4\3\2\2\2\24\u00c9\3\2\2\2\26\u00d6")
        buf.write("\3\2\2\2\30\u00db\3\2\2\2\32\u00e2\3\2\2\2\34\u00e7\3")
        buf.write("\2\2\2\36\u00ea\3\2\2\2 \u00f1\3\2\2\2\"\u00f6\3\2\2\2")
        buf.write("$\u00ff\3\2\2\2&\u0107\3\2\2\2(\u0113\3\2\2\2*\u0117\3")
        buf.write("\2\2\2,\u011b\3\2\2\2.\u012b\3\2\2\2\60\u0137\3\2\2\2")
        buf.write("\62\u0139\3\2\2\2\64\u0145\3\2\2\2\66\u0147\3\2\2\28\u014b")
        buf.write("\3\2\2\2:\u0156\3\2\2\2<\u0164\3\2\2\2>\u016c\3\2\2\2")
        buf.write("@\u0170\3\2\2\2B\u0172\3\2\2\2D\u0176\3\2\2\2F\u0178\3")
        buf.write("\2\2\2H\u017c\3\2\2\2J\u0180\3\2\2\2L\u0184\3\2\2\2N\u0188")
        buf.write("\3\2\2\2P\u0191\3\2\2\2R\u0193\3\2\2\2T\u0196\3\2\2\2")
        buf.write("V\u019a\3\2\2\2X\u01a3\3\2\2\2Z\u01a5\3\2\2\2\\\u01ad")
        buf.write("\3\2\2\2^\u01af\3\2\2\2`\u01b6\3\2\2\2b\u01bb\3\2\2\2")
        buf.write("d\u01c4\3\2\2\2f\u01c6\3\2\2\2h\u01d1\3\2\2\2j\u01dc\3")
        buf.write("\2\2\2l\u01e8\3\2\2\2n\u01ea\3\2\2\2p\u01f6\3\2\2\2r\u01f8")
        buf.write("\3\2\2\2t\u0204\3\2\2\2v\u0209\3\2\2\2x\u020b\3\2\2\2")
        buf.write("z\u0225\3\2\2\2|\u0227\3\2\2\2~\u022e\3\2\2\2\u0080\u0232")
        buf.write("\3\2\2\2\u0082\u0084\5\4\3\2\u0083\u0082\3\2\2\2\u0083")
        buf.write("\u0084\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\7\2\2\3")
        buf.write("\u0086\3\3\2\2\2\u0087\u0088\5\6\4\2\u0088\u0089\5\4\3")
        buf.write("\2\u0089\u008c\3\2\2\2\u008a\u008c\5\6\4\2\u008b\u0087")
        buf.write("\3\2\2\2\u008b\u008a\3\2\2\2\u008c\5\3\2\2\2\u008d\u0092")
        buf.write("\5\b\5\2\u008e\u0092\5\n\6\2\u008f\u0092\5\30\r\2\u0090")
        buf.write("\u0092\5\36\20\2\u0091\u008d\3\2\2\2\u0091\u008e\3\2\2")
        buf.write("\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u0094\7\64\2\2\u0094\u009d\3\2\2\2\u0095")
        buf.write("\u0098\5\f\7\2\u0096\u0098\5\24\13\2\u0097\u0095\3\2\2")
        buf.write("\2\u0097\u0096\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u009b")
        buf.write("\7\64\2\2\u009a\u0099\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u009d\3\2\2\2\u009c\u0091\3\2\2\2\u009c\u0097\3\2\2\2")
        buf.write("\u009d\7\3\2\2\2\u009e\u009f\7\16\2\2\u009f\u00a0\7=\2")
        buf.write("\2\u00a0\u00a3\5L\'\2\u00a1\u00a2\7#\2\2\u00a2\u00a4\5")
        buf.write("f\64\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00aa")
        buf.write("\3\2\2\2\u00a5\u00a6\7\16\2\2\u00a6\u00a7\7=\2\2\u00a7")
        buf.write("\u00a8\7#\2\2\u00a8\u00aa\5f\64\2\u00a9\u009e\3\2\2\2")
        buf.write("\u00a9\u00a5\3\2\2\2\u00aa\t\3\2\2\2\u00ab\u00ac\7\26")
        buf.write("\2\2\u00ac\u00ad\7=\2\2\u00ad\u00ae\7#\2\2\u00ae\u00af")
        buf.write("\5f\64\2\u00af\13\3\2\2\2\u00b0\u00b1\7\7\2\2\u00b1\u00b2")
        buf.write("\7=\2\2\u00b2\u00b4\7-\2\2\u00b3\u00b5\5\16\b\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\u00b8\7.\2\2\u00b7\u00b9\5L\'\2\u00b8\u00b7\3\2")
        buf.write("\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb")
        buf.write("\5$\23\2\u00bb\r\3\2\2\2\u00bc\u00bf\5\20\t\2\u00bd\u00be")
        buf.write("\7\63\2\2\u00be\u00c0\5\16\b\2\u00bf\u00bd\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\17\3\2\2\2\u00c1\u00c2\5\22\n\2\u00c2")
        buf.write("\u00c3\5L\'\2\u00c3\21\3\2\2\2\u00c4\u00c7\7=\2\2\u00c5")
        buf.write("\u00c6\7\63\2\2\u00c6\u00c8\5\22\n\2\u00c7\u00c5\3\2\2")
        buf.write("\2\u00c7\u00c8\3\2\2\2\u00c8\23\3\2\2\2\u00c9\u00ca\7")
        buf.write("\7\2\2\u00ca\u00cb\5\26\f\2\u00cb\u00cc\7=\2\2\u00cc\u00ce")
        buf.write("\7-\2\2\u00cd\u00cf\5\16\b\2\u00ce\u00cd\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d2\7.\2\2")
        buf.write("\u00d1\u00d3\5L\'\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3\3")
        buf.write("\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\5$\23\2\u00d5\25")
        buf.write("\3\2\2\2\u00d6\u00d7\7-\2\2\u00d7\u00d8\7=\2\2\u00d8\u00d9")
        buf.write("\7=\2\2\u00d9\u00da\7.\2\2\u00da\27\3\2\2\2\u00db\u00dc")
        buf.write("\7\b\2\2\u00dc\u00dd\7=\2\2\u00dd\u00de\7\t\2\2\u00de")
        buf.write("\u00df\7/\2\2\u00df\u00e0\5\32\16\2\u00e0\u00e1\7\60\2")
        buf.write("\2\u00e1\31\3\2\2\2\u00e2\u00e3\5\34\17\2\u00e3\u00e5")
        buf.write("\7\64\2\2\u00e4\u00e6\5\32\16\2\u00e5\u00e4\3\2\2\2\u00e5")
        buf.write("\u00e6\3\2\2\2\u00e6\33\3\2\2\2\u00e7\u00e8\7=\2\2\u00e8")
        buf.write("\u00e9\5L\'\2\u00e9\35\3\2\2\2\u00ea\u00eb\7\b\2\2\u00eb")
        buf.write("\u00ec\7=\2\2\u00ec\u00ed\7\n\2\2\u00ed\u00ee\7/\2\2\u00ee")
        buf.write("\u00ef\5 \21\2\u00ef\u00f0\7\60\2\2\u00f0\37\3\2\2\2\u00f1")
        buf.write("\u00f2\5\"\22\2\u00f2\u00f4\7\64\2\2\u00f3\u00f5\5 \21")
        buf.write("\2\u00f4\u00f3\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5!\3\2")
        buf.write("\2\2\u00f6\u00f7\7=\2\2\u00f7\u00f9\7-\2\2\u00f8\u00fa")
        buf.write("\5\16\b\2\u00f9\u00f8\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa")
        buf.write("\u00fb\3\2\2\2\u00fb\u00fd\7.\2\2\u00fc\u00fe\5L\'\2\u00fd")
        buf.write("\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe#\3\2\2\2\u00ff")
        buf.write("\u0100\7/\2\2\u0100\u0101\5&\24\2\u0101\u0102\7\60\2\2")
        buf.write("\u0102%\3\2\2\2\u0103\u0104\5(\25\2\u0104\u0105\5&\24")
        buf.write("\2\u0105\u0108\3\2\2\2\u0106\u0108\5(\25\2\u0107\u0103")
        buf.write("\3\2\2\2\u0107\u0106\3\2\2\2\u0108\'\3\2\2\2\u0109\u0114")
        buf.write("\3\2\2\2\u010a\u0114\5*\26\2\u010b\u0114\5@!\2\u010c\u0114")
        buf.write("\5B\"\2\u010d\u0114\5D#\2\u010e\u0114\5F$\2\u010f\u0114")
        buf.write("\5\b\5\2\u0110\u0114\5\n\6\2\u0111\u0114\5\60\31\2\u0112")
        buf.write("\u0114\5\64\33\2\u0113\u0109\3\2\2\2\u0113\u010a\3\2\2")
        buf.write("\2\u0113\u010b\3\2\2\2\u0113\u010c\3\2\2\2\u0113\u010d")
        buf.write("\3\2\2\2\u0113\u010e\3\2\2\2\u0113\u010f\3\2\2\2\u0113")
        buf.write("\u0110\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2")
        buf.write("\u0114\u0115\3\2\2\2\u0115\u0116\7\64\2\2\u0116)\3\2\2")
        buf.write("\2\u0117\u0118\5,\27\2\u0118\u0119\5.\30\2\u0119\u011a")
        buf.write("\5f\64\2\u011a+\3\2\2\2\u011b\u011c\b\27\1\2\u011c\u011d")
        buf.write("\7=\2\2\u011d\u0128\3\2\2\2\u011e\u011f\f\4\2\2\u011f")
        buf.write("\u0120\7\61\2\2\u0120\u0121\5f\64\2\u0121\u0122\7\62\2")
        buf.write("\2\u0122\u0127\3\2\2\2\u0123\u0124\f\3\2\2\u0124\u0125")
        buf.write("\7,\2\2\u0125\u0127\7=\2\2\u0126\u011e\3\2\2\2\u0126\u0123")
        buf.write("\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129-\3\2\2\2\u012a\u0128\3\2\2\2\u012b")
        buf.write("\u012c\t\2\2\2\u012c/\3\2\2\2\u012d\u012e\7\3\2\2\u012e")
        buf.write("\u012f\7-\2\2\u012f\u0130\5f\64\2\u0130\u0131\7.\2\2\u0131")
        buf.write("\u0134\5$\23\2\u0132\u0133\7\4\2\2\u0133\u0135\5\60\31")
        buf.write("\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0138")
        buf.write("\3\2\2\2\u0136\u0138\5\62\32\2\u0137\u012d\3\2\2\2\u0137")
        buf.write("\u0136\3\2\2\2\u0138\61\3\2\2\2\u0139\u013a\7\3\2\2\u013a")
        buf.write("\u013b\7-\2\2\u013b\u013c\5f\64\2\u013c\u013d\7.\2\2\u013d")
        buf.write("\u0140\5$\23\2\u013e\u013f\7\4\2\2\u013f\u0141\5$\23\2")
        buf.write("\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\63\3\2")
        buf.write("\2\2\u0142\u0146\5\66\34\2\u0143\u0146\58\35\2\u0144\u0146")
        buf.write("\5:\36\2\u0145\u0142\3\2\2\2\u0145\u0143\3\2\2\2\u0145")
        buf.write("\u0144\3\2\2\2\u0146\65\3\2\2\2\u0147\u0148\7\5\2\2\u0148")
        buf.write("\u0149\5f\64\2\u0149\u014a\5$\23\2\u014a\67\3\2\2\2\u014b")
        buf.write("\u014e\7\5\2\2\u014c\u014f\5<\37\2\u014d\u014f\5> \2\u014e")
        buf.write("\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u0150\u0151\7\64\2\2\u0151\u0152\5f\64\2\u0152\u0153")
        buf.write("\7\64\2\2\u0153\u0154\5> \2\u0154\u0155\5$\23\2\u0155")
        buf.write("9\3\2\2\2\u0156\u015d\7\5\2\2\u0157\u0158\7=\2\2\u0158")
        buf.write("\u0159\7\63\2\2\u0159\u015e\7=\2\2\u015a\u015b\7<\2\2")
        buf.write("\u015b\u015c\7\63\2\2\u015c\u015e\7=\2\2\u015d\u0157\3")
        buf.write("\2\2\2\u015d\u015a\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160")
        buf.write("\7\"\2\2\u0160\u0161\7\21\2\2\u0161\u0162\5f\64\2\u0162")
        buf.write("\u0163\5$\23\2\u0163;\3\2\2\2\u0164\u0165\7\16\2\2\u0165")
        buf.write("\u0167\7=\2\2\u0166\u0168\5L\'\2\u0167\u0166\3\2\2\2\u0167")
        buf.write("\u0168\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\7#\2\2")
        buf.write("\u016a\u016b\5f\64\2\u016b=\3\2\2\2\u016c\u016d\7=\2\2")
        buf.write("\u016d\u016e\5.\30\2\u016e\u016f\5f\64\2\u016f?\3\2\2")
        buf.write("\2\u0170\u0171\7\20\2\2\u0171A\3\2\2\2\u0172\u0173\7\17")
        buf.write("\2\2\u0173C\3\2\2\2\u0174\u0177\5|?\2\u0175\u0177\5~@")
        buf.write("\2\u0176\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177E\3\2")
        buf.write("\2\2\u0178\u017a\7\6\2\2\u0179\u017b\5f\64\2\u017a\u0179")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017bG\3\2\2\2\u017c\u017d")
        buf.write("\t\3\2\2\u017dI\3\2\2\2\u017e\u0181\5H%\2\u017f\u0181")
        buf.write("\7=\2\2\u0180\u017e\3\2\2\2\u0180\u017f\3\2\2\2\u0181")
        buf.write("K\3\2\2\2\u0182\u0185\5V,\2\u0183\u0185\5J&\2\u0184\u0182")
        buf.write("\3\2\2\2\u0184\u0183\3\2\2\2\u0185M\3\2\2\2\u0186\u0189")
        buf.write("\5P)\2\u0187\u0189\5R*\2\u0188\u0186\3\2\2\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189O\3\2\2\2\u018a\u0192\5\u0080A\2\u018b\u0192")
        buf.write("\7:\2\2\u018c\u0192\7;\2\2\u018d\u0192\7\23\2\2\u018e")
        buf.write("\u0192\7\24\2\2\u018f\u0192\7\22\2\2\u0190\u0192\5^\60")
        buf.write("\2\u0191\u018a\3\2\2\2\u0191\u018b\3\2\2\2\u0191\u018c")
        buf.write("\3\2\2\2\u0191\u018d\3\2\2\2\u0191\u018e\3\2\2\2\u0191")
        buf.write("\u018f\3\2\2\2\u0191\u0190\3\2\2\2\u0192Q\3\2\2\2\u0193")
        buf.write("\u0194\5V,\2\u0194\u0195\5T+\2\u0195S\3\2\2\2\u0196\u0197")
        buf.write("\7/\2\2\u0197\u0198\5Z.\2\u0198\u0199\7\60\2\2\u0199U")
        buf.write("\3\2\2\2\u019a\u019b\7\61\2\2\u019b\u019c\5X-\2\u019c")
        buf.write("\u019f\7\62\2\2\u019d\u01a0\5V,\2\u019e\u01a0\5J&\2\u019f")
        buf.write("\u019d\3\2\2\2\u019f\u019e\3\2\2\2\u01a0W\3\2\2\2\u01a1")
        buf.write("\u01a4\5\u0080A\2\u01a2\u01a4\7=\2\2\u01a3\u01a1\3\2\2")
        buf.write("\2\u01a3\u01a2\3\2\2\2\u01a4Y\3\2\2\2\u01a5\u01a8\5\\")
        buf.write("/\2\u01a6\u01a7\7\63\2\2\u01a7\u01a9\5Z.\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9[\3\2\2\2\u01aa\u01ae")
        buf.write("\5P)\2\u01ab\u01ae\7=\2\2\u01ac\u01ae\5T+\2\u01ad\u01aa")
        buf.write("\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ae")
        buf.write("]\3\2\2\2\u01af\u01b0\7=\2\2\u01b0\u01b2\7/\2\2\u01b1")
        buf.write("\u01b3\5`\61\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2")
        buf.write("\u01b3\u01b4\3\2\2\2\u01b4\u01b5\7\60\2\2\u01b5_\3\2\2")
        buf.write("\2\u01b6\u01b9\5b\62\2\u01b7\u01b8\7\63\2\2\u01b8\u01ba")
        buf.write("\5`\61\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba")
        buf.write("a\3\2\2\2\u01bb\u01bc\7=\2\2\u01bc\u01bd\7\65\2\2\u01bd")
        buf.write("\u01be\5f\64\2\u01bec\3\2\2\2\u01bf\u01c0\5f\64\2\u01c0")
        buf.write("\u01c1\7\63\2\2\u01c1\u01c2\5d\63\2\u01c2\u01c5\3\2\2")
        buf.write("\2\u01c3\u01c5\5f\64\2\u01c4\u01bf\3\2\2\2\u01c4\u01c3")
        buf.write("\3\2\2\2\u01c5e\3\2\2\2\u01c6\u01c7\b\64\1\2\u01c7\u01c8")
        buf.write("\5h\65\2\u01c8\u01ce\3\2\2\2\u01c9\u01ca\f\4\2\2\u01ca")
        buf.write("\u01cb\7*\2\2\u01cb\u01cd\5h\65\2\u01cc\u01c9\3\2\2\2")
        buf.write("\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3")
        buf.write("\2\2\2\u01cfg\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d2")
        buf.write("\b\65\1\2\u01d2\u01d3\5j\66\2\u01d3\u01d9\3\2\2\2\u01d4")
        buf.write("\u01d5\f\4\2\2\u01d5\u01d6\7)\2\2\u01d6\u01d8\5j\66\2")
        buf.write("\u01d7\u01d4\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3")
        buf.write("\2\2\2\u01d9\u01da\3\2\2\2\u01dai\3\2\2\2\u01db\u01d9")
        buf.write("\3\2\2\2\u01dc\u01dd\b\66\1\2\u01dd\u01de\5n8\2\u01de")
        buf.write("\u01e5\3\2\2\2\u01df\u01e0\f\4\2\2\u01e0\u01e1\5l\67\2")
        buf.write("\u01e1\u01e2\5n8\2\u01e2\u01e4\3\2\2\2\u01e3\u01df\3\2")
        buf.write("\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6")
        buf.write("\3\2\2\2\u01e6k\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01e9")
        buf.write("\t\4\2\2\u01e9m\3\2\2\2\u01ea\u01eb\b8\1\2\u01eb\u01ec")
        buf.write("\5r:\2\u01ec\u01f3\3\2\2\2\u01ed\u01ee\f\4\2\2\u01ee\u01ef")
        buf.write("\5p9\2\u01ef\u01f0\5r:\2\u01f0\u01f2\3\2\2\2\u01f1\u01ed")
        buf.write("\3\2\2\2\u01f2\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3")
        buf.write("\u01f4\3\2\2\2\u01f4o\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f6")
        buf.write("\u01f7\t\5\2\2\u01f7q\3\2\2\2\u01f8\u01f9\b:\1\2\u01f9")
        buf.write("\u01fa\5v<\2\u01fa\u0201\3\2\2\2\u01fb\u01fc\f\4\2\2\u01fc")
        buf.write("\u01fd\5t;\2\u01fd\u01fe\5v<\2\u01fe\u0200\3\2\2\2\u01ff")
        buf.write("\u01fb\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2")
        buf.write("\u0201\u0202\3\2\2\2\u0202s\3\2\2\2\u0203\u0201\3\2\2")
        buf.write("\2\u0204\u0205\t\6\2\2\u0205u\3\2\2\2\u0206\u0207\t\7")
        buf.write("\2\2\u0207\u020a\5v<\2\u0208\u020a\5x=\2\u0209\u0206\3")
        buf.write("\2\2\2\u0209\u0208\3\2\2\2\u020aw\3\2\2\2\u020b\u020c")
        buf.write("\b=\1\2\u020c\u020d\5z>\2\u020d\u021b\3\2\2\2\u020e\u020f")
        buf.write("\f\5\2\2\u020f\u0210\7\61\2\2\u0210\u0211\5f\64\2\u0211")
        buf.write("\u0212\7\62\2\2\u0212\u021a\3\2\2\2\u0213\u0214\f\4\2")
        buf.write("\2\u0214\u0217\7,\2\2\u0215\u0218\7=\2\2\u0216\u0218\5")
        buf.write("|?\2\u0217\u0215\3\2\2\2\u0217\u0216\3\2\2\2\u0218\u021a")
        buf.write("\3\2\2\2\u0219\u020e\3\2\2\2\u0219\u0213\3\2\2\2\u021a")
        buf.write("\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2")
        buf.write("\u021cy\3\2\2\2\u021d\u021b\3\2\2\2\u021e\u0226\5N(\2")
        buf.write("\u021f\u0226\7=\2\2\u0220\u0221\7-\2\2\u0221\u0222\5f")
        buf.write("\64\2\u0222\u0223\7.\2\2\u0223\u0226\3\2\2\2\u0224\u0226")
        buf.write("\5|?\2\u0225\u021e\3\2\2\2\u0225\u021f\3\2\2\2\u0225\u0220")
        buf.write("\3\2\2\2\u0225\u0224\3\2\2\2\u0226{\3\2\2\2\u0227\u0228")
        buf.write("\7=\2\2\u0228\u022a\7-\2\2\u0229\u022b\5d\63\2\u022a\u0229")
        buf.write("\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022c\3\2\2\2\u022c")
        buf.write("\u022d\7.\2\2\u022d}\3\2\2\2\u022e\u022f\5x=\2\u022f\u0230")
        buf.write("\7,\2\2\u0230\u0231\5|?\2\u0231\177\3\2\2\2\u0232\u0233")
        buf.write("\t\b\2\2\u0233\u0081\3\2\2\2\67\u0083\u008b\u0091\u0097")
        buf.write("\u009a\u009c\u00a3\u00a9\u00b4\u00b8\u00bf\u00c7\u00ce")
        buf.write("\u00d2\u00e5\u00f4\u00f9\u00fd\u0107\u0113\u0126\u0128")
        buf.write("\u0134\u0137\u0140\u0145\u014e\u015d\u0167\u0176\u017a")
        buf.write("\u0180\u0184\u0188\u0191\u019f\u01a3\u01a8\u01ad\u01b2")
        buf.write("\u01b9\u01c4\u01ce\u01d9\u01e5\u01f3\u0201\u0209\u0217")
        buf.write("\u0219\u021b\u0225\u022a")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'var'", "'continue'", "'break'", 
                     "'range'", "'nil'", "'true'", "'false'", "'boolean'", 
                     "'const'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "':='", "'='", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'&&'", "'||'", 
                     "'!'", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'", "':'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'_'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                      "FALSE", "BOOLEAN", "CONST", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "EQUAL", "NOTEQUAL", "LESS", "LESSEQUAL", 
                      "GREATER", "GREATEREQUAL", "DECLARE", "ASSIGN", "ADD_ASSIGN", 
                      "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "AND", "OR", "NOT", "DOT", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMI", "COLON", 
                      "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", 
                      "STR_LIT", "UNDERSCORE", "ID", "NEWLINE", "WS", "COMMENT", 
                      "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_many_declarations = 1
    RULE_declaration = 2
    RULE_varDeclaration = 3
    RULE_constDeclaration = 4
    RULE_funcDeclaration = 5
    RULE_paramList = 6
    RULE_param = 7
    RULE_multiID = 8
    RULE_methodDeclaration = 9
    RULE_methodReceiver = 10
    RULE_structDeclaration = 11
    RULE_structFields = 12
    RULE_field = 13
    RULE_interfaceDeclaration = 14
    RULE_methodSignatures = 15
    RULE_methodSignature = 16
    RULE_block = 17
    RULE_stmtList = 18
    RULE_statement = 19
    RULE_assignStmt = 20
    RULE_lhs = 21
    RULE_assignmentOp = 22
    RULE_ifStmt = 23
    RULE_ifElseStmt = 24
    RULE_forStmt = 25
    RULE_forExpr = 26
    RULE_forLoop = 27
    RULE_forRange = 28
    RULE_scalarDecl = 29
    RULE_scalarAssign = 30
    RULE_breakStmt = 31
    RULE_continueStmt = 32
    RULE_callStmt = 33
    RULE_returnStmt = 34
    RULE_primitiveType = 35
    RULE_baseType = 36
    RULE_typeSpec = 37
    RULE_literal = 38
    RULE_notArrayLiteral = 39
    RULE_arrayLiteral = 40
    RULE_arrayBody = 41
    RULE_arrayType = 42
    RULE_arrayDim = 43
    RULE_arrayList = 44
    RULE_arrayMember = 45
    RULE_structLiteral = 46
    RULE_structElements = 47
    RULE_structElement = 48
    RULE_exprList = 49
    RULE_expression = 50
    RULE_expr1 = 51
    RULE_expr2 = 52
    RULE_compOp = 53
    RULE_expr3 = 54
    RULE_addOp = 55
    RULE_expr4 = 56
    RULE_mulOp = 57
    RULE_expr5 = 58
    RULE_expr6 = 59
    RULE_expr7 = 60
    RULE_funcCall = 61
    RULE_methodCall = 62
    RULE_integer = 63

    ruleNames =  [ "program", "many_declarations", "declaration", "varDeclaration", 
                   "constDeclaration", "funcDeclaration", "paramList", "param", 
                   "multiID", "methodDeclaration", "methodReceiver", "structDeclaration", 
                   "structFields", "field", "interfaceDeclaration", "methodSignatures", 
                   "methodSignature", "block", "stmtList", "statement", 
                   "assignStmt", "lhs", "assignmentOp", "ifStmt", "ifElseStmt", 
                   "forStmt", "forExpr", "forLoop", "forRange", "scalarDecl", 
                   "scalarAssign", "breakStmt", "continueStmt", "callStmt", 
                   "returnStmt", "primitiveType", "baseType", "typeSpec", 
                   "literal", "notArrayLiteral", "arrayLiteral", "arrayBody", 
                   "arrayType", "arrayDim", "arrayList", "arrayMember", 
                   "structLiteral", "structElements", "structElement", "exprList", 
                   "expression", "expr1", "expr2", "compOp", "expr3", "addOp", 
                   "expr4", "mulOp", "expr5", "expr6", "expr7", "funcCall", 
                   "methodCall", "integer" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    VAR=12
    CONTINUE=13
    BREAK=14
    RANGE=15
    NIL=16
    TRUE=17
    FALSE=18
    BOOLEAN=19
    CONST=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQUAL=26
    NOTEQUAL=27
    LESS=28
    LESSEQUAL=29
    GREATER=30
    GREATEREQUAL=31
    DECLARE=32
    ASSIGN=33
    ADD_ASSIGN=34
    SUB_ASSIGN=35
    MUL_ASSIGN=36
    DIV_ASSIGN=37
    MOD_ASSIGN=38
    AND=39
    OR=40
    NOT=41
    DOT=42
    LPAREN=43
    RPAREN=44
    LBRACE=45
    RBRACE=46
    LBRACK=47
    RBRACK=48
    COMMA=49
    SEMI=50
    COLON=51
    DEC_LIT=52
    BIN_LIT=53
    OCT_LIT=54
    HEX_LIT=55
    FLOAT_LIT=56
    STR_LIT=57
    UNDERSCORE=58
    ID=59
    NEWLINE=60
    WS=61
    COMMENT=62
    BLOCK_COMMENT=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    ERROR_CHAR=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def many_declarations(self):
            return self.getTypedRuleContext(MiniGoParser.Many_declarationsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONST))) != 0):
                self.state = 128
                self.many_declarations()


            self.state = 131
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_declarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationContext,0)


        def many_declarations(self):
            return self.getTypedRuleContext(MiniGoParser.Many_declarationsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_many_declarations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_declarations" ):
                return visitor.visitMany_declarations(self)
            else:
                return visitor.visitChildren(self)




    def many_declarations(self):

        localctx = MiniGoParser.Many_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_many_declarations)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.declaration()
                self.state = 134
                self.many_declarations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def varDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclarationContext,0)


        def constDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclarationContext,0)


        def structDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.StructDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDeclarationContext,0)


        def funcDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.FuncDeclarationContext,0)


        def methodDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniGoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TYPE, MiniGoParser.VAR, MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 139
                    self.varDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 140
                    self.constDeclaration()
                    pass

                elif la_ == 3:
                    self.state = 141
                    self.structDeclaration()
                    pass

                elif la_ == 4:
                    self.state = 142
                    self.interfaceDeclaration()
                    pass


                self.state = 145
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 147
                    self.funcDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 148
                    self.methodDeclaration()
                    pass


                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SEMI:
                    self.state = 151
                    self.match(MiniGoParser.SEMI)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typeSpec(self):
            return self.getTypedRuleContext(MiniGoParser.TypeSpecContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = MiniGoParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(MiniGoParser.VAR)
                self.state = 157
                self.match(MiniGoParser.ID)
                self.state = 158
                self.typeSpec()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 159
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 160
                    self.expression(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(MiniGoParser.VAR)
                self.state = 164
                self.match(MiniGoParser.ID)
                self.state = 165
                self.match(MiniGoParser.ASSIGN)
                self.state = 166
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDeclaration" ):
                return visitor.visitConstDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def constDeclaration(self):

        localctx = MiniGoParser.ConstDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(MiniGoParser.CONST)
            self.state = 170
            self.match(MiniGoParser.ID)
            self.state = 171
            self.match(MiniGoParser.ASSIGN)
            self.state = 172
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def typeSpec(self):
            return self.getTypedRuleContext(MiniGoParser.TypeSpecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDeclaration" ):
                return visitor.visitFuncDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def funcDeclaration(self):

        localctx = MiniGoParser.FuncDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MiniGoParser.FUNC)
            self.state = 175
            self.match(MiniGoParser.ID)
            self.state = 176
            self.match(MiniGoParser.LPAREN)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 177
                self.paramList()


            self.state = 180
            self.match(MiniGoParser.RPAREN)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 181
                self.typeSpec()


            self.state = 184
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = MiniGoParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.param()
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 187
                self.match(MiniGoParser.COMMA)
                self.state = 188
                self.paramList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiID(self):
            return self.getTypedRuleContext(MiniGoParser.MultiIDContext,0)


        def typeSpec(self):
            return self.getTypedRuleContext(MiniGoParser.TypeSpecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.multiID()
            self.state = 192
            self.typeSpec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def multiID(self):
            return self.getTypedRuleContext(MiniGoParser.MultiIDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_multiID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiID" ):
                return visitor.visitMultiID(self)
            else:
                return visitor.visitChildren(self)




    def multiID(self):

        localctx = MiniGoParser.MultiIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_multiID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(MiniGoParser.ID)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 195
                self.match(MiniGoParser.COMMA)
                self.state = 196
                self.multiID()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def methodReceiver(self):
            return self.getTypedRuleContext(MiniGoParser.MethodReceiverContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def typeSpec(self):
            return self.getTypedRuleContext(MiniGoParser.TypeSpecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = MiniGoParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(MiniGoParser.FUNC)
            self.state = 200
            self.methodReceiver()
            self.state = 201
            self.match(MiniGoParser.ID)
            self.state = 202
            self.match(MiniGoParser.LPAREN)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 203
                self.paramList()


            self.state = 206
            self.match(MiniGoParser.RPAREN)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 207
                self.typeSpec()


            self.state = 210
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodReceiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodReceiver" ):
                return visitor.visitMethodReceiver(self)
            else:
                return visitor.visitChildren(self)




    def methodReceiver(self):

        localctx = MiniGoParser.MethodReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_methodReceiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MiniGoParser.LPAREN)
            self.state = 213
            self.match(MiniGoParser.ID)
            self.state = 214
            self.match(MiniGoParser.ID)
            self.state = 215
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def structFields(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDeclaration" ):
                return visitor.visitStructDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def structDeclaration(self):

        localctx = MiniGoParser.StructDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_structDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(MiniGoParser.TYPE)
            self.state = 218
            self.match(MiniGoParser.ID)
            self.state = 219
            self.match(MiniGoParser.STRUCT)
            self.state = 220
            self.match(MiniGoParser.LBRACE)
            self.state = 221
            self.structFields()
            self.state = 222
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def structFields(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structFields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFields" ):
                return visitor.visitStructFields(self)
            else:
                return visitor.visitChildren(self)




    def structFields(self):

        localctx = MiniGoParser.StructFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_structFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.field()
            self.state = 225
            self.match(MiniGoParser.SEMI)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 226
                self.structFields()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typeSpec(self):
            return self.getTypedRuleContext(MiniGoParser.TypeSpecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MiniGoParser.ID)
            self.state = 230
            self.typeSpec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def methodSignatures(self):
            return self.getTypedRuleContext(MiniGoParser.MethodSignaturesContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDeclaration" ):
                return visitor.visitInterfaceDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDeclaration(self):

        localctx = MiniGoParser.InterfaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_interfaceDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(MiniGoParser.TYPE)
            self.state = 233
            self.match(MiniGoParser.ID)
            self.state = 234
            self.match(MiniGoParser.INTERFACE)
            self.state = 235
            self.match(MiniGoParser.LBRACE)
            self.state = 236
            self.methodSignatures()
            self.state = 237
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodSignaturesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodSignature(self):
            return self.getTypedRuleContext(MiniGoParser.MethodSignatureContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def methodSignatures(self):
            return self.getTypedRuleContext(MiniGoParser.MethodSignaturesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodSignatures

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodSignatures" ):
                return visitor.visitMethodSignatures(self)
            else:
                return visitor.visitChildren(self)




    def methodSignatures(self):

        localctx = MiniGoParser.MethodSignaturesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_methodSignatures)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.methodSignature()
            self.state = 240
            self.match(MiniGoParser.SEMI)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 241
                self.methodSignatures()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodSignatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def typeSpec(self):
            return self.getTypedRuleContext(MiniGoParser.TypeSpecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodSignature

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodSignature" ):
                return visitor.visitMethodSignature(self)
            else:
                return visitor.visitChildren(self)




    def methodSignature(self):

        localctx = MiniGoParser.MethodSignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_methodSignature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(MiniGoParser.ID)
            self.state = 245
            self.match(MiniGoParser.LPAREN)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 246
                self.paramList()


            self.state = 249
            self.match(MiniGoParser.RPAREN)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 250
                self.typeSpec()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def stmtList(self):
            return self.getTypedRuleContext(MiniGoParser.StmtListContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(MiniGoParser.LBRACE)
            self.state = 254
            self.stmtList()
            self.state = 255
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def stmtList(self):
            return self.getTypedRuleContext(MiniGoParser.StmtListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmtList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtList" ):
                return visitor.visitStmtList(self)
            else:
                return visitor.visitChildren(self)




    def stmtList(self):

        localctx = MiniGoParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmtList)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.statement()
                self.state = 258
                self.stmtList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.statement()
                pass


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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def assignStmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(MiniGoParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ContinueStmtContext,0)


        def callStmt(self):
            return self.getTypedRuleContext(MiniGoParser.CallStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnStmtContext,0)


        def varDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclarationContext,0)


        def constDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclarationContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ForStmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 264
                self.assignStmt()
                pass

            elif la_ == 3:
                self.state = 265
                self.breakStmt()
                pass

            elif la_ == 4:
                self.state = 266
                self.continueStmt()
                pass

            elif la_ == 5:
                self.state = 267
                self.callStmt()
                pass

            elif la_ == 6:
                self.state = 268
                self.returnStmt()
                pass

            elif la_ == 7:
                self.state = 269
                self.varDeclaration()
                pass

            elif la_ == 8:
                self.state = 270
                self.constDeclaration()
                pass

            elif la_ == 9:
                self.state = 271
                self.ifStmt()
                pass

            elif la_ == 10:
                self.state = 272
                self.forStmt()
                pass


            self.state = 275
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assignmentOp(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentOpContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = MiniGoParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.lhs(0)
            self.state = 278
            self.assignmentOp()
            self.state = 279
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 292
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 284
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 285
                        self.match(MiniGoParser.LBRACK)
                        self.state = 286
                        self.expression(0)
                        self.state = 287
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 289
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 290
                        self.match(MiniGoParser.DOT)
                        self.state = 291
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignmentOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOp" ):
                return visitor.visitAssignmentOp(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOp(self):

        localctx = MiniGoParser.AssignmentOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignmentOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DECLARE) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def ifStmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfStmtContext,0)


        def ifElseStmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfElseStmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = MiniGoParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(MiniGoParser.IF)
                self.state = 300
                self.match(MiniGoParser.LPAREN)
                self.state = 301
                self.expression(0)
                self.state = 302
                self.match(MiniGoParser.RPAREN)
                self.state = 303
                self.block()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ELSE:
                    self.state = 304
                    self.match(MiniGoParser.ELSE)
                    self.state = 305
                    self.ifStmt()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.ifElseStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifElseStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseStmt" ):
                return visitor.visitIfElseStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifElseStmt(self):

        localctx = MiniGoParser.IfElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_ifElseStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(MiniGoParser.IF)
            self.state = 312
            self.match(MiniGoParser.LPAREN)
            self.state = 313
            self.expression(0)
            self.state = 314
            self.match(MiniGoParser.RPAREN)
            self.state = 315
            self.block()
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 316
                self.match(MiniGoParser.ELSE)
                self.state = 317
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forExpr(self):
            return self.getTypedRuleContext(MiniGoParser.ForExprContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(MiniGoParser.ForLoopContext,0)


        def forRange(self):
            return self.getTypedRuleContext(MiniGoParser.ForRangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = MiniGoParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forStmt)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.forExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.forLoop()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.forRange()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForExpr" ):
                return visitor.visitForExpr(self)
            else:
                return visitor.visitChildren(self)




    def forExpr(self):

        localctx = MiniGoParser.ForExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_forExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(MiniGoParser.FOR)
            self.state = 326
            self.expression(0)
            self.state = 327
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def scalarAssign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ScalarAssignContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ScalarAssignContext,i)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def scalarDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ScalarDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = MiniGoParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(MiniGoParser.FOR)
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.state = 330
                self.scalarDecl()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 331
                self.scalarAssign()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 334
            self.match(MiniGoParser.SEMI)
            self.state = 335
            self.expression(0)
            self.state = 336
            self.match(MiniGoParser.SEMI)
            self.state = 337
            self.scalarAssign()
            self.state = 338
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def UNDERSCORE(self):
            return self.getToken(MiniGoParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forRange

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForRange" ):
                return visitor.visitForRange(self)
            else:
                return visitor.visitChildren(self)




    def forRange(self):

        localctx = MiniGoParser.ForRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_forRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(MiniGoParser.FOR)
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 341
                self.match(MiniGoParser.ID)
                self.state = 342
                self.match(MiniGoParser.COMMA)
                self.state = 343
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.UNDERSCORE]:
                self.state = 344
                self.match(MiniGoParser.UNDERSCORE)
                self.state = 345
                self.match(MiniGoParser.COMMA)
                self.state = 346
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 349
            self.match(MiniGoParser.DECLARE)
            self.state = 350
            self.match(MiniGoParser.RANGE)
            self.state = 351
            self.expression(0)
            self.state = 352
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def typeSpec(self):
            return self.getTypedRuleContext(MiniGoParser.TypeSpecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_scalarDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarDecl" ):
                return visitor.visitScalarDecl(self)
            else:
                return visitor.visitChildren(self)




    def scalarDecl(self):

        localctx = MiniGoParser.ScalarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_scalarDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(MiniGoParser.VAR)
            self.state = 355
            self.match(MiniGoParser.ID)
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 356
                self.typeSpec()


            self.state = 359
            self.match(MiniGoParser.ASSIGN)
            self.state = 360
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assignmentOp(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentOpContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_scalarAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarAssign" ):
                return visitor.visitScalarAssign(self)
            else:
                return visitor.visitChildren(self)




    def scalarAssign(self):

        localctx = MiniGoParser.ScalarAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_scalarAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(MiniGoParser.ID)
            self.state = 363
            self.assignmentOp()
            self.state = 364
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = MiniGoParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = MiniGoParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStmt" ):
                return visitor.visitCallStmt(self)
            else:
                return visitor.visitChildren(self)




    def callStmt(self):

        localctx = MiniGoParser.CallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_callStmt)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.methodCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = MiniGoParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(MiniGoParser.RETURN)
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STR_LIT) | (1 << MiniGoParser.ID))) != 0):
                self.state = 375
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitiveType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = MiniGoParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitiveTypeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_baseType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseType" ):
                return visitor.visitBaseType(self)
            else:
                return visitor.visitChildren(self)




    def baseType(self):

        localctx = MiniGoParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_baseType)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpec" ):
                return visitor.visitTypeSpec(self)
            else:
                return visitor.visitChildren(self)




    def typeSpec(self):

        localctx = MiniGoParser.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_typeSpec)
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.arrayType()
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.baseType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notArrayLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.NotArrayLiteralContext,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_literal)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STR_LIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.notArrayLiteral()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.arrayLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer(self):
            return self.getTypedRuleContext(MiniGoParser.IntegerContext,0)


        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STR_LIT(self):
            return self.getToken(MiniGoParser.STR_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def structLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructLiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_notArrayLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotArrayLiteral" ):
                return visitor.visitNotArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def notArrayLiteral(self):

        localctx = MiniGoParser.NotArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_notArrayLiteral)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.integer()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 394
                self.match(MiniGoParser.STR_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 395
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 396
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 397
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 398
                self.structLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def arrayBody(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayBodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = MiniGoParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_arrayLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.arrayType()
            self.state = 402
            self.arrayBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def arrayList(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayListContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayBody" ):
                return visitor.visitArrayBody(self)
            else:
                return visitor.visitChildren(self)




    def arrayBody(self):

        localctx = MiniGoParser.ArrayBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arrayBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(MiniGoParser.LBRACE)
            self.state = 405
            self.arrayList()
            self.state = 406
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def arrayDim(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(MiniGoParser.LBRACK)
            self.state = 409
            self.arrayDim()
            self.state = 410
            self.match(MiniGoParser.RBRACK)
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK]:
                self.state = 411
                self.arrayType()
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                self.state = 412
                self.baseType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer(self):
            return self.getTypedRuleContext(MiniGoParser.IntegerContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayDim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDim" ):
                return visitor.visitArrayDim(self)
            else:
                return visitor.visitChildren(self)




    def arrayDim(self):

        localctx = MiniGoParser.ArrayDimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_arrayDim)
        try:
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.integer()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayMember(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayMemberContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arrayList(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayList" ):
                return visitor.visitArrayList(self)
            else:
                return visitor.visitChildren(self)




    def arrayList(self):

        localctx = MiniGoParser.ArrayListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_arrayList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.arrayMember()
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 420
                self.match(MiniGoParser.COMMA)
                self.state = 421
                self.arrayList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notArrayLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.NotArrayLiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrayBody(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayBodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayMember

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayMember" ):
                return visitor.visitArrayMember(self)
            else:
                return visitor.visitChildren(self)




    def arrayMember(self):

        localctx = MiniGoParser.ArrayMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arrayMember)
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.notArrayLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 426
                self.arrayBody()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def structElements(self):
            return self.getTypedRuleContext(MiniGoParser.StructElementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructLiteral" ):
                return visitor.visitStructLiteral(self)
            else:
                return visitor.visitChildren(self)




    def structLiteral(self):

        localctx = MiniGoParser.StructLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_structLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MiniGoParser.ID)
            self.state = 430
            self.match(MiniGoParser.LBRACE)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 431
                self.structElements()


            self.state = 434
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structElement(self):
            return self.getTypedRuleContext(MiniGoParser.StructElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def structElements(self):
            return self.getTypedRuleContext(MiniGoParser.StructElementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structElements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructElements" ):
                return visitor.visitStructElements(self)
            else:
                return visitor.visitChildren(self)




    def structElements(self):

        localctx = MiniGoParser.StructElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_structElements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.structElement()
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 437
                self.match(MiniGoParser.COMMA)
                self.state = 438
                self.structElements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructElement" ):
                return visitor.visitStructElement(self)
            else:
                return visitor.visitChildren(self)




    def structElement(self):

        localctx = MiniGoParser.StructElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_structElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(MiniGoParser.ID)
            self.state = 442
            self.match(MiniGoParser.COLON)
            self.state = 443
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def exprList(self):
            return self.getTypedRuleContext(MiniGoParser.ExprListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = MiniGoParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_exprList)
        try:
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.expression(0)
                self.state = 446
                self.match(MiniGoParser.COMMA)
                self.state = 447
                self.exprList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 460
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 455
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 456
                    self.match(MiniGoParser.OR)
                    self.state = 457
                    self.expr1(0) 
                self.state = 462
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 471
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 466
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 467
                    self.match(MiniGoParser.AND)
                    self.state = 468
                    self.expr2(0) 
                self.state = 473
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def compOp(self):
            return self.getTypedRuleContext(MiniGoParser.CompOpContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 483
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 477
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 478
                    self.compOp()
                    self.state = 479
                    self.expr3(0) 
                self.state = 485
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(MiniGoParser.NOTEQUAL, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def LESSEQUAL(self):
            return self.getToken(MiniGoParser.LESSEQUAL, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def GREATEREQUAL(self):
            return self.getToken(MiniGoParser.GREATEREQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_compOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompOp" ):
                return visitor.visitCompOp(self)
            else:
                return visitor.visitChildren(self)




    def compOp(self):

        localctx = MiniGoParser.CompOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOTEQUAL) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESSEQUAL) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATEREQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def addOp(self):
            return self.getTypedRuleContext(MiniGoParser.AddOpContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 497
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 491
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 492
                    self.addOp()
                    self.state = 493
                    self.expr4(0) 
                self.state = 499
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AddOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_addOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOp" ):
                return visitor.visitAddOp(self)
            else:
                return visitor.visitChildren(self)




    def addOp(self):

        localctx = MiniGoParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def mulOp(self):
            return self.getTypedRuleContext(MiniGoParser.MulOpContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 511
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 505
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 506
                    self.mulOp()
                    self.state = 507
                    self.expr5() 
                self.state = 513
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MulOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mulOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulOp" ):
                return visitor.visitMulOp(self)
            else:
                return visitor.visitChildren(self)




    def mulOp(self):

        localctx = MiniGoParser.MulOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_mulOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 517
                self.expr5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STR_LIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 518
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 537
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 535
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 524
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 525
                        self.match(MiniGoParser.LBRACK)
                        self.state = 526
                        self.expression(0)
                        self.state = 527
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 529
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 530
                        self.match(MiniGoParser.DOT)
                        self.state = 533
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                        if la_ == 1:
                            self.state = 531
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 532
                            self.funcCall()
                            pass


                        pass

             
                self.state = 539
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_expr7)
        try:
            self.state = 547
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 541
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 542
                self.match(MiniGoParser.LPAREN)
                self.state = 543
                self.expression(0)
                self.state = 544
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 546
                self.funcCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def exprList(self):
            return self.getTypedRuleContext(MiniGoParser.ExprListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = MiniGoParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(MiniGoParser.ID)
            self.state = 550
            self.match(MiniGoParser.LPAREN)
            self.state = 552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STR_LIT) | (1 << MiniGoParser.ID))) != 0):
                self.state = 551
                self.exprList()


            self.state = 554
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = MiniGoParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.expr6(0)
            self.state = 557
            self.match(MiniGoParser.DOT)
            self.state = 558
            self.funcCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC_LIT(self):
            return self.getToken(MiniGoParser.DEC_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(MiniGoParser.BIN_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_integer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = MiniGoParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.lhs_sempred
        self._predicates[50] = self.expression_sempred
        self._predicates[51] = self.expr1_sempred
        self._predicates[52] = self.expr2_sempred
        self._predicates[54] = self.expr3_sempred
        self._predicates[56] = self.expr4_sempred
        self._predicates[59] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




