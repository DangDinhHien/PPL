# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01c3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\5\2\u0088\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#")
        buf.write("\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\6\67\u014f\n\67\r\67\16\67\u0150\38\68\u0154\n8")
        buf.write("\r8\168\u0155\38\38\78\u015a\n8\f8\168\u015d\138\38\5")
        buf.write("8\u0160\n8\38\68\u0163\n8\r8\168\u0164\38\58\u0168\n8")
        buf.write("\39\39\59\u016c\n9\39\69\u016f\n9\r9\169\u0170\3:\3:\3")
        buf.write(":\7:\u0176\n:\f:\16:\u0179\13:\3:\3:\3;\3;\3;\3<\6<\u0181")
        buf.write("\n<\r<\16<\u0182\3<\3<\3=\3=\3=\3=\7=\u018b\n=\f=\16=")
        buf.write("\u018e\13=\3=\3=\3=\3=\3=\3>\3>\3>\3>\7>\u0199\n>\f>\16")
        buf.write(">\u019c\13>\3>\3>\3?\3?\7?\u01a2\n?\f?\16?\u01a5\13?\3")
        buf.write("@\3@\3@\3A\3A\3A\7A\u01ad\nA\fA\16A\u01b0\13A\3A\5A\u01b3")
        buf.write("\nA\3A\3A\3B\3B\3B\7B\u01ba\nB\fB\16B\u01bd\13B\3B\3B")
        buf.write("\3B\3B\3B\4\u018c\u01bb\2C\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q\2s:u\2w;y<{=}>\177?\u0081@\u0083")
        buf.write("A\3\2\16\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2")
        buf.write("$$^^ddhhppttvv\5\2\13\f\16\17\"\"\4\2\f\f\17\17\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\3\3\f\f\4\2$$^^\3\2^^\2\u01d3\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2s")
        buf.write("\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2")
        buf.write("\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\3\u0087\3")
        buf.write("\2\2\2\5\u0089\3\2\2\2\7\u0091\3\2\2\2\t\u0097\3\2\2\2")
        buf.write("\13\u009d\3\2\2\2\r\u00a6\3\2\2\2\17\u00a9\3\2\2\2\21")
        buf.write("\u00ae\3\2\2\2\23\u00b6\3\2\2\2\25\u00bc\3\2\2\2\27\u00bf")
        buf.write("\3\2\2\2\31\u00c3\3\2\2\2\33\u00c7\3\2\2\2\35\u00ce\3")
        buf.write("\2\2\2\37\u00d3\3\2\2\2!\u00d7\3\2\2\2#\u00de\3\2\2\2")
        buf.write("%\u00e3\3\2\2\2\'\u00e9\3\2\2\2)\u00ee\3\2\2\2+\u00f2")
        buf.write("\3\2\2\2-\u00f7\3\2\2\2/\u00fd\3\2\2\2\61\u0104\3\2\2")
        buf.write("\2\63\u0107\3\2\2\2\65\u010e\3\2\2\2\67\u0110\3\2\2\2")
        buf.write("9\u0112\3\2\2\2;\u0114\3\2\2\2=\u0116\3\2\2\2?\u0118\3")
        buf.write("\2\2\2A\u011a\3\2\2\2C\u011d\3\2\2\2E\u0120\3\2\2\2G\u0122")
        buf.write("\3\2\2\2I\u0124\3\2\2\2K\u0127\3\2\2\2M\u012a\3\2\2\2")
        buf.write("O\u012d\3\2\2\2Q\u0130\3\2\2\2S\u0132\3\2\2\2U\u0134\3")
        buf.write("\2\2\2W\u0137\3\2\2\2Y\u0139\3\2\2\2[\u013b\3\2\2\2]\u013d")
        buf.write("\3\2\2\2_\u013f\3\2\2\2a\u0141\3\2\2\2c\u0143\3\2\2\2")
        buf.write("e\u0145\3\2\2\2g\u0147\3\2\2\2i\u0149\3\2\2\2k\u014b\3")
        buf.write("\2\2\2m\u014e\3\2\2\2o\u0167\3\2\2\2q\u0169\3\2\2\2s\u0172")
        buf.write("\3\2\2\2u\u017c\3\2\2\2w\u0180\3\2\2\2y\u0186\3\2\2\2")
        buf.write("{\u0194\3\2\2\2}\u019f\3\2\2\2\177\u01a6\3\2\2\2\u0081")
        buf.write("\u01a9\3\2\2\2\u0083\u01b6\3\2\2\2\u0085\u0088\5#\22\2")
        buf.write("\u0086\u0088\5%\23\2\u0087\u0085\3\2\2\2\u0087\u0086\3")
        buf.write("\2\2\2\u0088\4\3\2\2\2\u0089\u008a\7d\2\2\u008a\u008b")
        buf.write("\7q\2\2\u008b\u008c\7q\2\2\u008c\u008d\7n\2\2\u008d\u008e")
        buf.write("\7g\2\2\u008e\u008f\7c\2\2\u008f\u0090\7p\2\2\u0090\6")
        buf.write("\3\2\2\2\u0091\u0092\7d\2\2\u0092\u0093\7t\2\2\u0093\u0094")
        buf.write("\7g\2\2\u0094\u0095\7c\2\2\u0095\u0096\7m\2\2\u0096\b")
        buf.write("\3\2\2\2\u0097\u0098\7e\2\2\u0098\u0099\7n\2\2\u0099\u009a")
        buf.write("\7c\2\2\u009a\u009b\7u\2\2\u009b\u009c\7u\2\2\u009c\n")
        buf.write("\3\2\2\2\u009d\u009e\7e\2\2\u009e\u009f\7q\2\2\u009f\u00a0")
        buf.write("\7p\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3")
        buf.write("\7p\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5\7g\2\2\u00a5\f")
        buf.write("\3\2\2\2\u00a6\u00a7\7f\2\2\u00a7\u00a8\7q\2\2\u00a8\16")
        buf.write("\3\2\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac")
        buf.write("\7u\2\2\u00ac\u00ad\7g\2\2\u00ad\20\3\2\2\2\u00ae\u00af")
        buf.write("\7g\2\2\u00af\u00b0\7z\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2")
        buf.write("\7g\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4\7f\2\2\u00b4\u00b5")
        buf.write("\7u\2\2\u00b5\22\3\2\2\2\u00b6\u00b7\7h\2\2\u00b7\u00b8")
        buf.write("\7n\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb")
        buf.write("\7v\2\2\u00bb\24\3\2\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be")
        buf.write("\7h\2\2\u00be\26\3\2\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1")
        buf.write("\7p\2\2\u00c1\u00c2\7v\2\2\u00c2\30\3\2\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7y\2\2\u00c6\32")
        buf.write("\3\2\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd")
        buf.write("\7i\2\2\u00cd\34\3\2\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0")
        buf.write("\7j\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7p\2\2\u00d2\36")
        buf.write("\3\2\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6")
        buf.write("\7t\2\2\u00d6 \3\2\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7w\2\2\u00db\u00dc")
        buf.write("\7t\2\2\u00dc\u00dd\7p\2\2\u00dd\"\3\2\2\2\u00de\u00df")
        buf.write("\7v\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2")
        buf.write("\7g\2\2\u00e2$\3\2\2\2\u00e3\u00e4\7h\2\2\u00e4\u00e5")
        buf.write("\7c\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8")
        buf.write("\7g\2\2\u00e8&\3\2\2\2\u00e9\u00ea\7x\2\2\u00ea\u00eb")
        buf.write("\7q\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7f\2\2\u00ed(\3")
        buf.write("\2\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1")
        buf.write("\7n\2\2\u00f1*\3\2\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4")
        buf.write("\7j\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7u\2\2\u00f6,\3")
        buf.write("\2\2\2\u00f7\u00f8\7h\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa")
        buf.write("\7p\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7n\2\2\u00fc.\3")
        buf.write("\2\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100")
        buf.write("\7c\2\2\u0100\u0101\7v\2\2\u0101\u0102\7k\2\2\u0102\u0103")
        buf.write("\7e\2\2\u0103\60\3\2\2\2\u0104\u0105\7v\2\2\u0105\u0106")
        buf.write("\7q\2\2\u0106\62\3\2\2\2\u0107\u0108\7f\2\2\u0108\u0109")
        buf.write("\7q\2\2\u0109\u010a\7y\2\2\u010a\u010b\7p\2\2\u010b\u010c")
        buf.write("\7v\2\2\u010c\u010d\7q\2\2\u010d\64\3\2\2\2\u010e\u010f")
        buf.write("\7-\2\2\u010f\66\3\2\2\2\u0110\u0111\7/\2\2\u01118\3\2")
        buf.write("\2\2\u0112\u0113\7,\2\2\u0113:\3\2\2\2\u0114\u0115\7\61")
        buf.write("\2\2\u0115<\3\2\2\2\u0116\u0117\7^\2\2\u0117>\3\2\2\2")
        buf.write("\u0118\u0119\7\'\2\2\u0119@\3\2\2\2\u011a\u011b\7#\2\2")
        buf.write("\u011b\u011c\7?\2\2\u011cB\3\2\2\2\u011d\u011e\7?\2\2")
        buf.write("\u011e\u011f\7?\2\2\u011fD\3\2\2\2\u0120\u0121\7>\2\2")
        buf.write("\u0121F\3\2\2\2\u0122\u0123\7@\2\2\u0123H\3\2\2\2\u0124")
        buf.write("\u0125\7>\2\2\u0125\u0126\7?\2\2\u0126J\3\2\2\2\u0127")
        buf.write("\u0128\7@\2\2\u0128\u0129\7?\2\2\u0129L\3\2\2\2\u012a")
        buf.write("\u012b\7~\2\2\u012b\u012c\7~\2\2\u012cN\3\2\2\2\u012d")
        buf.write("\u012e\7(\2\2\u012e\u012f\7(\2\2\u012fP\3\2\2\2\u0130")
        buf.write("\u0131\7#\2\2\u0131R\3\2\2\2\u0132\u0133\7`\2\2\u0133")
        buf.write("T\3\2\2\2\u0134\u0135\7<\2\2\u0135\u0136\7?\2\2\u0136")
        buf.write("V\3\2\2\2\u0137\u0138\7?\2\2\u0138X\3\2\2\2\u0139\u013a")
        buf.write("\7]\2\2\u013aZ\3\2\2\2\u013b\u013c\7_\2\2\u013c\\\3\2")
        buf.write("\2\2\u013d\u013e\7}\2\2\u013e^\3\2\2\2\u013f\u0140\7\177")
        buf.write("\2\2\u0140`\3\2\2\2\u0141\u0142\7*\2\2\u0142b\3\2\2\2")
        buf.write("\u0143\u0144\7+\2\2\u0144d\3\2\2\2\u0145\u0146\7=\2\2")
        buf.write("\u0146f\3\2\2\2\u0147\u0148\7<\2\2\u0148h\3\2\2\2\u0149")
        buf.write("\u014a\7\60\2\2\u014aj\3\2\2\2\u014b\u014c\7.\2\2\u014c")
        buf.write("l\3\2\2\2\u014d\u014f\t\2\2\2\u014e\u014d\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151n\3\2\2\2\u0152\u0154\t\2\2\2\u0153\u0152\3\2\2")
        buf.write("\2\u0154\u0155\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u015b\7\60\2\2\u0158")
        buf.write("\u015a\t\2\2\2\u0159\u0158\3\2\2\2\u015a\u015d\3\2\2\2")
        buf.write("\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015f\3")
        buf.write("\2\2\2\u015d\u015b\3\2\2\2\u015e\u0160\5q9\2\u015f\u015e")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0168\3\2\2\2\u0161")
        buf.write("\u0163\t\2\2\2\u0162\u0161\3\2\2\2\u0163\u0164\3\2\2\2")
        buf.write("\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\3")
        buf.write("\2\2\2\u0166\u0168\5q9\2\u0167\u0153\3\2\2\2\u0167\u0162")
        buf.write("\3\2\2\2\u0168p\3\2\2\2\u0169\u016b\t\3\2\2\u016a\u016c")
        buf.write("\t\4\2\2\u016b\u016a\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016e\3\2\2\2\u016d\u016f\t\2\2\2\u016e\u016d\3\2\2\2")
        buf.write("\u016f\u0170\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3")
        buf.write("\2\2\2\u0171r\3\2\2\2\u0172\u0177\7$\2\2\u0173\u0176\5")
        buf.write("u;\2\u0174\u0176\n\5\2\2\u0175\u0173\3\2\2\2\u0175\u0174")
        buf.write("\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u017a\3\2\2\2\u0179\u0177\3\2\2\2")
        buf.write("\u017a\u017b\7$\2\2\u017bt\3\2\2\2\u017c\u017d\7^\2\2")
        buf.write("\u017d\u017e\t\6\2\2\u017ev\3\2\2\2\u017f\u0181\t\7\2")
        buf.write("\2\u0180\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0180")
        buf.write("\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0185\b<\2\2\u0185x\3\2\2\2\u0186\u0187\7\61\2\2\u0187")
        buf.write("\u0188\7,\2\2\u0188\u018c\3\2\2\2\u0189\u018b\13\2\2\2")
        buf.write("\u018a\u0189\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018d\3")
        buf.write("\2\2\2\u018c\u018a\3\2\2\2\u018d\u018f\3\2\2\2\u018e\u018c")
        buf.write("\3\2\2\2\u018f\u0190\7,\2\2\u0190\u0191\7\61\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192\u0193\b=\2\2\u0193z\3\2\2\2\u0194")
        buf.write("\u0195\7\'\2\2\u0195\u0196\7\'\2\2\u0196\u019a\3\2\2\2")
        buf.write("\u0197\u0199\n\b\2\2\u0198\u0197\3\2\2\2\u0199\u019c\3")
        buf.write("\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019d")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019e\b>\2\2\u019e")
        buf.write("|\3\2\2\2\u019f\u01a3\t\t\2\2\u01a0\u01a2\t\n\2\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4~\3\2\2\2\u01a5\u01a3\3\2\2")
        buf.write("\2\u01a6\u01a7\13\2\2\2\u01a7\u01a8\b@\3\2\u01a8\u0080")
        buf.write("\3\2\2\2\u01a9\u01ae\7$\2\2\u01aa\u01ad\n\5\2\2\u01ab")
        buf.write("\u01ad\5u;\2\u01ac\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2\u01ad")
        buf.write("\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01af\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b3\t")
        buf.write("\13\2\2\u01b2\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b5\bA\4\2\u01b5\u0082\3\2\2\2\u01b6\u01bb\7$\2\2\u01b7")
        buf.write("\u01ba\5u;\2\u01b8\u01ba\n\f\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bb\u01b9\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3")
        buf.write("\2\2\2\u01be\u01bf\t\r\2\2\u01bf\u01c0\n\6\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01c2\bB\5\2\u01c2\u0084\3\2\2\2\27\2\u0087")
        buf.write("\u0150\u0155\u015b\u015f\u0164\u0167\u016b\u0170\u0175")
        buf.write("\u0177\u0182\u018c\u019a\u01a3\u01ac\u01ae\u01b2\u01b9")
        buf.write("\u01bb\6\b\2\2\3@\2\3A\3\3B\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLLIT = 1
    BOOLEAN = 2
    BREAK = 3
    CLASS = 4
    CONTINUE = 5
    DO = 6
    ELSE = 7
    EXTENDS = 8
    FLOAT = 9
    IF = 10
    INT = 11
    NEW = 12
    STRING = 13
    THEN = 14
    FOR = 15
    RETURN = 16
    TRUE = 17
    FALSE = 18
    VOID = 19
    NIL = 20
    THIS = 21
    FINAL = 22
    STATIC = 23
    TO = 24
    DOWNTO = 25
    ADD = 26
    SUB = 27
    MUL = 28
    FLOATDIV = 29
    INTDIV = 30
    MOD = 31
    NOTEQ = 32
    EQ = 33
    LESS = 34
    GREATER = 35
    LESSEQ = 36
    GREATEREQ = 37
    OR = 38
    AND = 39
    NOT = 40
    CONCAT = 41
    ASSIGN = 42
    OP_BANG = 43
    LSB = 44
    RSB = 45
    LP = 46
    RP = 47
    LB = 48
    RB = 49
    SEMICOLONE = 50
    COLON = 51
    DOT = 52
    COMMA = 53
    INTEGERLIT = 54
    FLOATLIT = 55
    STRINGLIT = 56
    WS = 57
    BLOCKCOMMENT = 58
    LINECOMMENT = 59
    ID = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'else'", 
            "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
            "'then'", "'for'", "'return'", "'true'", "'false'", "'void'", 
            "'nil'", "'this'", "'final'", "'static'", "'to'", "'downto'", 
            "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", 
            "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "':='", 
            "'='", "'['", "']'", "'{'", "'}'", "'('", "')'", "';'", "':'", 
            "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", 
            "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", "FOR", 
            "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", 
            "TO", "DOWNTO", "ADD", "SUB", "MUL", "FLOATDIV", "INTDIV", "MOD", 
            "NOTEQ", "EQ", "LESS", "GREATER", "LESSEQ", "GREATEREQ", "OR", 
            "AND", "NOT", "CONCAT", "ASSIGN", "OP_BANG", "LSB", "RSB", "LP", 
            "RP", "LB", "RB", "SEMICOLONE", "COLON", "DOT", "COMMA", "INTEGERLIT", 
            "FLOATLIT", "STRINGLIT", "WS", "BLOCKCOMMENT", "LINECOMMENT", 
            "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BOOLLIT", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", 
                  "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", 
                  "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", 
                  "THIS", "FINAL", "STATIC", "TO", "DOWNTO", "ADD", "SUB", 
                  "MUL", "FLOATDIV", "INTDIV", "MOD", "NOTEQ", "EQ", "LESS", 
                  "GREATER", "LESSEQ", "GREATEREQ", "OR", "AND", "NOT", 
                  "CONCAT", "ASSIGN", "OP_BANG", "LSB", "RSB", "LP", "RP", 
                  "LB", "RB", "SEMICOLONE", "COLON", "DOT", "COMMA", "INTEGERLIT", 
                  "FLOATLIT", "EXPONENT", "STRINGLIT", "EscapeSequence", 
                  "WS", "BLOCKCOMMENT", "LINECOMMENT", "ID", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[62] = self.ERROR_CHAR_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		raise ErrorToken(self.text)
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                        if self.text[-1]=='\n':
                             raise UncloseString(self.text[1:-1])
                        else:
                            raise UncloseString(self.text[1:])
                    
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                       raise IllegalEscape(self.text[1:-1]) 
                    
     


