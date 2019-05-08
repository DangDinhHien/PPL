# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0215\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\6\2j\n\2\r\2\16\2k\3\2\3\2\3\3\3\3\3\3\3\3\5\3t\n")
        buf.write("\3\3\3\3\3\5\3x\n\3\3\3\3\3\3\4\3\4\6\4~\n\4\r\4\16\4")
        buf.write("\177\3\5\3\5\5\5\u0084\n\5\3\6\5\6\u0087\n\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\5\7\u0091\n\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\7\b\u009b\n\b\f\b\16\b\u009e\13\b\3\t\3")
        buf.write("\t\5\t\u00a2\n\t\3\t\5\t\u00a5\n\t\3\t\3\t\3\t\5\t\u00aa")
        buf.write("\n\t\3\t\3\t\3\t\3\n\3\n\3\n\7\n\u00b2\n\n\f\n\16\n\u00b5")
        buf.write("\13\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\5\f\u00be\n\f\3")
        buf.write("\r\3\r\3\16\3\16\5\16\u00c4\n\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00dd\n")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00e8\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\7\22\u00f3\n\22\f\22\16\22\u00f6\13\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u0101\n\23\f\23")
        buf.write("\16\23\u0104\13\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u0115\n")
        buf.write("\24\f\24\16\24\u0118\13\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\7\25\u0120\n\25\f\25\16\25\u0123\13\25\3\26\3\26\3")
        buf.write("\26\5\26\u0128\n\26\3\27\3\27\3\27\3\27\3\27\5\27\u012f")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\5\30\u0136\n\30\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\7\31\u013e\n\31\f\31\16\31\u0141")
        buf.write("\13\31\3\32\3\32\3\32\5\32\u0146\n\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\5\33\u0150\n\33\3\33\5\33\u0153")
        buf.write("\n\33\3\34\3\34\3\35\3\35\5\35\u0159\n\35\3\35\3\35\3")
        buf.write("\35\3\35\3\36\3\36\3\36\3\36\5\36\u0163\n\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u016a\n\37\3\37\3\37\3\37\3\37\3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\5!\u0178\n!\3!\3!\3\"\3\"\5\"\u017e")
        buf.write("\n\"\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0188\n#\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\5$\u0196\n$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\5%\u019f\n%\3&\3&\7&\u01a3\n&\f&\16&\u01a6\13&\3&\7")
        buf.write("&\u01a9\n&\f&\16&\u01ac\13&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\5(\u01b8\n(\3)\3)\3)\3)\5)\u01be\n)\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3/\3/\5/\u01d7\n/\3/\3/\3\60\3\60\3\60\3\60\3\60\5\60")
        buf.write("\u01e0\n\60\3\60\3\60\3\60\3\60\3\60\5\60\u01e7\n\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\61\3\61\5\61\u01f0\n\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\5\62\u01f9\n\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\5\62\u0200\n\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\5\63\u0209\n\63\3\63\3\63\3\64\3\64\3")
        buf.write("\64\7\64\u0210\n\64\f\64\16\64\u0213\13\64\3\64\2\7\"")
        buf.write("$&(\60\65\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdf\2\7\6\2\4\4")
        buf.write("\13\13\r\r\17\17\4\2\26\26>>\4\2\3\38:\4\2\27\27>>\3\2")
        buf.write("\32\33\2\u022a\2i\3\2\2\2\4o\3\2\2\2\6}\3\2\2\2\b\u0083")
        buf.write("\3\2\2\2\n\u0086\3\2\2\2\f\u0090\3\2\2\2\16\u0097\3\2")
        buf.write("\2\2\20\u00a1\3\2\2\2\22\u00ae\3\2\2\2\24\u00b6\3\2\2")
        buf.write("\2\26\u00bd\3\2\2\2\30\u00bf\3\2\2\2\32\u00c3\3\2\2\2")
        buf.write("\34\u00c9\3\2\2\2\36\u00dc\3\2\2\2 \u00e7\3\2\2\2\"\u00e9")
        buf.write("\3\2\2\2$\u00f7\3\2\2\2&\u0105\3\2\2\2(\u0119\3\2\2\2")
        buf.write("*\u0127\3\2\2\2,\u012e\3\2\2\2.\u0135\3\2\2\2\60\u0137")
        buf.write("\3\2\2\2\62\u0145\3\2\2\2\64\u0152\3\2\2\2\66\u0154\3")
        buf.write("\2\2\28\u0158\3\2\2\2:\u0162\3\2\2\2<\u0164\3\2\2\2>\u016f")
        buf.write("\3\2\2\2@\u0173\3\2\2\2B\u017d\3\2\2\2D\u0187\3\2\2\2")
        buf.write("F\u0195\3\2\2\2H\u019e\3\2\2\2J\u01a0\3\2\2\2L\u01af\3")
        buf.write("\2\2\2N\u01b7\3\2\2\2P\u01bd\3\2\2\2R\u01bf\3\2\2\2T\u01c8")
        buf.write("\3\2\2\2V\u01ca\3\2\2\2X\u01cd\3\2\2\2Z\u01d0\3\2\2\2")
        buf.write("\\\u01d6\3\2\2\2^\u01da\3\2\2\2`\u01ea\3\2\2\2b\u01f3")
        buf.write("\3\2\2\2d\u0203\3\2\2\2f\u020c\3\2\2\2hj\5\4\3\2ih\3\2")
        buf.write("\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2lm\3\2\2\2mn\7\2\2\3")
        buf.write("n\3\3\2\2\2op\7\6\2\2ps\7>\2\2qr\7\n\2\2rt\7>\2\2sq\3")
        buf.write("\2\2\2st\3\2\2\2tu\3\2\2\2uw\7\60\2\2vx\5\6\4\2wv\3\2")
        buf.write("\2\2wx\3\2\2\2xy\3\2\2\2yz\7\61\2\2z\5\3\2\2\2{~\5\b\5")
        buf.write("\2|~\5\20\t\2}{\3\2\2\2}|\3\2\2\2~\177\3\2\2\2\177}\3")
        buf.write("\2\2\2\177\u0080\3\2\2\2\u0080\7\3\2\2\2\u0081\u0084\5")
        buf.write("\f\7\2\u0082\u0084\5\n\6\2\u0083\u0081\3\2\2\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\t\3\2\2\2\u0085\u0087\7\31\2\2\u0086\u0085")
        buf.write("\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u0089\7\30\2\2\u0089\u008a\5\26\f\2\u008a\u008b\7>\2")
        buf.write("\2\u008b\u008c\7-\2\2\u008c\u008d\5\36\20\2\u008d\u008e")
        buf.write("\7\64\2\2\u008e\13\3\2\2\2\u008f\u0091\7\31\2\2\u0090")
        buf.write("\u008f\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\u0093\5\16\b\2\u0093\u0094\7\65\2\2\u0094\u0095")
        buf.write("\5\26\f\2\u0095\u0096\7\64\2\2\u0096\r\3\2\2\2\u0097\u009c")
        buf.write("\7>\2\2\u0098\u0099\7\67\2\2\u0099\u009b\7>\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009a\3\2\2\2")
        buf.write("\u009c\u009d\3\2\2\2\u009d\17\3\2\2\2\u009e\u009c\3\2")
        buf.write("\2\2\u009f\u00a2\5\26\f\2\u00a0\u00a2\7\25\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a4\3\2\2\2\u00a3\u00a5\7\31\2\2\u00a4\u00a3\3\2\2")
        buf.write("\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7")
        buf.write("\7>\2\2\u00a7\u00a9\7\62\2\2\u00a8\u00aa\5\22\n\2\u00a9")
        buf.write("\u00a8\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00ac\7\63\2\2\u00ac\u00ad\5J&\2\u00ad\21\3\2\2")
        buf.write("\2\u00ae\u00b3\5\24\13\2\u00af\u00b0\7\64\2\2\u00b0\u00b2")
        buf.write("\5\24\13\2\u00b1\u00af\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\23\3\2\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b6\u00b7\5\16\b\2\u00b7\u00b8\7\65\2")
        buf.write("\2\u00b8\u00b9\5\26\f\2\u00b9\25\3\2\2\2\u00ba\u00be\5")
        buf.write("\30\r\2\u00bb\u00be\5\32\16\2\u00bc\u00be\5\34\17\2\u00bd")
        buf.write("\u00ba\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3\2\2\2")
        buf.write("\u00be\27\3\2\2\2\u00bf\u00c0\t\2\2\2\u00c0\31\3\2\2\2")
        buf.write("\u00c1\u00c4\7>\2\2\u00c2\u00c4\5\30\r\2\u00c3\u00c1\3")
        buf.write("\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6")
        buf.write("\7.\2\2\u00c6\u00c7\78\2\2\u00c7\u00c8\7/\2\2\u00c8\33")
        buf.write("\3\2\2\2\u00c9\u00ca\t\3\2\2\u00ca\35\3\2\2\2\u00cb\u00cc")
        buf.write("\5 \21\2\u00cc\u00cd\7$\2\2\u00cd\u00ce\5 \21\2\u00ce")
        buf.write("\u00dd\3\2\2\2\u00cf\u00d0\5 \21\2\u00d0\u00d1\7%\2\2")
        buf.write("\u00d1\u00d2\5 \21\2\u00d2\u00dd\3\2\2\2\u00d3\u00d4\5")
        buf.write(" \21\2\u00d4\u00d5\7&\2\2\u00d5\u00d6\5 \21\2\u00d6\u00dd")
        buf.write("\3\2\2\2\u00d7\u00d8\5 \21\2\u00d8\u00d9\7\'\2\2\u00d9")
        buf.write("\u00da\5 \21\2\u00da\u00dd\3\2\2\2\u00db\u00dd\5 \21\2")
        buf.write("\u00dc\u00cb\3\2\2\2\u00dc\u00cf\3\2\2\2\u00dc\u00d3\3")
        buf.write("\2\2\2\u00dc\u00d7\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\37")
        buf.write("\3\2\2\2\u00de\u00df\5\"\22\2\u00df\u00e0\7#\2\2\u00e0")
        buf.write("\u00e1\5\"\22\2\u00e1\u00e8\3\2\2\2\u00e2\u00e3\5\"\22")
        buf.write("\2\u00e3\u00e4\7\"\2\2\u00e4\u00e5\5\"\22\2\u00e5\u00e8")
        buf.write("\3\2\2\2\u00e6\u00e8\5\"\22\2\u00e7\u00de\3\2\2\2\u00e7")
        buf.write("\u00e2\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8!\3\2\2\2\u00e9")
        buf.write("\u00ea\b\22\1\2\u00ea\u00eb\5$\23\2\u00eb\u00f4\3\2\2")
        buf.write("\2\u00ec\u00ed\f\5\2\2\u00ed\u00ee\7(\2\2\u00ee\u00f3")
        buf.write("\5$\23\2\u00ef\u00f0\f\4\2\2\u00f0\u00f1\7)\2\2\u00f1")
        buf.write("\u00f3\5$\23\2\u00f2\u00ec\3\2\2\2\u00f2\u00ef\3\2\2\2")
        buf.write("\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3")
        buf.write("\2\2\2\u00f5#\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8")
        buf.write("\b\23\1\2\u00f8\u00f9\5&\24\2\u00f9\u0102\3\2\2\2\u00fa")
        buf.write("\u00fb\f\5\2\2\u00fb\u00fc\7\34\2\2\u00fc\u0101\5&\24")
        buf.write("\2\u00fd\u00fe\f\4\2\2\u00fe\u00ff\7\35\2\2\u00ff\u0101")
        buf.write("\5&\24\2\u0100\u00fa\3\2\2\2\u0100\u00fd\3\2\2\2\u0101")
        buf.write("\u0104\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2")
        buf.write("\u0103%\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0106\b\24\1")
        buf.write("\2\u0106\u0107\5(\25\2\u0107\u0116\3\2\2\2\u0108\u0109")
        buf.write("\f\7\2\2\u0109\u010a\7\36\2\2\u010a\u0115\5(\25\2\u010b")
        buf.write("\u010c\f\6\2\2\u010c\u010d\7 \2\2\u010d\u0115\5(\25\2")
        buf.write("\u010e\u010f\f\5\2\2\u010f\u0110\7\37\2\2\u0110\u0115")
        buf.write("\5(\25\2\u0111\u0112\f\4\2\2\u0112\u0113\7!\2\2\u0113")
        buf.write("\u0115\5(\25\2\u0114\u0108\3\2\2\2\u0114\u010b\3\2\2\2")
        buf.write("\u0114\u010e\3\2\2\2\u0114\u0111\3\2\2\2\u0115\u0118\3")
        buf.write("\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\'")
        buf.write("\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a\b\25\1\2\u011a")
        buf.write("\u011b\5*\26\2\u011b\u0121\3\2\2\2\u011c\u011d\f\4\2\2")
        buf.write("\u011d\u011e\7+\2\2\u011e\u0120\5*\26\2\u011f\u011c\3")
        buf.write("\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f\3\2\2\2\u0121\u0122")
        buf.write("\3\2\2\2\u0122)\3\2\2\2\u0123\u0121\3\2\2\2\u0124\u0125")
        buf.write("\7*\2\2\u0125\u0128\5*\26\2\u0126\u0128\5,\27\2\u0127")
        buf.write("\u0124\3\2\2\2\u0127\u0126\3\2\2\2\u0128+\3\2\2\2\u0129")
        buf.write("\u012a\7\34\2\2\u012a\u012f\5,\27\2\u012b\u012c\7\35\2")
        buf.write("\2\u012c\u012f\5,\27\2\u012d\u012f\5.\30\2\u012e\u0129")
        buf.write("\3\2\2\2\u012e\u012b\3\2\2\2\u012e\u012d\3\2\2\2\u012f")
        buf.write("-\3\2\2\2\u0130\u0131\7.\2\2\u0131\u0132\5\36\20\2\u0132")
        buf.write("\u0133\7/\2\2\u0133\u0136\3\2\2\2\u0134\u0136\5\60\31")
        buf.write("\2\u0135\u0130\3\2\2\2\u0135\u0134\3\2\2\2\u0136/\3\2")
        buf.write("\2\2\u0137\u0138\b\31\1\2\u0138\u0139\5\62\32\2\u0139")
        buf.write("\u013f\3\2\2\2\u013a\u013b\f\4\2\2\u013b\u013c\7\66\2")
        buf.write("\2\u013c\u013e\5\62\32\2\u013d\u013a\3\2\2\2\u013e\u0141")
        buf.write("\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write("\61\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0143\7\16\2\2\u0143")
        buf.write("\u0146\5\62\32\2\u0144\u0146\5\64\33\2\u0145\u0142\3\2")
        buf.write("\2\2\u0145\u0144\3\2\2\2\u0146\63\3\2\2\2\u0147\u0153")
        buf.write("\7>\2\2\u0148\u0153\5\66\34\2\u0149\u0153\58\35\2\u014a")
        buf.write("\u0153\5:\36\2\u014b\u0153\5@!\2\u014c\u0153\7\27\2\2")
        buf.write("\u014d\u014f\7\62\2\2\u014e\u0150\5\36\20\2\u014f\u014e")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0153\7\63\2\2\u0152\u0147\3\2\2\2\u0152\u0148\3\2\2")
        buf.write("\2\u0152\u0149\3\2\2\2\u0152\u014a\3\2\2\2\u0152\u014b")
        buf.write("\3\2\2\2\u0152\u014c\3\2\2\2\u0152\u014d\3\2\2\2\u0153")
        buf.write("\65\3\2\2\2\u0154\u0155\t\4\2\2\u0155\67\3\2\2\2\u0156")
        buf.write("\u0159\7>\2\2\u0157\u0159\5:\36\2\u0158\u0156\3\2\2\2")
        buf.write("\u0158\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b\7")
        buf.write(".\2\2\u015b\u015c\5\36\20\2\u015c\u015d\7/\2\2\u015d9")
        buf.write("\3\2\2\2\u015e\u0163\5<\37\2\u015f\u0163\5> \2\u0160\u0163")
        buf.write("\5^\60\2\u0161\u0163\5`\61\2\u0162\u015e\3\2\2\2\u0162")
        buf.write("\u015f\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0161\3\2\2\2")
        buf.write("\u0163;\3\2\2\2\u0164\u0165\t\5\2\2\u0165\u0166\7\66\2")
        buf.write("\2\u0166\u0167\7>\2\2\u0167\u0169\7\62\2\2\u0168\u016a")
        buf.write("\5f\64\2\u0169\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u016c\7\63\2\2\u016c\u016d\7\66\2")
        buf.write("\2\u016d\u016e\7>\2\2\u016e=\3\2\2\2\u016f\u0170\t\5\2")
        buf.write("\2\u0170\u0171\7\66\2\2\u0171\u0172\7>\2\2\u0172?\3\2")
        buf.write("\2\2\u0173\u0174\7\16\2\2\u0174\u0175\7>\2\2\u0175\u0177")
        buf.write("\7\62\2\2\u0176\u0178\5f\64\2\u0177\u0176\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a\7\63\2")
        buf.write("\2\u017aA\3\2\2\2\u017b\u017e\5D#\2\u017c\u017e\5F$\2")
        buf.write("\u017d\u017b\3\2\2\2\u017d\u017c\3\2\2\2\u017eC\3\2\2")
        buf.write("\2\u017f\u0180\7\f\2\2\u0180\u0181\5\36\20\2\u0181\u0182")
        buf.write("\7\20\2\2\u0182\u0183\5D#\2\u0183\u0184\7\t\2\2\u0184")
        buf.write("\u0185\5D#\2\u0185\u0188\3\2\2\2\u0186\u0188\5H%\2\u0187")
        buf.write("\u017f\3\2\2\2\u0187\u0186\3\2\2\2\u0188E\3\2\2\2\u0189")
        buf.write("\u018a\7\f\2\2\u018a\u018b\5\36\20\2\u018b\u018c\7\20")
        buf.write("\2\2\u018c\u018d\5B\"\2\u018d\u0196\3\2\2\2\u018e\u018f")
        buf.write("\7\f\2\2\u018f\u0190\5\36\20\2\u0190\u0191\7\20\2\2\u0191")
        buf.write("\u0192\5D#\2\u0192\u0193\7\t\2\2\u0193\u0194\5F$\2\u0194")
        buf.write("\u0196\3\2\2\2\u0195\u0189\3\2\2\2\u0195\u018e\3\2\2\2")
        buf.write("\u0196G\3\2\2\2\u0197\u019f\5J&\2\u0198\u019f\5L\'\2\u0199")
        buf.write("\u019f\5R*\2\u019a\u019f\5V,\2\u019b\u019f\5X-\2\u019c")
        buf.write("\u019f\5Z.\2\u019d\u019f\5\\/\2\u019e\u0197\3\2\2\2\u019e")
        buf.write("\u0198\3\2\2\2\u019e\u0199\3\2\2\2\u019e\u019a\3\2\2\2")
        buf.write("\u019e\u019b\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019d\3")
        buf.write("\2\2\2\u019fI\3\2\2\2\u01a0\u01a4\7\60\2\2\u01a1\u01a3")
        buf.write("\5\b\5\2\u01a2\u01a1\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01aa\3\2\2\2")
        buf.write("\u01a6\u01a4\3\2\2\2\u01a7\u01a9\5B\"\2\u01a8\u01a7\3")
        buf.write("\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab")
        buf.write("\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad")
        buf.write("\u01ae\7\61\2\2\u01aeK\3\2\2\2\u01af\u01b0\5N(\2\u01b0")
        buf.write("\u01b1\7,\2\2\u01b1\u01b2\5\36\20\2\u01b2\u01b3\7\64\2")
        buf.write("\2\u01b3M\3\2\2\2\u01b4\u01b8\5P)\2\u01b5\u01b8\5\f\7")
        buf.write("\2\u01b6\u01b8\58\35\2\u01b7\u01b4\3\2\2\2\u01b7\u01b5")
        buf.write("\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8O\3\2\2\2\u01b9\u01ba")
        buf.write("\7\27\2\2\u01ba\u01bb\7\66\2\2\u01bb\u01be\7>\2\2\u01bc")
        buf.write("\u01be\7>\2\2\u01bd\u01b9\3\2\2\2\u01bd\u01bc\3\2\2\2")
        buf.write("\u01beQ\3\2\2\2\u01bf\u01c0\7\21\2\2\u01c0\u01c1\5T+\2")
        buf.write("\u01c1\u01c2\7,\2\2\u01c2\u01c3\5\36\20\2\u01c3\u01c4")
        buf.write("\t\6\2\2\u01c4\u01c5\5\36\20\2\u01c5\u01c6\7\b\2\2\u01c6")
        buf.write("\u01c7\5B\"\2\u01c7S\3\2\2\2\u01c8\u01c9\7>\2\2\u01c9")
        buf.write("U\3\2\2\2\u01ca\u01cb\7\5\2\2\u01cb\u01cc\7\64\2\2\u01cc")
        buf.write("W\3\2\2\2\u01cd\u01ce\7\7\2\2\u01ce\u01cf\7\64\2\2\u01cf")
        buf.write("Y\3\2\2\2\u01d0\u01d1\7\22\2\2\u01d1\u01d2\5\36\20\2\u01d2")
        buf.write("\u01d3\7\64\2\2\u01d3[\3\2\2\2\u01d4\u01d7\5b\62\2\u01d5")
        buf.write("\u01d7\5d\63\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u01d9\7\64\2\2\u01d9]\3\2\2")
        buf.write("\2\u01da\u01db\t\5\2\2\u01db\u01dc\7\66\2\2\u01dc\u01dd")
        buf.write("\7>\2\2\u01dd\u01df\7\62\2\2\u01de\u01e0\5f\64\2\u01df")
        buf.write("\u01de\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1\u01e2\7\63\2\2\u01e2\u01e3\7\66\2\2\u01e3\u01e4")
        buf.write("\7>\2\2\u01e4\u01e6\7\62\2\2\u01e5\u01e7\5f\64\2\u01e6")
        buf.write("\u01e5\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e8\u01e9\7\63\2\2\u01e9_\3\2\2\2\u01ea\u01eb\t\5\2")
        buf.write("\2\u01eb\u01ec\7\66\2\2\u01ec\u01ed\7>\2\2\u01ed\u01ef")
        buf.write("\7\62\2\2\u01ee\u01f0\5f\64\2\u01ef\u01ee\3\2\2\2\u01ef")
        buf.write("\u01f0\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\7\63\2")
        buf.write("\2\u01f2a\3\2\2\2\u01f3\u01f4\t\5\2\2\u01f4\u01f5\7\66")
        buf.write("\2\2\u01f5\u01f6\7>\2\2\u01f6\u01f8\7\62\2\2\u01f7\u01f9")
        buf.write("\5f\64\2\u01f8\u01f7\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9")
        buf.write("\u01fa\3\2\2\2\u01fa\u01fb\7\63\2\2\u01fb\u01fc\7\66\2")
        buf.write("\2\u01fc\u01fd\7>\2\2\u01fd\u01ff\7\62\2\2\u01fe\u0200")
        buf.write("\5f\64\2\u01ff\u01fe\3\2\2\2\u01ff\u0200\3\2\2\2\u0200")
        buf.write("\u0201\3\2\2\2\u0201\u0202\7\63\2\2\u0202c\3\2\2\2\u0203")
        buf.write("\u0204\t\5\2\2\u0204\u0205\7\66\2\2\u0205\u0206\7>\2\2")
        buf.write("\u0206\u0208\7\62\2\2\u0207\u0209\5f\64\2\u0208\u0207")
        buf.write("\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020a\3\2\2\2\u020a")
        buf.write("\u020b\7\63\2\2\u020be\3\2\2\2\u020c\u0211\5\36\20\2\u020d")
        buf.write("\u020e\7\67\2\2\u020e\u0210\5\36\20\2\u020f\u020d\3\2")
        buf.write("\2\2\u0210\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212")
        buf.write("\3\2\2\2\u0212g\3\2\2\2\u0213\u0211\3\2\2\2\65ksw}\177")
        buf.write("\u0083\u0086\u0090\u009c\u00a1\u00a4\u00a9\u00b3\u00bd")
        buf.write("\u00c3\u00dc\u00e7\u00f2\u00f4\u0100\u0102\u0114\u0116")
        buf.write("\u0121\u0127\u012e\u0135\u013f\u0145\u014f\u0152\u0158")
        buf.write("\u0162\u0169\u0177\u017d\u0187\u0195\u019e\u01a4\u01aa")
        buf.write("\u01b7\u01bd\u01d6\u01df\u01e6\u01ef\u01f8\u01ff\u0208")
        buf.write("\u0211")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'boolean'", "'break'", "'class'", 
                     "'continue'", "'do'", "'else'", "'extends'", "'float'", 
                     "'if'", "'int'", "'new'", "'string'", "'then'", "'for'", 
                     "'return'", "'true'", "'false'", "'void'", "'nil'", 
                     "'this'", "'final'", "'static'", "'to'", "'downto'", 
                     "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
                     "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", 
                     "'!'", "'^'", "':='", "'='", "'['", "']'", "'{'", "'}'", 
                     "'('", "')'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "BOOLLIT", "BOOLEAN", "BREAK", "CLASS", 
                      "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", "IF", 
                      "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", "TRUE", 
                      "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", 
                      "TO", "DOWNTO", "ADD", "SUB", "MUL", "FLOATDIV", "INTDIV", 
                      "MOD", "NOTEQ", "EQ", "LESS", "GREATER", "LESSEQ", 
                      "GREATEREQ", "OR", "AND", "NOT", "CONCAT", "ASSIGN", 
                      "OP_BANG", "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMICOLONE", 
                      "COLON", "DOT", "COMMA", "INTEGERLIT", "FLOATLIT", 
                      "STRINGLIT", "WS", "BLOCKCOMMENT", "LINECOMMENT", 
                      "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_list_of_members = 2
    RULE_attribute = 3
    RULE_constant_decl = 4
    RULE_variable_decl = 5
    RULE_id_list = 6
    RULE_method = 7
    RULE_list_of_para = 8
    RULE_para = 9
    RULE_type_lit = 10
    RULE_primitive_type = 11
    RULE_array_type = 12
    RULE_class_type = 13
    RULE_exp = 14
    RULE_exp1 = 15
    RULE_exp2 = 16
    RULE_exp3 = 17
    RULE_exp4 = 18
    RULE_exp5 = 19
    RULE_exp6 = 20
    RULE_exp7 = 21
    RULE_exp8 = 22
    RULE_exp9 = 23
    RULE_exp10 = 24
    RULE_exp11 = 25
    RULE_literals = 26
    RULE_index_exp = 27
    RULE_member_access = 28
    RULE_instance_attribute = 29
    RULE_static_attribute = 30
    RULE_object_creation = 31
    RULE_statement = 32
    RULE_match_state = 33
    RULE_unmatch_state = 34
    RULE_other_state = 35
    RULE_block_state = 36
    RULE_assign_state = 37
    RULE_lhs = 38
    RULE_local_variable = 39
    RULE_for_state = 40
    RULE_scalar_variable = 41
    RULE_break_state = 42
    RULE_continue_state = 43
    RULE_return_state = 44
    RULE_method_invo_state = 45
    RULE_instance_method = 46
    RULE_static_method = 47
    RULE_instance_method_state = 48
    RULE_static_method_state = 49
    RULE_list_exp = 50

    ruleNames =  [ "program", "class_decl", "list_of_members", "attribute", 
                   "constant_decl", "variable_decl", "id_list", "method", 
                   "list_of_para", "para", "type_lit", "primitive_type", 
                   "array_type", "class_type", "exp", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "exp8", "exp9", "exp10", 
                   "exp11", "literals", "index_exp", "member_access", "instance_attribute", 
                   "static_attribute", "object_creation", "statement", "match_state", 
                   "unmatch_state", "other_state", "block_state", "assign_state", 
                   "lhs", "local_variable", "for_state", "scalar_variable", 
                   "break_state", "continue_state", "return_state", "method_invo_state", 
                   "instance_method", "static_method", "instance_method_state", 
                   "static_method_state", "list_exp" ]

    EOF = Token.EOF
    BOOLLIT=1
    BOOLEAN=2
    BREAK=3
    CLASS=4
    CONTINUE=5
    DO=6
    ELSE=7
    EXTENDS=8
    FLOAT=9
    IF=10
    INT=11
    NEW=12
    STRING=13
    THEN=14
    FOR=15
    RETURN=16
    TRUE=17
    FALSE=18
    VOID=19
    NIL=20
    THIS=21
    FINAL=22
    STATIC=23
    TO=24
    DOWNTO=25
    ADD=26
    SUB=27
    MUL=28
    FLOATDIV=29
    INTDIV=30
    MOD=31
    NOTEQ=32
    EQ=33
    LESS=34
    GREATER=35
    LESSEQ=36
    GREATEREQ=37
    OR=38
    AND=39
    NOT=40
    CONCAT=41
    ASSIGN=42
    OP_BANG=43
    LSB=44
    RSB=45
    LP=46
    RP=47
    LB=48
    RB=49
    SEMICOLONE=50
    COLON=51
    DOT=52
    COMMA=53
    INTEGERLIT=54
    FLOATLIT=55
    STRINGLIT=56
    WS=57
    BLOCKCOMMENT=58
    LINECOMMENT=59
    ID=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_declContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.class_decl()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 107
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def list_of_members(self):
            return self.getTypedRuleContext(BKOOLParser.List_of_membersContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = BKOOLParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(BKOOLParser.CLASS)
            self.state = 110
            self.match(BKOOLParser.ID)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 111
                self.match(BKOOLParser.EXTENDS)
                self.state = 112
                self.match(BKOOLParser.ID)


            self.state = 115
            self.match(BKOOLParser.LP)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 116
                self.list_of_members()


            self.state = 119
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_membersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.AttributeContext,i)


        def method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MethodContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MethodContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_of_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_members" ):
                return visitor.visitList_of_members(self)
            else:
                return visitor.visitChildren(self)




    def list_of_members(self):

        localctx = BKOOLParser.List_of_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list_of_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 123
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 121
                    self.attribute()
                    pass

                elif la_ == 2:
                    self.state = 122
                    self.method()
                    pass


                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Variable_declContext,0)


        def constant_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Constant_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = BKOOLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.constant_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def type_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Type_litContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def OP_BANG(self):
            return self.getToken(BKOOLParser.OP_BANG, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMICOLONE(self):
            return self.getToken(BKOOLParser.SEMICOLONE, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_constant_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant_decl" ):
                return visitor.visitConstant_decl(self)
            else:
                return visitor.visitChildren(self)




    def constant_decl(self):

        localctx = BKOOLParser.Constant_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constant_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 131
                self.match(BKOOLParser.STATIC)


            self.state = 134
            self.match(BKOOLParser.FINAL)
            self.state = 135
            self.type_lit()
            self.state = 136
            self.match(BKOOLParser.ID)
            self.state = 137
            self.match(BKOOLParser.OP_BANG)
            self.state = 138
            self.exp()
            self.state = 139
            self.match(BKOOLParser.SEMICOLONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(BKOOLParser.Id_listContext,0)


        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def type_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Type_litContext,0)


        def SEMICOLONE(self):
            return self.getToken(BKOOLParser.SEMICOLONE, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = BKOOLParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 141
                self.match(BKOOLParser.STATIC)


            self.state = 144
            self.id_list()
            self.state = 145
            self.match(BKOOLParser.COLON)
            self.state = 146
            self.type_lit()
            self.state = 147
            self.match(BKOOLParser.SEMICOLONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = BKOOLParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(BKOOLParser.ID)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 150
                self.match(BKOOLParser.COMMA)
                self.state = 151
                self.match(BKOOLParser.ID)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def block_state(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stateContext,0)


        def type_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Type_litContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def list_of_para(self):
            return self.getTypedRuleContext(BKOOLParser.List_of_paraContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = BKOOLParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 157
                self.type_lit()

            elif la_ == 2:
                self.state = 158
                self.match(BKOOLParser.VOID)


            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 161
                self.match(BKOOLParser.STATIC)


            self.state = 164
            self.match(BKOOLParser.ID)
            self.state = 165
            self.match(BKOOLParser.LB)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ID:
                self.state = 166
                self.list_of_para()


            self.state = 169
            self.match(BKOOLParser.RB)
            self.state = 170
            self.block_state()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_paraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParaContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParaContext,i)


        def SEMICOLONE(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMICOLONE)
            else:
                return self.getToken(BKOOLParser.SEMICOLONE, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_list_of_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_para" ):
                return visitor.visitList_of_para(self)
            else:
                return visitor.visitChildren(self)




    def list_of_para(self):

        localctx = BKOOLParser.List_of_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_of_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.para()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SEMICOLONE:
                self.state = 173
                self.match(BKOOLParser.SEMICOLONE)
                self.state = 174
                self.para()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(BKOOLParser.Id_listContext,0)


        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def type_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Type_litContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = BKOOLParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.id_list()
            self.state = 181
            self.match(BKOOLParser.COLON)
            self.state = 182
            self.type_lit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_type_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_lit" ):
                return visitor.visitType_lit(self)
            else:
                return visitor.visitChildren(self)




    def type_lit(self):

        localctx = BKOOLParser.Type_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type_lit)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.array_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.class_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = BKOOLParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING))) != 0)):
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


    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTEGERLIT(self):
            return self.getToken(BKOOLParser.INTEGERLIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.state = 191
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING]:
                self.state = 192
                self.primitive_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 195
            self.match(BKOOLParser.LSB)
            self.state = 196
            self.match(BKOOLParser.INTEGERLIT)
            self.state = 197
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = BKOOLParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_class_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.NIL or _la==BKOOLParser.ID):
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


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp1Context,i)


        def LESS(self):
            return self.getToken(BKOOLParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKOOLParser.GREATER, 0)

        def LESSEQ(self):
            return self.getToken(BKOOLParser.LESSEQ, 0)

        def GREATEREQ(self):
            return self.getToken(BKOOLParser.GREATEREQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.exp1()
                self.state = 202
                self.match(BKOOLParser.LESS)
                self.state = 203
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.exp1()
                self.state = 206
                self.match(BKOOLParser.GREATER)
                self.state = 207
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.exp1()
                self.state = 210
                self.match(BKOOLParser.LESSEQ)
                self.state = 211
                self.exp1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 213
                self.exp1()
                self.state = 214
                self.match(BKOOLParser.GREATEREQ)
                self.state = 215
                self.exp1()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 217
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp2Context,i)


        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def NOTEQ(self):
            return self.getToken(BKOOLParser.NOTEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp1)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.exp2(0)
                self.state = 221
                self.match(BKOOLParser.EQ)
                self.state = 222
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.exp2(0)
                self.state = 225
                self.match(BKOOLParser.NOTEQ)
                self.state = 226
                self.exp2(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 240
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 234
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 235
                        self.match(BKOOLParser.OR)
                        self.state = 236
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 237
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 238
                        self.match(BKOOLParser.AND)
                        self.state = 239
                        self.exp3(0)
                        pass

             
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 256
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 254
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 248
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 249
                        self.match(BKOOLParser.ADD)
                        self.state = 250
                        self.exp4(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 251
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 252
                        self.match(BKOOLParser.SUB)
                        self.state = 253
                        self.exp4(0)
                        pass

             
                self.state = 258
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def INTDIV(self):
            return self.getToken(BKOOLParser.INTDIV, 0)

        def FLOATDIV(self):
            return self.getToken(BKOOLParser.FLOATDIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 274
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 262
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 263
                        self.match(BKOOLParser.MUL)
                        self.state = 264
                        self.exp5(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 265
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 266
                        self.match(BKOOLParser.INTDIV)
                        self.state = 267
                        self.exp5(0)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 268
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 269
                        self.match(BKOOLParser.FLOATDIV)
                        self.state = 270
                        self.exp5(0)
                        pass

                    elif la_ == 4:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 271
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 272
                        self.match(BKOOLParser.MOD)
                        self.state = 273
                        self.exp5(0)
                        pass

             
                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 287
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 282
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 283
                    self.match(BKOOLParser.CONCAT)
                    self.state = 284
                    self.exp6() 
                self.state = 289
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp6)
        try:
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(BKOOLParser.NOT)
                self.state = 291
                self.exp6()
                pass
            elif token in [BKOOLParser.BOOLLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.LSB, BKOOLParser.LB, BKOOLParser.INTEGERLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.exp7()
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


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp7)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(BKOOLParser.ADD)
                self.state = 296
                self.exp7()
                pass
            elif token in [BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.match(BKOOLParser.SUB)
                self.state = 298
                self.exp7()
                pass
            elif token in [BKOOLParser.BOOLLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.LSB, BKOOLParser.LB, BKOOLParser.INTEGERLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 299
                self.exp8()
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


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = BKOOLParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp8)
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LSB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(BKOOLParser.LSB)
                self.state = 303
                self.exp()
                self.state = 304
                self.match(BKOOLParser.RSB)
                pass
            elif token in [BKOOLParser.BOOLLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.INTEGERLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.exp9(0)
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


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 317
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 312
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 313
                    self.match(BKOOLParser.DOT)
                    self.state = 314
                    self.exp10() 
                self.state = 319
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def exp11(self):
            return self.getTypedRuleContext(BKOOLParser.Exp11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exp10)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(BKOOLParser.NEW)
                self.state = 321
                self.exp10()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.exp11()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp11Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def literals(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralsContext,0)


        def index_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Index_expContext,0)


        def member_access(self):
            return self.getTypedRuleContext(BKOOLParser.Member_accessContext,0)


        def object_creation(self):
            return self.getTypedRuleContext(BKOOLParser.Object_creationContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = BKOOLParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp11)
        self._la = 0 # Token type
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.literals()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.index_exp()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                self.member_access()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 329
                self.object_creation()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 330
                self.match(BKOOLParser.THIS)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 331
                self.match(BKOOLParser.LB)
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LSB) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTEGERLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 332
                    self.exp()


                self.state = 335
                self.match(BKOOLParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGERLIT(self):
            return self.getToken(BKOOLParser.INTEGERLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(BKOOLParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = BKOOLParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.INTEGERLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT))) != 0)):
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


    class Index_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def member_access(self):
            return self.getTypedRuleContext(BKOOLParser.Member_accessContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_index_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_exp" ):
                return visitor.visitIndex_exp(self)
            else:
                return visitor.visitChildren(self)




    def index_exp(self):

        localctx = BKOOLParser.Index_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_index_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 340
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 341
                self.member_access()
                pass


            self.state = 344
            self.match(BKOOLParser.LSB)
            self.state = 345
            self.exp()
            self.state = 346
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Instance_attributeContext,0)


        def static_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Static_attributeContext,0)


        def instance_method(self):
            return self.getTypedRuleContext(BKOOLParser.Instance_methodContext,0)


        def static_method(self):
            return self.getTypedRuleContext(BKOOLParser.Static_methodContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access" ):
                return visitor.visitMember_access(self)
            else:
                return visitor.visitChildren(self)




    def member_access(self):

        localctx = BKOOLParser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_member_access)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.instance_attribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.static_attribute()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
                self.instance_method()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 351
                self.static_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_attributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.DOT)
            else:
                return self.getToken(BKOOLParser.DOT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def list_exp(self):
            return self.getTypedRuleContext(BKOOLParser.List_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instance_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_attribute" ):
                return visitor.visitInstance_attribute(self)
            else:
                return visitor.visitChildren(self)




    def instance_attribute(self):

        localctx = BKOOLParser.Instance_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_instance_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 355
            self.match(BKOOLParser.DOT)
            self.state = 356
            self.match(BKOOLParser.ID)
            self.state = 357
            self.match(BKOOLParser.LB)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LSB) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTEGERLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 358
                self.list_exp()


            self.state = 361
            self.match(BKOOLParser.RB)
            self.state = 362
            self.match(BKOOLParser.DOT)
            self.state = 363
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_attributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_static_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_attribute" ):
                return visitor.visitStatic_attribute(self)
            else:
                return visitor.visitChildren(self)




    def static_attribute(self):

        localctx = BKOOLParser.Static_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_static_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 366
            self.match(BKOOLParser.DOT)
            self.state = 367
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_creationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def list_exp(self):
            return self.getTypedRuleContext(BKOOLParser.List_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_object_creation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_creation" ):
                return visitor.visitObject_creation(self)
            else:
                return visitor.visitChildren(self)




    def object_creation(self):

        localctx = BKOOLParser.Object_creationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_object_creation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(BKOOLParser.NEW)
            self.state = 370
            self.match(BKOOLParser.ID)
            self.state = 371
            self.match(BKOOLParser.LB)
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LSB) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTEGERLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 372
                self.list_exp()


            self.state = 375
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def match_state(self):
            return self.getTypedRuleContext(BKOOLParser.Match_stateContext,0)


        def unmatch_state(self):
            return self.getTypedRuleContext(BKOOLParser.Unmatch_stateContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_statement)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match_state()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.unmatch_state()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Match_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def match_state(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Match_stateContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Match_stateContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def other_state(self):
            return self.getTypedRuleContext(BKOOLParser.Other_stateContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_match_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatch_state" ):
                return visitor.visitMatch_state(self)
            else:
                return visitor.visitChildren(self)




    def match_state(self):

        localctx = BKOOLParser.Match_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_match_state)
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(BKOOLParser.IF)
                self.state = 382
                self.exp()
                self.state = 383
                self.match(BKOOLParser.THEN)
                self.state = 384
                self.match_state()
                self.state = 385
                self.match(BKOOLParser.ELSE)
                self.state = 386
                self.match_state()
                pass
            elif token in [BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.STATIC, BKOOLParser.LP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.other_state()
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


    class Unmatch_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def match_state(self):
            return self.getTypedRuleContext(BKOOLParser.Match_stateContext,0)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def unmatch_state(self):
            return self.getTypedRuleContext(BKOOLParser.Unmatch_stateContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_unmatch_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnmatch_state" ):
                return visitor.visitUnmatch_state(self)
            else:
                return visitor.visitChildren(self)




    def unmatch_state(self):

        localctx = BKOOLParser.Unmatch_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_unmatch_state)
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.match(BKOOLParser.IF)
                self.state = 392
                self.exp()
                self.state = 393
                self.match(BKOOLParser.THEN)
                self.state = 394
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.match(BKOOLParser.IF)
                self.state = 397
                self.exp()
                self.state = 398
                self.match(BKOOLParser.THEN)
                self.state = 399
                self.match_state()
                self.state = 400
                self.match(BKOOLParser.ELSE)
                self.state = 401
                self.unmatch_state()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Other_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_state(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stateContext,0)


        def assign_state(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stateContext,0)


        def for_state(self):
            return self.getTypedRuleContext(BKOOLParser.For_stateContext,0)


        def break_state(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stateContext,0)


        def continue_state(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_stateContext,0)


        def return_state(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stateContext,0)


        def method_invo_state(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invo_stateContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_other_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOther_state" ):
                return visitor.visitOther_state(self)
            else:
                return visitor.visitChildren(self)




    def other_state(self):

        localctx = BKOOLParser.Other_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_other_state)
        try:
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.block_state()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.assign_state()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 407
                self.for_state()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 408
                self.break_state()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 409
                self.continue_state()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 410
                self.return_state()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 411
                self.method_invo_state()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.AttributeContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_state" ):
                return visitor.visitBlock_state(self)
            else:
                return visitor.visitChildren(self)




    def block_state(self):

        localctx = BKOOLParser.Block_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_block_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(BKOOLParser.LP)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 415
                    self.attribute() 
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 421
                self.statement()
                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 427
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMICOLONE(self):
            return self.getToken(BKOOLParser.SEMICOLONE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_state" ):
                return visitor.visitAssign_state(self)
            else:
                return visitor.visitChildren(self)




    def assign_state(self):

        localctx = BKOOLParser.Assign_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assign_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.lhs()
            self.state = 430
            self.match(BKOOLParser.ASSIGN)
            self.state = 431
            self.exp()
            self.state = 432
            self.match(BKOOLParser.SEMICOLONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_variable(self):
            return self.getTypedRuleContext(BKOOLParser.Local_variableContext,0)


        def variable_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Variable_declContext,0)


        def index_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Index_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_lhs)
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.local_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.variable_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 436
                self.index_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_local_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_variable" ):
                return visitor.visitLocal_variable(self)
            else:
                return visitor.visitChildren(self)




    def local_variable(self):

        localctx = BKOOLParser.Local_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_local_variable)
        try:
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.match(BKOOLParser.THIS)
                self.state = 440
                self.match(BKOOLParser.DOT)
                self.state = 441
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.match(BKOOLParser.ID)
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


    class For_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def scalar_variable(self):
            return self.getTypedRuleContext(BKOOLParser.Scalar_variableContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_state" ):
                return visitor.visitFor_state(self)
            else:
                return visitor.visitChildren(self)




    def for_state(self):

        localctx = BKOOLParser.For_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_for_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(BKOOLParser.FOR)
            self.state = 446
            self.scalar_variable()
            self.state = 447
            self.match(BKOOLParser.ASSIGN)
            self.state = 448
            self.exp()
            self.state = 449
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 450
            self.exp()
            self.state = 451
            self.match(BKOOLParser.DO)
            self.state = 452
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scalar_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_variable" ):
                return visitor.visitScalar_variable(self)
            else:
                return visitor.visitChildren(self)




    def scalar_variable(self):

        localctx = BKOOLParser.Scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_scalar_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMICOLONE(self):
            return self.getToken(BKOOLParser.SEMICOLONE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_state" ):
                return visitor.visitBreak_state(self)
            else:
                return visitor.visitChildren(self)




    def break_state(self):

        localctx = BKOOLParser.Break_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_break_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(BKOOLParser.BREAK)
            self.state = 457
            self.match(BKOOLParser.SEMICOLONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMICOLONE(self):
            return self.getToken(BKOOLParser.SEMICOLONE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_state" ):
                return visitor.visitContinue_state(self)
            else:
                return visitor.visitChildren(self)




    def continue_state(self):

        localctx = BKOOLParser.Continue_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_continue_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(BKOOLParser.CONTINUE)
            self.state = 460
            self.match(BKOOLParser.SEMICOLONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMICOLONE(self):
            return self.getToken(BKOOLParser.SEMICOLONE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_state" ):
                return visitor.visitReturn_state(self)
            else:
                return visitor.visitChildren(self)




    def return_state(self):

        localctx = BKOOLParser.Return_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_return_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(BKOOLParser.RETURN)
            self.state = 463
            self.exp()
            self.state = 464
            self.match(BKOOLParser.SEMICOLONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invo_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLONE(self):
            return self.getToken(BKOOLParser.SEMICOLONE, 0)

        def instance_method_state(self):
            return self.getTypedRuleContext(BKOOLParser.Instance_method_stateContext,0)


        def static_method_state(self):
            return self.getTypedRuleContext(BKOOLParser.Static_method_stateContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invo_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invo_state" ):
                return visitor.visitMethod_invo_state(self)
            else:
                return visitor.visitChildren(self)




    def method_invo_state(self):

        localctx = BKOOLParser.Method_invo_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_method_invo_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 466
                self.instance_method_state()
                pass

            elif la_ == 2:
                self.state = 467
                self.static_method_state()
                pass


            self.state = 470
            self.match(BKOOLParser.SEMICOLONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.DOT)
            else:
                return self.getToken(BKOOLParser.DOT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.LB)
            else:
                return self.getToken(BKOOLParser.LB, i)

        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.RB)
            else:
                return self.getToken(BKOOLParser.RB, i)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def list_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.List_expContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.List_expContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instance_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method" ):
                return visitor.visitInstance_method(self)
            else:
                return visitor.visitChildren(self)




    def instance_method(self):

        localctx = BKOOLParser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_instance_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 473
            self.match(BKOOLParser.DOT)
            self.state = 474
            self.match(BKOOLParser.ID)
            self.state = 475
            self.match(BKOOLParser.LB)
            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LSB) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTEGERLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 476
                self.list_exp()


            self.state = 479
            self.match(BKOOLParser.RB)
            self.state = 480
            self.match(BKOOLParser.DOT)
            self.state = 481
            self.match(BKOOLParser.ID)
            self.state = 482
            self.match(BKOOLParser.LB)
            self.state = 484
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LSB) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTEGERLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 483
                self.list_exp()


            self.state = 486
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def list_exp(self):
            return self.getTypedRuleContext(BKOOLParser.List_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_static_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method" ):
                return visitor.visitStatic_method(self)
            else:
                return visitor.visitChildren(self)




    def static_method(self):

        localctx = BKOOLParser.Static_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_static_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 489
            self.match(BKOOLParser.DOT)
            self.state = 490
            self.match(BKOOLParser.ID)
            self.state = 491
            self.match(BKOOLParser.LB)
            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LSB) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTEGERLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 492
                self.list_exp()


            self.state = 495
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.DOT)
            else:
                return self.getToken(BKOOLParser.DOT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.LB)
            else:
                return self.getToken(BKOOLParser.LB, i)

        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.RB)
            else:
                return self.getToken(BKOOLParser.RB, i)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def list_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.List_expContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.List_expContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instance_method_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_state" ):
                return visitor.visitInstance_method_state(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_state(self):

        localctx = BKOOLParser.Instance_method_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_instance_method_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 498
            self.match(BKOOLParser.DOT)
            self.state = 499
            self.match(BKOOLParser.ID)
            self.state = 500
            self.match(BKOOLParser.LB)
            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LSB) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTEGERLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 501
                self.list_exp()


            self.state = 504
            self.match(BKOOLParser.RB)
            self.state = 505
            self.match(BKOOLParser.DOT)
            self.state = 506
            self.match(BKOOLParser.ID)
            self.state = 507
            self.match(BKOOLParser.LB)
            self.state = 509
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LSB) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTEGERLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 508
                self.list_exp()


            self.state = 511
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def list_exp(self):
            return self.getTypedRuleContext(BKOOLParser.List_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_static_method_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_state" ):
                return visitor.visitStatic_method_state(self)
            else:
                return visitor.visitChildren(self)




    def static_method_state(self):

        localctx = BKOOLParser.Static_method_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_static_method_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 514
            self.match(BKOOLParser.DOT)
            self.state = 515
            self.match(BKOOLParser.ID)
            self.state = 516
            self.match(BKOOLParser.LB)
            self.state = 518
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LSB) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTEGERLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 517
                self.list_exp()


            self.state = 520
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_list_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_exp" ):
                return visitor.visitList_exp(self)
            else:
                return visitor.visitChildren(self)




    def list_exp(self):

        localctx = BKOOLParser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_list_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.exp()
            self.state = 527
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 523
                self.match(BKOOLParser.COMMA)
                self.state = 524
                self.exp()
                self.state = 529
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self._predicates[16] = self.exp2_sempred
        self._predicates[17] = self.exp3_sempred
        self._predicates[18] = self.exp4_sempred
        self._predicates[19] = self.exp5_sempred
        self._predicates[23] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




