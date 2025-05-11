# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u01e4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\7\65\u0152")
        buf.write("\n\65\f\65\16\65\u0155\13\65\5\65\u0157\n\65\3\66\3\66")
        buf.write("\3\66\6\66\u015c\n\66\r\66\16\66\u015d\3\67\3\67\3\67")
        buf.write("\6\67\u0163\n\67\r\67\16\67\u0164\38\38\38\68\u016a\n")
        buf.write("8\r8\168\u016b\39\69\u016f\n9\r9\169\u0170\39\39\79\u0175")
        buf.write("\n9\f9\169\u0178\139\39\39\59\u017c\n9\39\69\u017f\n9")
        buf.write("\r9\169\u0180\59\u0183\n9\3:\3:\3;\3;\3;\3<\3<\5<\u018c")
        buf.write("\n<\3=\3=\7=\u0190\n=\f=\16=\u0193\13=\3=\3=\3>\3>\3?")
        buf.write("\3?\7?\u019b\n?\f?\16?\u019e\13?\3@\5@\u01a1\n@\3@\3@")
        buf.write("\3@\3A\6A\u01a7\nA\rA\16A\u01a8\3A\3A\3B\3B\3B\3B\7B\u01b1")
        buf.write("\nB\fB\16B\u01b4\13B\3B\3B\3C\3C\3C\3C\3C\7C\u01bd\nC")
        buf.write("\fC\16C\u01c0\13C\3C\3C\3C\3C\3C\3D\3D\7D\u01c9\nD\fD")
        buf.write("\16D\u01cc\13D\3D\3D\3D\5D\u01d1\nD\3D\3D\3E\3E\3E\3F")
        buf.write("\3F\7F\u01da\nF\fF\16F\u01dd\13F\3F\3F\3F\3G\3G\3G\3\u01be")
        buf.write("\2H\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s\2u\2w\2y;{<}=\177>\u0081?\u0083@\u0085A\u0087B\u0089")
        buf.write("\2\u008bC\u008dD\3\2\23\3\2\63;\3\2\62;\4\2DDdd\3\2\62")
        buf.write("\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--")
        buf.write("//\7\2$$^^ppttvv\5\2\f\f$$^^\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\5\2\13\13\16\17\"\"\4\2\f\f\17\17\3\3\f\f\2\u01f4\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2")
        buf.write("\2\5\u0092\3\2\2\2\7\u0097\3\2\2\2\t\u009b\3\2\2\2\13")
        buf.write("\u00a2\3\2\2\2\r\u00a7\3\2\2\2\17\u00ac\3\2\2\2\21\u00b3")
        buf.write("\3\2\2\2\23\u00bd\3\2\2\2\25\u00c4\3\2\2\2\27\u00c8\3")
        buf.write("\2\2\2\31\u00ce\3\2\2\2\33\u00d2\3\2\2\2\35\u00db\3\2")
        buf.write("\2\2\37\u00e1\3\2\2\2!\u00e7\3\2\2\2#\u00eb\3\2\2\2%\u00f0")
        buf.write("\3\2\2\2\'\u00f6\3\2\2\2)\u00fe\3\2\2\2+\u0104\3\2\2\2")
        buf.write("-\u0106\3\2\2\2/\u0108\3\2\2\2\61\u010a\3\2\2\2\63\u010c")
        buf.write("\3\2\2\2\65\u010e\3\2\2\2\67\u0111\3\2\2\29\u0114\3\2")
        buf.write("\2\2;\u0116\3\2\2\2=\u0119\3\2\2\2?\u011b\3\2\2\2A\u011e")
        buf.write("\3\2\2\2C\u0121\3\2\2\2E\u0123\3\2\2\2G\u0126\3\2\2\2")
        buf.write("I\u0129\3\2\2\2K\u012c\3\2\2\2M\u012f\3\2\2\2O\u0132\3")
        buf.write("\2\2\2Q\u0135\3\2\2\2S\u0138\3\2\2\2U\u013a\3\2\2\2W\u013c")
        buf.write("\3\2\2\2Y\u013e\3\2\2\2[\u0140\3\2\2\2]\u0142\3\2\2\2")
        buf.write("_\u0144\3\2\2\2a\u0146\3\2\2\2c\u0148\3\2\2\2e\u014a\3")
        buf.write("\2\2\2g\u014c\3\2\2\2i\u0156\3\2\2\2k\u0158\3\2\2\2m\u015f")
        buf.write("\3\2\2\2o\u0166\3\2\2\2q\u016e\3\2\2\2s\u0184\3\2\2\2")
        buf.write("u\u0186\3\2\2\2w\u018b\3\2\2\2y\u018d\3\2\2\2{\u0196\3")
        buf.write("\2\2\2}\u0198\3\2\2\2\177\u01a0\3\2\2\2\u0081\u01a6\3")
        buf.write("\2\2\2\u0083\u01ac\3\2\2\2\u0085\u01b7\3\2\2\2\u0087\u01c6")
        buf.write("\3\2\2\2\u0089\u01d4\3\2\2\2\u008b\u01d7\3\2\2\2\u008d")
        buf.write("\u01e1\3\2\2\2\u008f\u0090\7k\2\2\u0090\u0091\7h\2\2\u0091")
        buf.write("\4\3\2\2\2\u0092\u0093\7g\2\2\u0093\u0094\7n\2\2\u0094")
        buf.write("\u0095\7u\2\2\u0095\u0096\7g\2\2\u0096\6\3\2\2\2\u0097")
        buf.write("\u0098\7h\2\2\u0098\u0099\7q\2\2\u0099\u009a\7t\2\2\u009a")
        buf.write("\b\3\2\2\2\u009b\u009c\7t\2\2\u009c\u009d\7g\2\2\u009d")
        buf.write("\u009e\7v\2\2\u009e\u009f\7w\2\2\u009f\u00a0\7t\2\2\u00a0")
        buf.write("\u00a1\7p\2\2\u00a1\n\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3")
        buf.write("\u00a4\7w\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7e\2\2\u00a6")
        buf.write("\f\3\2\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9\7{\2\2\u00a9")
        buf.write("\u00aa\7r\2\2\u00aa\u00ab\7g\2\2\u00ab\16\3\2\2\2\u00ac")
        buf.write("\u00ad\7u\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7t\2\2\u00af")
        buf.write("\u00b0\7w\2\2\u00b0\u00b1\7e\2\2\u00b1\u00b2\7v\2\2\u00b2")
        buf.write("\20\3\2\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5\7p\2\2\u00b5")
        buf.write("\u00b6\7v\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7t\2\2\u00b8")
        buf.write("\u00b9\7h\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7e\2\2\u00bb")
        buf.write("\u00bc\7g\2\2\u00bc\22\3\2\2\2\u00bd\u00be\7u\2\2\u00be")
        buf.write("\u00bf\7v\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7k\2\2\u00c1")
        buf.write("\u00c2\7p\2\2\u00c2\u00c3\7i\2\2\u00c3\24\3\2\2\2\u00c4")
        buf.write("\u00c5\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7v\2\2\u00c7")
        buf.write("\26\3\2\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca\7n\2\2\u00ca")
        buf.write("\u00cb\7q\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd\7v\2\2\u00cd")
        buf.write("\30\3\2\2\2\u00ce\u00cf\7x\2\2\u00cf\u00d0\7c\2\2\u00d0")
        buf.write("\u00d1\7t\2\2\u00d1\32\3\2\2\2\u00d2\u00d3\7e\2\2\u00d3")
        buf.write("\u00d4\7q\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6\7v\2\2\u00d6")
        buf.write("\u00d7\7k\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7w\2\2\u00d9")
        buf.write("\u00da\7g\2\2\u00da\34\3\2\2\2\u00db\u00dc\7d\2\2\u00dc")
        buf.write("\u00dd\7t\2\2\u00dd\u00de\7g\2\2\u00de\u00df\7c\2\2\u00df")
        buf.write("\u00e0\7m\2\2\u00e0\36\3\2\2\2\u00e1\u00e2\7t\2\2\u00e2")
        buf.write("\u00e3\7c\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7i\2\2\u00e5")
        buf.write("\u00e6\7g\2\2\u00e6 \3\2\2\2\u00e7\u00e8\7p\2\2\u00e8")
        buf.write("\u00e9\7k\2\2\u00e9\u00ea\7n\2\2\u00ea\"\3\2\2\2\u00eb")
        buf.write("\u00ec\7v\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7w\2\2\u00ee")
        buf.write("\u00ef\7g\2\2\u00ef$\3\2\2\2\u00f0\u00f1\7h\2\2\u00f1")
        buf.write("\u00f2\7c\2\2\u00f2\u00f3\7n\2\2\u00f3\u00f4\7u\2\2\u00f4")
        buf.write("\u00f5\7g\2\2\u00f5&\3\2\2\2\u00f6\u00f7\7d\2\2\u00f7")
        buf.write("\u00f8\7q\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa\7n\2\2\u00fa")
        buf.write("\u00fb\7g\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7p\2\2\u00fd")
        buf.write("(\3\2\2\2\u00fe\u00ff\7e\2\2\u00ff\u0100\7q\2\2\u0100")
        buf.write("\u0101\7p\2\2\u0101\u0102\7u\2\2\u0102\u0103\7v\2\2\u0103")
        buf.write("*\3\2\2\2\u0104\u0105\7-\2\2\u0105,\3\2\2\2\u0106\u0107")
        buf.write("\7/\2\2\u0107.\3\2\2\2\u0108\u0109\7,\2\2\u0109\60\3\2")
        buf.write("\2\2\u010a\u010b\7\61\2\2\u010b\62\3\2\2\2\u010c\u010d")
        buf.write("\7\'\2\2\u010d\64\3\2\2\2\u010e\u010f\7?\2\2\u010f\u0110")
        buf.write("\7?\2\2\u0110\66\3\2\2\2\u0111\u0112\7#\2\2\u0112\u0113")
        buf.write("\7?\2\2\u01138\3\2\2\2\u0114\u0115\7>\2\2\u0115:\3\2\2")
        buf.write("\2\u0116\u0117\7>\2\2\u0117\u0118\7?\2\2\u0118<\3\2\2")
        buf.write("\2\u0119\u011a\7@\2\2\u011a>\3\2\2\2\u011b\u011c\7@\2")
        buf.write("\2\u011c\u011d\7?\2\2\u011d@\3\2\2\2\u011e\u011f\7<\2")
        buf.write("\2\u011f\u0120\7?\2\2\u0120B\3\2\2\2\u0121\u0122\7?\2")
        buf.write("\2\u0122D\3\2\2\2\u0123\u0124\7-\2\2\u0124\u0125\7?\2")
        buf.write("\2\u0125F\3\2\2\2\u0126\u0127\7/\2\2\u0127\u0128\7?\2")
        buf.write("\2\u0128H\3\2\2\2\u0129\u012a\7,\2\2\u012a\u012b\7?\2")
        buf.write("\2\u012bJ\3\2\2\2\u012c\u012d\7\61\2\2\u012d\u012e\7?")
        buf.write("\2\2\u012eL\3\2\2\2\u012f\u0130\7\'\2\2\u0130\u0131\7")
        buf.write("?\2\2\u0131N\3\2\2\2\u0132\u0133\7(\2\2\u0133\u0134\7")
        buf.write("(\2\2\u0134P\3\2\2\2\u0135\u0136\7~\2\2\u0136\u0137\7")
        buf.write("~\2\2\u0137R\3\2\2\2\u0138\u0139\7#\2\2\u0139T\3\2\2\2")
        buf.write("\u013a\u013b\7\60\2\2\u013bV\3\2\2\2\u013c\u013d\7*\2")
        buf.write("\2\u013dX\3\2\2\2\u013e\u013f\7+\2\2\u013fZ\3\2\2\2\u0140")
        buf.write("\u0141\7}\2\2\u0141\\\3\2\2\2\u0142\u0143\7\177\2\2\u0143")
        buf.write("^\3\2\2\2\u0144\u0145\7]\2\2\u0145`\3\2\2\2\u0146\u0147")
        buf.write("\7_\2\2\u0147b\3\2\2\2\u0148\u0149\7.\2\2\u0149d\3\2\2")
        buf.write("\2\u014a\u014b\7=\2\2\u014bf\3\2\2\2\u014c\u014d\7<\2")
        buf.write("\2\u014dh\3\2\2\2\u014e\u0157\7\62\2\2\u014f\u0153\t\2")
        buf.write("\2\2\u0150\u0152\t\3\2\2\u0151\u0150\3\2\2\2\u0152\u0155")
        buf.write("\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154")
        buf.write("\u0157\3\2\2\2\u0155\u0153\3\2\2\2\u0156\u014e\3\2\2\2")
        buf.write("\u0156\u014f\3\2\2\2\u0157j\3\2\2\2\u0158\u0159\7\62\2")
        buf.write("\2\u0159\u015b\t\4\2\2\u015a\u015c\t\5\2\2\u015b\u015a")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015b\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015el\3\2\2\2\u015f\u0160\7\62\2\2\u0160")
        buf.write("\u0162\t\6\2\2\u0161\u0163\t\7\2\2\u0162\u0161\3\2\2\2")
        buf.write("\u0163\u0164\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165n\3\2\2\2\u0166\u0167\7\62\2\2\u0167\u0169")
        buf.write("\t\b\2\2\u0168\u016a\t\t\2\2\u0169\u0168\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016cp\3\2\2\2\u016d\u016f\t\3\2\2\u016e\u016d\3\2\2")
        buf.write("\2\u016f\u0170\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171")
        buf.write("\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0176\7\60\2\2\u0173")
        buf.write("\u0175\t\3\2\2\u0174\u0173\3\2\2\2\u0175\u0178\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0182\3")
        buf.write("\2\2\2\u0178\u0176\3\2\2\2\u0179\u017b\t\n\2\2\u017a\u017c")
        buf.write("\t\13\2\2\u017b\u017a\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017e\3\2\2\2\u017d\u017f\t\3\2\2\u017e\u017d\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3")
        buf.write("\2\2\2\u0181\u0183\3\2\2\2\u0182\u0179\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183r\3\2\2\2\u0184\u0185\t\f\2\2\u0185t\3\2")
        buf.write("\2\2\u0186\u0187\7^\2\2\u0187\u0188\5s:\2\u0188v\3\2\2")
        buf.write("\2\u0189\u018c\n\r\2\2\u018a\u018c\5u;\2\u018b\u0189\3")
        buf.write("\2\2\2\u018b\u018a\3\2\2\2\u018cx\3\2\2\2\u018d\u0191")
        buf.write("\7$\2\2\u018e\u0190\5w<\2\u018f\u018e\3\2\2\2\u0190\u0193")
        buf.write("\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192")
        buf.write("\u0194\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0195\7$\2\2")
        buf.write("\u0195z\3\2\2\2\u0196\u0197\7a\2\2\u0197|\3\2\2\2\u0198")
        buf.write("\u019c\t\16\2\2\u0199\u019b\t\17\2\2\u019a\u0199\3\2\2")
        buf.write("\2\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d")
        buf.write("\3\2\2\2\u019d~\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a1")
        buf.write("\7\17\2\2\u01a0\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a3\7\f\2\2\u01a3\u01a4\b@\2\2")
        buf.write("\u01a4\u0080\3\2\2\2\u01a5\u01a7\t\20\2\2\u01a6\u01a5")
        buf.write("\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8")
        buf.write("\u01a9\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\bA\3\2")
        buf.write("\u01ab\u0082\3\2\2\2\u01ac\u01ad\7\61\2\2\u01ad\u01ae")
        buf.write("\7\61\2\2\u01ae\u01b2\3\2\2\2\u01af\u01b1\n\21\2\2\u01b0")
        buf.write("\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2")
        buf.write("\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3")
        buf.write("\2\2\2\u01b5\u01b6\bB\3\2\u01b6\u0084\3\2\2\2\u01b7\u01b8")
        buf.write("\7\61\2\2\u01b8\u01b9\7,\2\2\u01b9\u01be\3\2\2\2\u01ba")
        buf.write("\u01bd\5\u0085C\2\u01bb\u01bd\13\2\2\2\u01bc\u01ba\3\2")
        buf.write("\2\2\u01bc\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c1\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c1\u01c2\7,\2\2\u01c2\u01c3\7\61\2\2")
        buf.write("\u01c3\u01c4\3\2\2\2\u01c4\u01c5\bC\3\2\u01c5\u0086\3")
        buf.write("\2\2\2\u01c6\u01ca\7$\2\2\u01c7\u01c9\5w<\2\u01c8\u01c7")
        buf.write("\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01d0\3\2\2\2\u01cc\u01ca\3\2\2\2")
        buf.write("\u01cd\u01ce\7\17\2\2\u01ce\u01d1\7\f\2\2\u01cf\u01d1")
        buf.write("\t\22\2\2\u01d0\u01cd\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1")
        buf.write("\u01d2\3\2\2\2\u01d2\u01d3\bD\4\2\u01d3\u0088\3\2\2\2")
        buf.write("\u01d4\u01d5\7^\2\2\u01d5\u01d6\n\f\2\2\u01d6\u008a\3")
        buf.write("\2\2\2\u01d7\u01db\7$\2\2\u01d8\u01da\5w<\2\u01d9\u01d8")
        buf.write("\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01de\u01df\5\u0089E\2\u01df\u01e0\bF\5\2\u01e0\u008c")
        buf.write("\3\2\2\2\u01e1\u01e2\13\2\2\2\u01e2\u01e3\bG\6\2\u01e3")
        buf.write("\u008e\3\2\2\2\30\2\u0153\u0156\u015d\u0164\u016b\u0170")
        buf.write("\u0176\u017b\u0180\u0182\u018b\u0191\u019c\u01a0\u01a8")
        buf.write("\u01b2\u01bc\u01be\u01ca\u01d0\u01db\7\3@\2\b\2\2\3D\3")
        buf.write("\3F\4\3G\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    VAR = 12
    CONTINUE = 13
    BREAK = 14
    RANGE = 15
    NIL = 16
    TRUE = 17
    FALSE = 18
    BOOLEAN = 19
    CONST = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    EQUAL = 26
    NOTEQUAL = 27
    LESS = 28
    LESSEQUAL = 29
    GREATER = 30
    GREATEREQUAL = 31
    DECLARE = 32
    ASSIGN = 33
    ADD_ASSIGN = 34
    SUB_ASSIGN = 35
    MUL_ASSIGN = 36
    DIV_ASSIGN = 37
    MOD_ASSIGN = 38
    AND = 39
    OR = 40
    NOT = 41
    DOT = 42
    LPAREN = 43
    RPAREN = 44
    LBRACE = 45
    RBRACE = 46
    LBRACK = 47
    RBRACK = 48
    COMMA = 49
    SEMI = 50
    COLON = 51
    DEC_LIT = 52
    BIN_LIT = 53
    OCT_LIT = 54
    HEX_LIT = 55
    FLOAT_LIT = 56
    STR_LIT = 57
    UNDERSCORE = 58
    ID = 59
    NEWLINE = 60
    WS = 61
    COMMENT = 62
    BLOCK_COMMENT = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'var'", "'continue'", 
            "'break'", "'range'", "'nil'", "'true'", "'false'", "'boolean'", 
            "'const'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "':='", "'='", "'+='", "'-='", 
            "'*='", "'/='", "'%='", "'&&'", "'||'", "'!'", "'.'", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "':'", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "VAR", "CONTINUE", "BREAK", "RANGE", 
            "NIL", "TRUE", "FALSE", "BOOLEAN", "CONST", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "NOTEQUAL", "LESS", "LESSEQUAL", "GREATER", 
            "GREATEREQUAL", "DECLARE", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
            "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AND", "OR", "NOT", 
            "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
            "COMMA", "SEMI", "COLON", "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", 
            "FLOAT_LIT", "STR_LIT", "UNDERSCORE", "ID", "NEWLINE", "WS", 
            "COMMENT", "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "BOOLEAN", "CONST", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", 
                  "LESS", "LESSEQUAL", "GREATER", "GREATEREQUAL", "DECLARE", 
                  "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "AND", "OR", "NOT", "DOT", "LPAREN", "RPAREN", 
                  "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMI", 
                  "COLON", "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", 
                  "ESC_LETTER", "ESCAPE", "STR_CHAR", "STR_LIT", "UNDERSCORE", 
                  "ID", "NEWLINE", "WS", "COMMENT", "BLOCK_COMMENT", "UNCLOSE_STRING", 
                  "ESCAPE_ILLEGAL", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        self.last_token_type = self.type
        if self.last_token_type == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif self.last_token_type == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif self.last_token_type == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[62] = self.NEWLINE_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                literal_tokens = [
                    self.DEC_LIT, self.HEX_LIT, self.BIN_LIT, self.OCT_LIT, self.FLOAT_LIT, self.BOOLEAN, self.STR_LIT
                ]
                type_tokens = [
                    self.STRING, self.INT, self.FLOAT, self.NIL, self.TRUE, self.FALSE
                ]
                statement_tokens = [
                    self.RETURN, self.CONTINUE, self.BREAK
                ]
                bracket_tokens = [
                    self.RPAREN, self.RBRACK, self.RBRACE
                ]
                identifier_tokens = [
                    self.ID
                ]
                
                if hasattr(self, 'last_token_type') and self.last_token_type in (
                    literal_tokens + type_tokens + statement_tokens + bracket_tokens + identifier_tokens
                ):
                    self.text = ';'
                    self.type = self.SEMI
                else:
                    self.skip()

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                raise UncloseString(self.text[:-2])  # Case \r\n
            elif (self.text[-1] == '\n'):
                raise UncloseString(self.text[:-1])  # Case \n
            else:
                raise UncloseString(self.text)    # Case EOF

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text)

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


