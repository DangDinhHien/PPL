# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0255\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\3\2")
        buf.write("\5\2\u00bc\n\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$")
        buf.write("\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*")
        buf.write("\3*\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\3;\3;\3<\3<")
        buf.write("\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\3B\3")
        buf.write("B\3B\3C\3C\3C\3C\3D\3D\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3")
        buf.write("I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3M\3N\3N\3O\3O\3O\3P\3P\7")
        buf.write("P\u01c6\nP\fP\16P\u01c9\13P\3P\3P\3P\3P\3Q\3Q\3Q\3Q\7")
        buf.write("Q\u01d3\nQ\fQ\16Q\u01d6\13Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3")
        buf.write("R\7R\u01e1\nR\fR\16R\u01e4\13R\3R\3R\3S\6S\u01e9\nS\r")
        buf.write("S\16S\u01ea\3S\3S\3T\6T\u01f0\nT\rT\16T\u01f1\3U\3U\5")
        buf.write("U\u01f6\nU\3U\6U\u01f9\nU\rU\16U\u01fa\3V\6V\u01fe\nV")
        buf.write("\rV\16V\u01ff\3V\3V\6V\u0204\nV\rV\16V\u0205\3V\3V\7V")
        buf.write("\u020a\nV\fV\16V\u020d\13V\3V\5V\u0210\nV\3V\3V\6V\u0214")
        buf.write("\nV\rV\16V\u0215\3V\5V\u0219\nV\3V\6V\u021c\nV\rV\16V")
        buf.write("\u021d\3V\5V\u0221\nV\3W\3W\7W\u0225\nW\fW\16W\u0228\13")
        buf.write("W\3X\3X\3X\3X\7X\u022e\nX\fX\16X\u0231\13X\3X\3X\3X\3")
        buf.write("Y\3Y\3Y\3Z\3Z\3Z\3[\3[\3[\7[\u023f\n[\f[\16[\u0242\13")
        buf.write("[\3[\5[\u0245\n[\3[\3[\3\\\3\\\3\\\7\\\u024c\n\\\f\\\16")
        buf.write("\\\u024f\13\\\3\\\3\\\3\\\3\\\3\\\5\u01c7\u01d4\u024d")
        buf.write("\2]\3\3\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2")
        buf.write("\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63")
        buf.write("\2\65\2\67\29\4;\5=\6?\7A\bC\tE\nG\13I\fK\rM\16O\17Q\20")
        buf.write("S\21U\22W\23Y\24[\25]\26_\27a\30c\31e\32g\33i\34k\35m")
        buf.write("\36o\37q s!u\"w#y${%}&\177\'\u0081(\u0083)\u0085*\u0087")
        buf.write("+\u0089,\u008b-\u008d.\u008f/\u0091\60\u0093\61\u0095")
        buf.write("\62\u0097\63\u0099\64\u009b\65\u009d\66\u009f\67\u00a1")
        buf.write("8\u00a39\u00a5:\u00a7;\u00a9<\u00ab=\u00ad>\u00af?\u00b1")
        buf.write("\2\u00b3@\u00b5A\u00b7B\3\2&\4\2CCcc\4\2DDdd\4\2EEee\4")
        buf.write("\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLl")
        buf.write("l\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2")
        buf.write("SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4")
        buf.write("\2ZZzz\4\2[[{{\4\2\\\\||\4\2\f\f\17\17\5\2\13\f\17\17")
        buf.write("\"\"\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\b\2\f\f\17\17$")
        buf.write("$GHQQ^^\n\2$$))^^ddhhppttvv\3\3\f\f\4\2$$^^\3\2^^\2\u0253")
        buf.write("\2\3\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2")
        buf.write("\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5")
        buf.write("\3\2\2\2\2\u00b7\3\2\2\2\3\u00bb\3\2\2\2\5\u00bd\3\2\2")
        buf.write("\2\7\u00bf\3\2\2\2\t\u00c1\3\2\2\2\13\u00c3\3\2\2\2\r")
        buf.write("\u00c5\3\2\2\2\17\u00c7\3\2\2\2\21\u00c9\3\2\2\2\23\u00cb")
        buf.write("\3\2\2\2\25\u00cd\3\2\2\2\27\u00cf\3\2\2\2\31\u00d1\3")
        buf.write("\2\2\2\33\u00d3\3\2\2\2\35\u00d5\3\2\2\2\37\u00d7\3\2")
        buf.write("\2\2!\u00d9\3\2\2\2#\u00db\3\2\2\2%\u00dd\3\2\2\2\'\u00df")
        buf.write("\3\2\2\2)\u00e1\3\2\2\2+\u00e3\3\2\2\2-\u00e5\3\2\2\2")
        buf.write("/\u00e7\3\2\2\2\61\u00e9\3\2\2\2\63\u00eb\3\2\2\2\65\u00ed")
        buf.write("\3\2\2\2\67\u00ef\3\2\2\29\u00f1\3\2\2\2;\u00f9\3\2\2")
        buf.write("\2=\u00fe\3\2\2\2?\u0106\3\2\2\2A\u010d\3\2\2\2C\u0113")
        buf.write("\3\2\2\2E\u0117\3\2\2\2G\u011d\3\2\2\2I\u0121\3\2\2\2")
        buf.write("K\u0127\3\2\2\2M\u0130\3\2\2\2O\u0134\3\2\2\2Q\u0137\3")
        buf.write("\2\2\2S\u013e\3\2\2\2U\u0141\3\2\2\2W\u0144\3\2\2\2Y\u0149")
        buf.write("\3\2\2\2[\u014e\3\2\2\2]\u0155\3\2\2\2_\u015b\3\2\2\2")
        buf.write("a\u0164\3\2\2\2c\u016e\3\2\2\2e\u0173\3\2\2\2g\u0178\3")
        buf.write("\2\2\2i\u017e\3\2\2\2k\u0181\3\2\2\2m\u0183\3\2\2\2o\u0185")
        buf.write("\3\2\2\2q\u0187\3\2\2\2s\u0189\3\2\2\2u\u018c\3\2\2\2")
        buf.write("w\u018e\3\2\2\2y\u0190\3\2\2\2{\u0192\3\2\2\2}\u0195\3")
        buf.write("\2\2\2\177\u0198\3\2\2\2\u0081\u019c\3\2\2\2\u0083\u01a0")
        buf.write("\3\2\2\2\u0085\u01a3\3\2\2\2\u0087\u01a7\3\2\2\2\u0089")
        buf.write("\u01ab\3\2\2\2\u008b\u01ad\3\2\2\2\u008d\u01af\3\2\2\2")
        buf.write("\u008f\u01b1\3\2\2\2\u0091\u01b3\3\2\2\2\u0093\u01b5\3")
        buf.write("\2\2\2\u0095\u01b7\3\2\2\2\u0097\u01b9\3\2\2\2\u0099\u01bb")
        buf.write("\3\2\2\2\u009b\u01be\3\2\2\2\u009d\u01c0\3\2\2\2\u009f")
        buf.write("\u01c3\3\2\2\2\u00a1\u01ce\3\2\2\2\u00a3\u01dc\3\2\2\2")
        buf.write("\u00a5\u01e8\3\2\2\2\u00a7\u01ef\3\2\2\2\u00a9\u01f3\3")
        buf.write("\2\2\2\u00ab\u0220\3\2\2\2\u00ad\u0222\3\2\2\2\u00af\u0229")
        buf.write("\3\2\2\2\u00b1\u0235\3\2\2\2\u00b3\u0238\3\2\2\2\u00b5")
        buf.write("\u023b\3\2\2\2\u00b7\u0248\3\2\2\2\u00b9\u00bc\5e\63\2")
        buf.write("\u00ba\u00bc\5g\64\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3")
        buf.write("\2\2\2\u00bc\4\3\2\2\2\u00bd\u00be\t\2\2\2\u00be\6\3\2")
        buf.write("\2\2\u00bf\u00c0\t\3\2\2\u00c0\b\3\2\2\2\u00c1\u00c2\t")
        buf.write("\4\2\2\u00c2\n\3\2\2\2\u00c3\u00c4\t\5\2\2\u00c4\f\3\2")
        buf.write("\2\2\u00c5\u00c6\t\6\2\2\u00c6\16\3\2\2\2\u00c7\u00c8")
        buf.write("\t\7\2\2\u00c8\20\3\2\2\2\u00c9\u00ca\t\b\2\2\u00ca\22")
        buf.write("\3\2\2\2\u00cb\u00cc\t\t\2\2\u00cc\24\3\2\2\2\u00cd\u00ce")
        buf.write("\t\n\2\2\u00ce\26\3\2\2\2\u00cf\u00d0\t\13\2\2\u00d0\30")
        buf.write("\3\2\2\2\u00d1\u00d2\t\f\2\2\u00d2\32\3\2\2\2\u00d3\u00d4")
        buf.write("\t\r\2\2\u00d4\34\3\2\2\2\u00d5\u00d6\t\16\2\2\u00d6\36")
        buf.write("\3\2\2\2\u00d7\u00d8\t\17\2\2\u00d8 \3\2\2\2\u00d9\u00da")
        buf.write("\t\20\2\2\u00da\"\3\2\2\2\u00db\u00dc\t\21\2\2\u00dc$")
        buf.write("\3\2\2\2\u00dd\u00de\t\22\2\2\u00de&\3\2\2\2\u00df\u00e0")
        buf.write("\t\23\2\2\u00e0(\3\2\2\2\u00e1\u00e2\t\24\2\2\u00e2*\3")
        buf.write("\2\2\2\u00e3\u00e4\t\25\2\2\u00e4,\3\2\2\2\u00e5\u00e6")
        buf.write("\t\26\2\2\u00e6.\3\2\2\2\u00e7\u00e8\t\27\2\2\u00e8\60")
        buf.write("\3\2\2\2\u00e9\u00ea\t\30\2\2\u00ea\62\3\2\2\2\u00eb\u00ec")
        buf.write("\t\31\2\2\u00ec\64\3\2\2\2\u00ed\u00ee\t\32\2\2\u00ee")
        buf.write("\66\3\2\2\2\u00ef\u00f0\t\33\2\2\u00f08\3\2\2\2\u00f1")
        buf.write("\u00f2\5\25\13\2\u00f2\u00f3\5\37\20\2\u00f3\u00f4\5+")
        buf.write("\26\2\u00f4\u00f5\5\r\7\2\u00f5\u00f6\5\21\t\2\u00f6\u00f7")
        buf.write("\5\r\7\2\u00f7\u00f8\5\'\24\2\u00f8:\3\2\2\2\u00f9\u00fa")
        buf.write("\5\'\24\2\u00fa\u00fb\5\r\7\2\u00fb\u00fc\5\5\3\2\u00fc")
        buf.write("\u00fd\5\33\16\2\u00fd<\3\2\2\2\u00fe\u00ff\5\7\4\2\u00ff")
        buf.write("\u0100\5!\21\2\u0100\u0101\5!\21\2\u0101\u0102\5\33\16")
        buf.write("\2\u0102\u0103\5\r\7\2\u0103\u0104\5\5\3\2\u0104\u0105")
        buf.write("\5\37\20\2\u0105>\3\2\2\2\u0106\u0107\5)\25\2\u0107\u0108")
        buf.write("\5+\26\2\u0108\u0109\5\'\24\2\u0109\u010a\5\25\13\2\u010a")
        buf.write("\u010b\5\37\20\2\u010b\u010c\5\21\t\2\u010c@\3\2\2\2\u010d")
        buf.write("\u010e\5\5\3\2\u010e\u010f\5\'\24\2\u010f\u0110\5\'\24")
        buf.write("\2\u0110\u0111\5\5\3\2\u0111\u0112\5\65\33\2\u0112B\3")
        buf.write("\2\2\2\u0113\u0114\5/\30\2\u0114\u0115\5\5\3\2\u0115\u0116")
        buf.write("\5\'\24\2\u0116D\3\2\2\2\u0117\u0118\5\7\4\2\u0118\u0119")
        buf.write("\5\r\7\2\u0119\u011a\5\21\t\2\u011a\u011b\5\25\13\2\u011b")
        buf.write("\u011c\5\37\20\2\u011cF\3\2\2\2\u011d\u011e\5\r\7\2\u011e")
        buf.write("\u011f\5\37\20\2\u011f\u0120\5\13\6\2\u0120H\3\2\2\2\u0121")
        buf.write("\u0122\5\7\4\2\u0122\u0123\5\'\24\2\u0123\u0124\5\r\7")
        buf.write("\2\u0124\u0125\5\5\3\2\u0125\u0126\5\31\r\2\u0126J\3\2")
        buf.write("\2\2\u0127\u0128\5\t\5\2\u0128\u0129\5!\21\2\u0129\u012a")
        buf.write("\5\37\20\2\u012a\u012b\5+\26\2\u012b\u012c\5\25\13\2\u012c")
        buf.write("\u012d\5\37\20\2\u012d\u012e\5-\27\2\u012e\u012f\5\r\7")
        buf.write("\2\u012fL\3\2\2\2\u0130\u0131\5\17\b\2\u0131\u0132\5!")
        buf.write("\21\2\u0132\u0133\5\'\24\2\u0133N\3\2\2\2\u0134\u0135")
        buf.write("\5+\26\2\u0135\u0136\5!\21\2\u0136P\3\2\2\2\u0137\u0138")
        buf.write("\5\13\6\2\u0138\u0139\5!\21\2\u0139\u013a\5\61\31\2\u013a")
        buf.write("\u013b\5\37\20\2\u013b\u013c\5+\26\2\u013c\u013d\5!\21")
        buf.write("\2\u013dR\3\2\2\2\u013e\u013f\5\13\6\2\u013f\u0140\5!")
        buf.write("\21\2\u0140T\3\2\2\2\u0141\u0142\5\25\13\2\u0142\u0143")
        buf.write("\5\17\b\2\u0143V\3\2\2\2\u0144\u0145\5+\26\2\u0145\u0146")
        buf.write("\5\23\n\2\u0146\u0147\5\r\7\2\u0147\u0148\5\37\20\2\u0148")
        buf.write("X\3\2\2\2\u0149\u014a\5\r\7\2\u014a\u014b\5\33\16\2\u014b")
        buf.write("\u014c\5)\25\2\u014c\u014d\5\r\7\2\u014dZ\3\2\2\2\u014e")
        buf.write("\u014f\5\'\24\2\u014f\u0150\5\r\7\2\u0150\u0151\5+\26")
        buf.write("\2\u0151\u0152\5-\27\2\u0152\u0153\5\'\24\2\u0153\u0154")
        buf.write("\5\37\20\2\u0154\\\3\2\2\2\u0155\u0156\5\61\31\2\u0156")
        buf.write("\u0157\5\23\n\2\u0157\u0158\5\25\13\2\u0158\u0159\5\33")
        buf.write("\16\2\u0159\u015a\5\r\7\2\u015a^\3\2\2\2\u015b\u015c\5")
        buf.write("\17\b\2\u015c\u015d\5-\27\2\u015d\u015e\5\37\20\2\u015e")
        buf.write("\u015f\5\t\5\2\u015f\u0160\5+\26\2\u0160\u0161\5\25\13")
        buf.write("\2\u0161\u0162\5!\21\2\u0162\u0163\5\37\20\2\u0163`\3")
        buf.write("\2\2\2\u0164\u0165\5#\22\2\u0165\u0166\5\'\24\2\u0166")
        buf.write("\u0167\5!\21\2\u0167\u0168\5\t\5\2\u0168\u0169\5\r\7\2")
        buf.write("\u0169\u016a\5\13\6\2\u016a\u016b\5-\27\2\u016b\u016c")
        buf.write("\5\'\24\2\u016c\u016d\5\r\7\2\u016db\3\2\2\2\u016e\u016f")
        buf.write("\5\61\31\2\u016f\u0170\5\25\13\2\u0170\u0171\5+\26\2\u0171")
        buf.write("\u0172\5\23\n\2\u0172d\3\2\2\2\u0173\u0174\5+\26\2\u0174")
        buf.write("\u0175\5\'\24\2\u0175\u0176\5-\27\2\u0176\u0177\5\r\7")
        buf.write("\2\u0177f\3\2\2\2\u0178\u0179\5\17\b\2\u0179\u017a\5\5")
        buf.write("\3\2\u017a\u017b\5\33\16\2\u017b\u017c\5)\25\2\u017c\u017d")
        buf.write("\5\r\7\2\u017dh\3\2\2\2\u017e\u017f\5!\21\2\u017f\u0180")
        buf.write("\5\17\b\2\u0180j\3\2\2\2\u0181\u0182\7-\2\2\u0182l\3\2")
        buf.write("\2\2\u0183\u0184\7/\2\2\u0184n\3\2\2\2\u0185\u0186\7,")
        buf.write("\2\2\u0186p\3\2\2\2\u0187\u0188\7\61\2\2\u0188r\3\2\2")
        buf.write("\2\u0189\u018a\7>\2\2\u018a\u018b\7@\2\2\u018bt\3\2\2")
        buf.write("\2\u018c\u018d\7?\2\2\u018dv\3\2\2\2\u018e\u018f\7>\2")
        buf.write("\2\u018fx\3\2\2\2\u0190\u0191\7@\2\2\u0191z\3\2\2\2\u0192")
        buf.write("\u0193\7>\2\2\u0193\u0194\7?\2\2\u0194|\3\2\2\2\u0195")
        buf.write("\u0196\7@\2\2\u0196\u0197\7?\2\2\u0197~\3\2\2\2\u0198")
        buf.write("\u0199\5\37\20\2\u0199\u019a\5!\21\2\u019a\u019b\5+\26")
        buf.write("\2\u019b\u0080\3\2\2\2\u019c\u019d\5\5\3\2\u019d\u019e")
        buf.write("\5\37\20\2\u019e\u019f\5\13\6\2\u019f\u0082\3\2\2\2\u01a0")
        buf.write("\u01a1\5!\21\2\u01a1\u01a2\5\'\24\2\u01a2\u0084\3\2\2")
        buf.write("\2\u01a3\u01a4\5\13\6\2\u01a4\u01a5\5\25\13\2\u01a5\u01a6")
        buf.write("\5/\30\2\u01a6\u0086\3\2\2\2\u01a7\u01a8\5\35\17\2\u01a8")
        buf.write("\u01a9\5!\21\2\u01a9\u01aa\5\13\6\2\u01aa\u0088\3\2\2")
        buf.write("\2\u01ab\u01ac\7]\2\2\u01ac\u008a\3\2\2\2\u01ad\u01ae")
        buf.write("\7_\2\2\u01ae\u008c\3\2\2\2\u01af\u01b0\7*\2\2\u01b0\u008e")
        buf.write("\3\2\2\2\u01b1\u01b2\7+\2\2\u01b2\u0090\3\2\2\2\u01b3")
        buf.write("\u01b4\7}\2\2\u01b4\u0092\3\2\2\2\u01b5\u01b6\7\177\2")
        buf.write("\2\u01b6\u0094\3\2\2\2\u01b7\u01b8\7=\2\2\u01b8\u0096")
        buf.write("\3\2\2\2\u01b9\u01ba\7<\2\2\u01ba\u0098\3\2\2\2\u01bb")
        buf.write("\u01bc\7\60\2\2\u01bc\u01bd\7\60\2\2\u01bd\u009a\3\2\2")
        buf.write("\2\u01be\u01bf\7.\2\2\u01bf\u009c\3\2\2\2\u01c0\u01c1")
        buf.write("\7<\2\2\u01c1\u01c2\7?\2\2\u01c2\u009e\3\2\2\2\u01c3\u01c7")
        buf.write("\7}\2\2\u01c4\u01c6\13\2\2\2\u01c5\u01c4\3\2\2\2\u01c6")
        buf.write("\u01c9\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c8\u01ca\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cb\7")
        buf.write("\177\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd\bP\2\2\u01cd")
        buf.write("\u00a0\3\2\2\2\u01ce\u01cf\7*\2\2\u01cf\u01d0\7,\2\2\u01d0")
        buf.write("\u01d4\3\2\2\2\u01d1\u01d3\13\2\2\2\u01d2\u01d1\3\2\2")
        buf.write("\2\u01d3\u01d6\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d4\u01d2")
        buf.write("\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7")
        buf.write("\u01d8\7,\2\2\u01d8\u01d9\7+\2\2\u01d9\u01da\3\2\2\2\u01da")
        buf.write("\u01db\bQ\2\2\u01db\u00a2\3\2\2\2\u01dc\u01dd\7\61\2\2")
        buf.write("\u01dd\u01de\7\61\2\2\u01de\u01e2\3\2\2\2\u01df\u01e1")
        buf.write("\n\34\2\2\u01e0\u01df\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e5\3\2\2\2")
        buf.write("\u01e4\u01e2\3\2\2\2\u01e5\u01e6\bR\2\2\u01e6\u00a4\3")
        buf.write("\2\2\2\u01e7\u01e9\t\35\2\2\u01e8\u01e7\3\2\2\2\u01e9")
        buf.write("\u01ea\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2")
        buf.write("\u01eb\u01ec\3\2\2\2\u01ec\u01ed\bS\2\2\u01ed\u00a6\3")
        buf.write("\2\2\2\u01ee\u01f0\t\36\2\2\u01ef\u01ee\3\2\2\2\u01f0")
        buf.write("\u01f1\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2")
        buf.write("\u01f2\u00a8\3\2\2\2\u01f3\u01f5\t\6\2\2\u01f4\u01f6\5")
        buf.write("m\67\2\u01f5\u01f4\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f8")
        buf.write("\3\2\2\2\u01f7\u01f9\t\36\2\2\u01f8\u01f7\3\2\2\2\u01f9")
        buf.write("\u01fa\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2")
        buf.write("\u01fb\u00aa\3\2\2\2\u01fc\u01fe\t\36\2\2\u01fd\u01fc")
        buf.write("\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0221\7\60\2")
        buf.write("\2\u0202\u0204\t\36\2\2\u0203\u0202\3\2\2\2\u0204\u0205")
        buf.write("\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206")
        buf.write("\u0207\3\2\2\2\u0207\u020b\7\60\2\2\u0208\u020a\t\36\2")
        buf.write("\2\u0209\u0208\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209")
        buf.write("\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020f\3\2\2\2\u020d")
        buf.write("\u020b\3\2\2\2\u020e\u0210\5\u00a9U\2\u020f\u020e\3\2")
        buf.write("\2\2\u020f\u0210\3\2\2\2\u0210\u0221\3\2\2\2\u0211\u0213")
        buf.write("\7\60\2\2\u0212\u0214\t\36\2\2\u0213\u0212\3\2\2\2\u0214")
        buf.write("\u0215\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3\2\2\2")
        buf.write("\u0216\u0218\3\2\2\2\u0217\u0219\5\u00a9U\2\u0218\u0217")
        buf.write("\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u0221\3\2\2\2\u021a")
        buf.write("\u021c\t\36\2\2\u021b\u021a\3\2\2\2\u021c\u021d\3\2\2")
        buf.write("\2\u021d\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u021f")
        buf.write("\3\2\2\2\u021f\u0221\5\u00a9U\2\u0220\u01fd\3\2\2\2\u0220")
        buf.write("\u0203\3\2\2\2\u0220\u0211\3\2\2\2\u0220\u021b\3\2\2\2")
        buf.write("\u0221\u00ac\3\2\2\2\u0222\u0226\t\37\2\2\u0223\u0225")
        buf.write("\t \2\2\u0224\u0223\3\2\2\2\u0225\u0228\3\2\2\2\u0226")
        buf.write("\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u00ae\3\2\2\2")
        buf.write("\u0228\u0226\3\2\2\2\u0229\u022f\7$\2\2\u022a\u022e\5")
        buf.write("\u00b1Y\2\u022b\u022e\5\u00adW\2\u022c\u022e\n!\2\2\u022d")
        buf.write("\u022a\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022c\3\2\2\2")
        buf.write("\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230\3")
        buf.write("\2\2\2\u0230\u0232\3\2\2\2\u0231\u022f\3\2\2\2\u0232\u0233")
        buf.write("\7$\2\2\u0233\u0234\bX\3\2\u0234\u00b0\3\2\2\2\u0235\u0236")
        buf.write("\7^\2\2\u0236\u0237\t\"\2\2\u0237\u00b2\3\2\2\2\u0238")
        buf.write("\u0239\13\2\2\2\u0239\u023a\bZ\4\2\u023a\u00b4\3\2\2\2")
        buf.write("\u023b\u0240\7$\2\2\u023c\u023f\n!\2\2\u023d\u023f\5\u00b1")
        buf.write("Y\2\u023e\u023c\3\2\2\2\u023e\u023d\3\2\2\2\u023f\u0242")
        buf.write("\3\2\2\2\u0240\u023e\3\2\2\2\u0240\u0241\3\2\2\2\u0241")
        buf.write("\u0244\3\2\2\2\u0242\u0240\3\2\2\2\u0243\u0245\t#\2\2")
        buf.write("\u0244\u0243\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0247\b")
        buf.write("[\5\2\u0247\u00b6\3\2\2\2\u0248\u024d\7$\2\2\u0249\u024c")
        buf.write("\5\u00b1Y\2\u024a\u024c\n$\2\2\u024b\u0249\3\2\2\2\u024b")
        buf.write("\u024a\3\2\2\2\u024c\u024f\3\2\2\2\u024d\u024e\3\2\2\2")
        buf.write("\u024d\u024b\3\2\2\2\u024e\u0250\3\2\2\2\u024f\u024d\3")
        buf.write("\2\2\2\u0250\u0251\t%\2\2\u0251\u0252\n\"\2\2\u0252\u0253")
        buf.write("\3\2\2\2\u0253\u0254\b\\\6\2\u0254\u00b8\3\2\2\2\33\2")
        buf.write("\u00bb\u01c7\u01d4\u01e2\u01ea\u01f1\u01f5\u01fa\u01ff")
        buf.write("\u0205\u020b\u020f\u0215\u0218\u021d\u0220\u0226\u022d")
        buf.write("\u022f\u023e\u0240\u0244\u024b\u024d\7\b\2\2\3X\2\3Z\3")
        buf.write("\3[\4\3\\\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLLIT = 1
    INTTYPE = 2
    REALTYPE = 3
    BOOLTYPE = 4
    STRINGTYPE = 5
    ARRAYTYPE = 6
    VAR = 7
    BEGIN = 8
    END = 9
    BREAK = 10
    CONTINUE = 11
    FOR = 12
    TO = 13
    DOWNTO = 14
    DO = 15
    IF = 16
    THEN = 17
    ELSE = 18
    RETURN = 19
    WHILE = 20
    FUCNTION = 21
    PROCEDURE = 22
    WITH = 23
    TRUE = 24
    FALSE = 25
    OF = 26
    ADD_OP = 27
    SUB_OP = 28
    MUL_OP = 29
    DIV_OP = 30
    NOT_EQ_OP = 31
    EQUAL = 32
    LES_THAN = 33
    GRE_THAN = 34
    LOE_THAN = 35
    GOE_THAN = 36
    NOT = 37
    AND = 38
    OR = 39
    DIV = 40
    MOD = 41
    LSB = 42
    RSB = 43
    LB = 44
    RB = 45
    LP = 46
    RP = 47
    SEMI = 48
    COLON = 49
    D_DOT = 50
    COMMA = 51
    ASSIGN = 52
    BLOCK_COMMENT1 = 53
    BLOCK_COMMENT2 = 54
    LINE_COMMENT = 55
    WS = 56
    INTLIT = 57
    EXPONENT_ = 58
    REALLIT = 59
    ID = 60
    STRINGLIT = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'<>'", "'='", "'<'", "'>'", "'<='", 
            "'>='", "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "':'", 
            "'..'", "','", "':='" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "INTTYPE", "REALTYPE", "BOOLTYPE", "STRINGTYPE", 
            "ARRAYTYPE", "VAR", "BEGIN", "END", "BREAK", "CONTINUE", "FOR", 
            "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", 
            "FUCNTION", "PROCEDURE", "WITH", "TRUE", "FALSE", "OF", "ADD_OP", 
            "SUB_OP", "MUL_OP", "DIV_OP", "NOT_EQ_OP", "EQUAL", "LES_THAN", 
            "GRE_THAN", "LOE_THAN", "GOE_THAN", "NOT", "AND", "OR", "DIV", 
            "MOD", "LSB", "RSB", "LB", "RB", "LP", "RP", "SEMI", "COLON", 
            "D_DOT", "COMMA", "ASSIGN", "BLOCK_COMMENT1", "BLOCK_COMMENT2", 
            "LINE_COMMENT", "WS", "INTLIT", "EXPONENT_", "REALLIT", "ID", 
            "STRINGLIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BOOLLIT", "A", "B", "C", "D", "E", "F", "G", "H", "I", 
                  "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
                  "U", "V", "W", "X", "Y", "Z", "INTTYPE", "REALTYPE", "BOOLTYPE", 
                  "STRINGTYPE", "ARRAYTYPE", "VAR", "BEGIN", "END", "BREAK", 
                  "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
                  "ELSE", "RETURN", "WHILE", "FUCNTION", "PROCEDURE", "WITH", 
                  "TRUE", "FALSE", "OF", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
                  "NOT_EQ_OP", "EQUAL", "LES_THAN", "GRE_THAN", "LOE_THAN", 
                  "GOE_THAN", "NOT", "AND", "OR", "DIV", "MOD", "LSB", "RSB", 
                  "LB", "RB", "LP", "RP", "SEMI", "COLON", "D_DOT", "COMMA", 
                  "ASSIGN", "BLOCK_COMMENT1", "BLOCK_COMMENT2", "LINE_COMMENT", 
                  "WS", "INTLIT", "EXPONENT_", "REALLIT", "ID", "STRINGLIT", 
                  "EscapeSequence", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[86] = self.STRINGLIT_action 
            actions[88] = self.ERROR_CHAR_action 
            actions[89] = self.UNCLOSE_STRING_action 
            actions[90] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                        s=self.text[1:-1]   
                        self.text=s
                    
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		raise ErrorToken(self.text)
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                        if self.text[-1]=='\n':
                             raise UncloseString(self.text[1:-1])
                        else:
                            raise UncloseString(self.text[1:])
                    
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                       raise IllegalEscape(self.text[1:]) 
                    
     


