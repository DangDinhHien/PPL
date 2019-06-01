# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0273\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\5\34\u00f0\n\34\3\35\3\35\3")
        buf.write("\35\3\35\7\35\u00f6\n\35\f\35\16\35\u00f9\13\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\36\3\36\7\36\u0102\n\36\f\36\16\36")
        buf.write("\u0105\13\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\7")
        buf.write("\37\u010f\n\37\f\37\16\37\u0112\13\37\3\37\3\37\3 \6 ")
        buf.write("\u0117\n \r \16 \u0118\3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3")
        buf.write(")\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\3")
        buf.write("8\38\38\39\39\39\39\3:\3:\3:\3:\3;\3;\3;\3<\3<\3<\3<\3")
        buf.write("=\3=\3=\3=\3>\3>\3>\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3")
        buf.write("C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3G\3H\3H\3H\3I\3I\3J\3J\3")
        buf.write("K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3")
        buf.write("S\3S\3T\3T\7T\u01f1\nT\fT\16T\u01f4\13T\3U\6U\u01f7\n")
        buf.write("U\rU\16U\u01f8\3V\6V\u01fc\nV\rV\16V\u01fd\3V\3V\5V\u0202")
        buf.write("\nV\3V\7V\u0205\nV\fV\16V\u0208\13V\3V\6V\u020b\nV\rV")
        buf.write("\16V\u020c\3V\5V\u0210\nV\3V\3V\7V\u0214\nV\fV\16V\u0217")
        buf.write("\13V\3V\5V\u021a\nV\3V\6V\u021d\nV\rV\16V\u021e\3V\3V")
        buf.write("\7V\u0223\nV\fV\16V\u0226\13V\3V\5V\u0229\nV\3V\6V\u022c")
        buf.write("\nV\rV\16V\u022d\3V\6V\u0231\nV\rV\16V\u0232\3V\5V\u0236")
        buf.write("\nV\3V\7V\u0239\nV\fV\16V\u023c\13V\5V\u023e\nV\3W\3W")
        buf.write("\5W\u0242\nW\3W\6W\u0245\nW\rW\16W\u0246\3X\3X\3X\7X\u024c")
        buf.write("\nX\fX\16X\u024f\13X\3X\3X\3X\3Y\3Y\3Y\3Z\3Z\3Z\3[\3[")
        buf.write("\3[\7[\u025d\n[\f[\16[\u0260\13[\3[\5[\u0263\n[\3[\3[")
        buf.write("\3\\\3\\\3\\\7\\\u026a\n\\\f\\\16\\\u026d\13\\\3\\\3\\")
        buf.write("\3\\\3\\\3\\\5\u00f7\u0103\u026b\2]\3\2\5\2\7\2\t\2\13")
        buf.write("\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2")
        buf.write("#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\39\4;\5=\6?\7")
        buf.write("A\bC\tE\nG\13I\fK\rM\16O\17Q\20S\21U\22W\23Y\24[\25]\26")
        buf.write("_\27a\30c\31e\32g\33i\34k\35m\36o\37q s!u\"w#y${%}&\177")
        buf.write("\'\u0081(\u0083)\u0085*\u0087+\u0089,\u008b-\u008d.\u008f")
        buf.write("/\u0091\60\u0093\61\u0095\62\u0097\63\u0099\64\u009b\65")
        buf.write("\u009d\66\u009f\67\u00a18\u00a39\u00a5:\u00a7;\u00a9<")
        buf.write("\u00ab=\u00ad\2\u00af>\u00b1\2\u00b3?\u00b5@\u00b7A\3")
        buf.write("\2&\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4")
        buf.write("\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOo")
        buf.write("o\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2")
        buf.write("VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\|")
        buf.write("|\4\2\f\f\17\17\5\2\13\f\17\17\"\"\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\3\2\62;\b\2\f\f\17\17$$GHQQ^^\n\2$$))^^ddhhpp")
        buf.write("ttvv\3\3\f\f\4\2$$^^\3\2^^\2\u0277\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7")
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00af\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\3\u00b9")
        buf.write("\3\2\2\2\5\u00bb\3\2\2\2\7\u00bd\3\2\2\2\t\u00bf\3\2\2")
        buf.write("\2\13\u00c1\3\2\2\2\r\u00c3\3\2\2\2\17\u00c5\3\2\2\2\21")
        buf.write("\u00c7\3\2\2\2\23\u00c9\3\2\2\2\25\u00cb\3\2\2\2\27\u00cd")
        buf.write("\3\2\2\2\31\u00cf\3\2\2\2\33\u00d1\3\2\2\2\35\u00d3\3")
        buf.write("\2\2\2\37\u00d5\3\2\2\2!\u00d7\3\2\2\2#\u00d9\3\2\2\2")
        buf.write("%\u00db\3\2\2\2\'\u00dd\3\2\2\2)\u00df\3\2\2\2+\u00e1")
        buf.write("\3\2\2\2-\u00e3\3\2\2\2/\u00e5\3\2\2\2\61\u00e7\3\2\2")
        buf.write("\2\63\u00e9\3\2\2\2\65\u00eb\3\2\2\2\67\u00ef\3\2\2\2")
        buf.write("9\u00f1\3\2\2\2;\u00ff\3\2\2\2=\u010a\3\2\2\2?\u0116\3")
        buf.write("\2\2\2A\u011c\3\2\2\2C\u0122\3\2\2\2E\u012b\3\2\2\2G\u012f")
        buf.write("\3\2\2\2I\u0132\3\2\2\2K\u0139\3\2\2\2M\u013c\3\2\2\2")
        buf.write("O\u013f\3\2\2\2Q\u0144\3\2\2\2S\u0149\3\2\2\2U\u0150\3")
        buf.write("\2\2\2W\u0156\3\2\2\2Y\u015c\3\2\2\2[\u0160\3\2\2\2]\u0169")
        buf.write("\3\2\2\2_\u0173\3\2\2\2a\u0177\3\2\2\2c\u017c\3\2\2\2")
        buf.write("e\u0182\3\2\2\2g\u0188\3\2\2\2i\u018b\3\2\2\2k\u0190\3")
        buf.write("\2\2\2m\u0198\3\2\2\2o\u01a0\3\2\2\2q\u01a7\3\2\2\2s\u01ab")
        buf.write("\3\2\2\2u\u01af\3\2\2\2w\u01b2\3\2\2\2y\u01b6\3\2\2\2")
        buf.write("{\u01ba\3\2\2\2}\u01bf\3\2\2\2\177\u01c1\3\2\2\2\u0081")
        buf.write("\u01c3\3\2\2\2\u0083\u01c5\3\2\2\2\u0085\u01c7\3\2\2\2")
        buf.write("\u0087\u01ca\3\2\2\2\u0089\u01cc\3\2\2\2\u008b\u01ce\3")
        buf.write("\2\2\2\u008d\u01d0\3\2\2\2\u008f\u01d3\3\2\2\2\u0091\u01d6")
        buf.write("\3\2\2\2\u0093\u01d8\3\2\2\2\u0095\u01da\3\2\2\2\u0097")
        buf.write("\u01dc\3\2\2\2\u0099\u01de\3\2\2\2\u009b\u01e0\3\2\2\2")
        buf.write("\u009d\u01e2\3\2\2\2\u009f\u01e5\3\2\2\2\u00a1\u01e7\3")
        buf.write("\2\2\2\u00a3\u01e9\3\2\2\2\u00a5\u01eb\3\2\2\2\u00a7\u01ee")
        buf.write("\3\2\2\2\u00a9\u01f6\3\2\2\2\u00ab\u023d\3\2\2\2\u00ad")
        buf.write("\u023f\3\2\2\2\u00af\u0248\3\2\2\2\u00b1\u0253\3\2\2\2")
        buf.write("\u00b3\u0256\3\2\2\2\u00b5\u0259\3\2\2\2\u00b7\u0266\3")
        buf.write("\2\2\2\u00b9\u00ba\t\2\2\2\u00ba\4\3\2\2\2\u00bb\u00bc")
        buf.write("\t\3\2\2\u00bc\6\3\2\2\2\u00bd\u00be\t\4\2\2\u00be\b\3")
        buf.write("\2\2\2\u00bf\u00c0\t\5\2\2\u00c0\n\3\2\2\2\u00c1\u00c2")
        buf.write("\t\6\2\2\u00c2\f\3\2\2\2\u00c3\u00c4\t\7\2\2\u00c4\16")
        buf.write("\3\2\2\2\u00c5\u00c6\t\b\2\2\u00c6\20\3\2\2\2\u00c7\u00c8")
        buf.write("\t\t\2\2\u00c8\22\3\2\2\2\u00c9\u00ca\t\n\2\2\u00ca\24")
        buf.write("\3\2\2\2\u00cb\u00cc\t\13\2\2\u00cc\26\3\2\2\2\u00cd\u00ce")
        buf.write("\t\f\2\2\u00ce\30\3\2\2\2\u00cf\u00d0\t\r\2\2\u00d0\32")
        buf.write("\3\2\2\2\u00d1\u00d2\t\16\2\2\u00d2\34\3\2\2\2\u00d3\u00d4")
        buf.write("\t\17\2\2\u00d4\36\3\2\2\2\u00d5\u00d6\t\20\2\2\u00d6")
        buf.write(" \3\2\2\2\u00d7\u00d8\t\21\2\2\u00d8\"\3\2\2\2\u00d9\u00da")
        buf.write("\t\22\2\2\u00da$\3\2\2\2\u00db\u00dc\t\23\2\2\u00dc&\3")
        buf.write("\2\2\2\u00dd\u00de\t\24\2\2\u00de(\3\2\2\2\u00df\u00e0")
        buf.write("\t\25\2\2\u00e0*\3\2\2\2\u00e1\u00e2\t\26\2\2\u00e2,\3")
        buf.write("\2\2\2\u00e3\u00e4\t\27\2\2\u00e4.\3\2\2\2\u00e5\u00e6")
        buf.write("\t\30\2\2\u00e6\60\3\2\2\2\u00e7\u00e8\t\31\2\2\u00e8")
        buf.write("\62\3\2\2\2\u00e9\u00ea\t\32\2\2\u00ea\64\3\2\2\2\u00eb")
        buf.write("\u00ec\t\33\2\2\u00ec\66\3\2\2\2\u00ed\u00f0\5a\61\2\u00ee")
        buf.write("\u00f0\5c\62\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2\2")
        buf.write("\u00f08\3\2\2\2\u00f1\u00f2\7*\2\2\u00f2\u00f3\7,\2\2")
        buf.write("\u00f3\u00f7\3\2\2\2\u00f4\u00f6\13\2\2\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f7")
        buf.write("\u00f5\3\2\2\2\u00f8\u00fa\3\2\2\2\u00f9\u00f7\3\2\2\2")
        buf.write("\u00fa\u00fb\7,\2\2\u00fb\u00fc\7+\2\2\u00fc\u00fd\3\2")
        buf.write("\2\2\u00fd\u00fe\b\35\2\2\u00fe:\3\2\2\2\u00ff\u0103\7")
        buf.write("}\2\2\u0100\u0102\13\2\2\2\u0101\u0100\3\2\2\2\u0102\u0105")
        buf.write("\3\2\2\2\u0103\u0104\3\2\2\2\u0103\u0101\3\2\2\2\u0104")
        buf.write("\u0106\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0107\7\177\2")
        buf.write("\2\u0107\u0108\3\2\2\2\u0108\u0109\b\36\2\2\u0109<\3\2")
        buf.write("\2\2\u010a\u010b\7\61\2\2\u010b\u010c\7\61\2\2\u010c\u0110")
        buf.write("\3\2\2\2\u010d\u010f\n\34\2\2\u010e\u010d\3\2\2\2\u010f")
        buf.write("\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111\u0113\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0114\b")
        buf.write("\37\2\2\u0114>\3\2\2\2\u0115\u0117\t\35\2\2\u0116\u0115")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0116\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\b \2\2")
        buf.write("\u011b@\3\2\2\2\u011c\u011d\5\5\3\2\u011d\u011e\5%\23")
        buf.write("\2\u011e\u011f\5\13\6\2\u011f\u0120\5\3\2\2\u0120\u0121")
        buf.write("\5\27\f\2\u0121B\3\2\2\2\u0122\u0123\5\7\4\2\u0123\u0124")
        buf.write("\5\37\20\2\u0124\u0125\5\35\17\2\u0125\u0126\5)\25\2\u0126")
        buf.write("\u0127\5\23\n\2\u0127\u0128\5\35\17\2\u0128\u0129\5+\26")
        buf.write("\2\u0129\u012a\5\13\6\2\u012aD\3\2\2\2\u012b\u012c\5\r")
        buf.write("\7\2\u012c\u012d\5\37\20\2\u012d\u012e\5%\23\2\u012eF")
        buf.write("\3\2\2\2\u012f\u0130\5)\25\2\u0130\u0131\5\37\20\2\u0131")
        buf.write("H\3\2\2\2\u0132\u0133\5\t\5\2\u0133\u0134\5\37\20\2\u0134")
        buf.write("\u0135\5/\30\2\u0135\u0136\5\35\17\2\u0136\u0137\5)\25")
        buf.write("\2\u0137\u0138\5\37\20\2\u0138J\3\2\2\2\u0139\u013a\5")
        buf.write("\t\5\2\u013a\u013b\5\37\20\2\u013bL\3\2\2\2\u013c\u013d")
        buf.write("\5\23\n\2\u013d\u013e\5\r\7\2\u013eN\3\2\2\2\u013f\u0140")
        buf.write("\5)\25\2\u0140\u0141\5\21\t\2\u0141\u0142\5\13\6\2\u0142")
        buf.write("\u0143\5\35\17\2\u0143P\3\2\2\2\u0144\u0145\5\13\6\2\u0145")
        buf.write("\u0146\5\31\r\2\u0146\u0147\5\'\24\2\u0147\u0148\5\13")
        buf.write("\6\2\u0148R\3\2\2\2\u0149\u014a\5%\23\2\u014a\u014b\5")
        buf.write("\13\6\2\u014b\u014c\5)\25\2\u014c\u014d\5+\26\2\u014d")
        buf.write("\u014e\5%\23\2\u014e\u014f\5\35\17\2\u014fT\3\2\2\2\u0150")
        buf.write("\u0151\5/\30\2\u0151\u0152\5\21\t\2\u0152\u0153\5\23\n")
        buf.write("\2\u0153\u0154\5\31\r\2\u0154\u0155\5\13\6\2\u0155V\3")
        buf.write("\2\2\2\u0156\u0157\5\5\3\2\u0157\u0158\5\13\6\2\u0158")
        buf.write("\u0159\5\17\b\2\u0159\u015a\5\23\n\2\u015a\u015b\5\35")
        buf.write("\17\2\u015bX\3\2\2\2\u015c\u015d\5\13\6\2\u015d\u015e")
        buf.write("\5\35\17\2\u015e\u015f\5\t\5\2\u015fZ\3\2\2\2\u0160\u0161")
        buf.write("\5\r\7\2\u0161\u0162\5+\26\2\u0162\u0163\5\35\17\2\u0163")
        buf.write("\u0164\5\7\4\2\u0164\u0165\5)\25\2\u0165\u0166\5\23\n")
        buf.write("\2\u0166\u0167\5\37\20\2\u0167\u0168\5\35\17\2\u0168\\")
        buf.write("\3\2\2\2\u0169\u016a\5!\21\2\u016a\u016b\5%\23\2\u016b")
        buf.write("\u016c\5\37\20\2\u016c\u016d\5\7\4\2\u016d\u016e\5\13")
        buf.write("\6\2\u016e\u016f\5\t\5\2\u016f\u0170\5+\26\2\u0170\u0171")
        buf.write("\5%\23\2\u0171\u0172\5\13\6\2\u0172^\3\2\2\2\u0173\u0174")
        buf.write("\5-\27\2\u0174\u0175\5\3\2\2\u0175\u0176\5%\23\2\u0176")
        buf.write("`\3\2\2\2\u0177\u0178\5)\25\2\u0178\u0179\5%\23\2\u0179")
        buf.write("\u017a\5+\26\2\u017a\u017b\5\13\6\2\u017bb\3\2\2\2\u017c")
        buf.write("\u017d\5\r\7\2\u017d\u017e\5\3\2\2\u017e\u017f\5\31\r")
        buf.write("\2\u017f\u0180\5\'\24\2\u0180\u0181\5\13\6\2\u0181d\3")
        buf.write("\2\2\2\u0182\u0183\5\3\2\2\u0183\u0184\5%\23\2\u0184\u0185")
        buf.write("\5%\23\2\u0185\u0186\5\3\2\2\u0186\u0187\5\63\32\2\u0187")
        buf.write("f\3\2\2\2\u0188\u0189\5\37\20\2\u0189\u018a\5\r\7\2\u018a")
        buf.write("h\3\2\2\2\u018b\u018c\5%\23\2\u018c\u018d\5\13\6\2\u018d")
        buf.write("\u018e\5\3\2\2\u018e\u018f\5\31\r\2\u018fj\3\2\2\2\u0190")
        buf.write("\u0191\5\5\3\2\u0191\u0192\5\37\20\2\u0192\u0193\5\37")
        buf.write("\20\2\u0193\u0194\5\31\r\2\u0194\u0195\5\13\6\2\u0195")
        buf.write("\u0196\5\3\2\2\u0196\u0197\5\35\17\2\u0197l\3\2\2\2\u0198")
        buf.write("\u0199\5\23\n\2\u0199\u019a\5\35\17\2\u019a\u019b\5)\25")
        buf.write("\2\u019b\u019c\5\13\6\2\u019c\u019d\5\17\b\2\u019d\u019e")
        buf.write("\5\13\6\2\u019e\u019f\5%\23\2\u019fn\3\2\2\2\u01a0\u01a1")
        buf.write("\5\'\24\2\u01a1\u01a2\5)\25\2\u01a2\u01a3\5%\23\2\u01a3")
        buf.write("\u01a4\5\23\n\2\u01a4\u01a5\5\35\17\2\u01a5\u01a6\5\17")
        buf.write("\b\2\u01a6p\3\2\2\2\u01a7\u01a8\5\35\17\2\u01a8\u01a9")
        buf.write("\5\37\20\2\u01a9\u01aa\5)\25\2\u01aar\3\2\2\2\u01ab\u01ac")
        buf.write("\5\3\2\2\u01ac\u01ad\5\35\17\2\u01ad\u01ae\5\t\5\2\u01ae")
        buf.write("t\3\2\2\2\u01af\u01b0\5\37\20\2\u01b0\u01b1\5%\23\2\u01b1")
        buf.write("v\3\2\2\2\u01b2\u01b3\5\t\5\2\u01b3\u01b4\5\23\n\2\u01b4")
        buf.write("\u01b5\5-\27\2\u01b5x\3\2\2\2\u01b6\u01b7\5\33\16\2\u01b7")
        buf.write("\u01b8\5\37\20\2\u01b8\u01b9\5\t\5\2\u01b9z\3\2\2\2\u01ba")
        buf.write("\u01bb\5/\30\2\u01bb\u01bc\5\23\n\2\u01bc\u01bd\5)\25")
        buf.write("\2\u01bd\u01be\5\21\t\2\u01be|\3\2\2\2\u01bf\u01c0\7-")
        buf.write("\2\2\u01c0~\3\2\2\2\u01c1\u01c2\7/\2\2\u01c2\u0080\3\2")
        buf.write("\2\2\u01c3\u01c4\7,\2\2\u01c4\u0082\3\2\2\2\u01c5\u01c6")
        buf.write("\7\61\2\2\u01c6\u0084\3\2\2\2\u01c7\u01c8\7>\2\2\u01c8")
        buf.write("\u01c9\7@\2\2\u01c9\u0086\3\2\2\2\u01ca\u01cb\7?\2\2\u01cb")
        buf.write("\u0088\3\2\2\2\u01cc\u01cd\7>\2\2\u01cd\u008a\3\2\2\2")
        buf.write("\u01ce\u01cf\7@\2\2\u01cf\u008c\3\2\2\2\u01d0\u01d1\7")
        buf.write(">\2\2\u01d1\u01d2\7?\2\2\u01d2\u008e\3\2\2\2\u01d3\u01d4")
        buf.write("\7@\2\2\u01d4\u01d5\7?\2\2\u01d5\u0090\3\2\2\2\u01d6\u01d7")
        buf.write("\7]\2\2\u01d7\u0092\3\2\2\2\u01d8\u01d9\7_\2\2\u01d9\u0094")
        buf.write("\3\2\2\2\u01da\u01db\7<\2\2\u01db\u0096\3\2\2\2\u01dc")
        buf.write("\u01dd\7*\2\2\u01dd\u0098\3\2\2\2\u01de\u01df\7+\2\2\u01df")
        buf.write("\u009a\3\2\2\2\u01e0\u01e1\7=\2\2\u01e1\u009c\3\2\2\2")
        buf.write("\u01e2\u01e3\7\60\2\2\u01e3\u01e4\7\60\2\2\u01e4\u009e")
        buf.write("\3\2\2\2\u01e5\u01e6\7.\2\2\u01e6\u00a0\3\2\2\2\u01e7")
        buf.write("\u01e8\7}\2\2\u01e8\u00a2\3\2\2\2\u01e9\u01ea\7\177\2")
        buf.write("\2\u01ea\u00a4\3\2\2\2\u01eb\u01ec\7<\2\2\u01ec\u01ed")
        buf.write("\7?\2\2\u01ed\u00a6\3\2\2\2\u01ee\u01f2\t\36\2\2\u01ef")
        buf.write("\u01f1\t\37\2\2\u01f0\u01ef\3\2\2\2\u01f1\u01f4\3\2\2")
        buf.write("\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u00a8")
        buf.write("\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01f7\t \2\2\u01f6")
        buf.write("\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f6\3\2\2\2")
        buf.write("\u01f8\u01f9\3\2\2\2\u01f9\u00aa\3\2\2\2\u01fa\u01fc\t")
        buf.write(" \2\2\u01fb\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fb")
        buf.write("\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0201\5\u00adW\2\u0200\u0202\7\60\2\2\u0201\u0200\3\2")
        buf.write("\2\2\u0201\u0202\3\2\2\2\u0202\u0206\3\2\2\2\u0203\u0205")
        buf.write("\t \2\2\u0204\u0203\3\2\2\2\u0205\u0208\3\2\2\2\u0206")
        buf.write("\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u023e\3\2\2\2")
        buf.write("\u0208\u0206\3\2\2\2\u0209\u020b\t \2\2\u020a\u0209\3")
        buf.write("\2\2\2\u020b\u020c\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d")
        buf.write("\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u0210\7\60\2\2\u020f")
        buf.write("\u020e\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0211\3\2\2\2")
        buf.write("\u0211\u023e\5\u00adW\2\u0212\u0214\t \2\2\u0213\u0212")
        buf.write("\3\2\2\2\u0214\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215")
        buf.write("\u0216\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215\3\2\2\2")
        buf.write("\u0218\u021a\7\60\2\2\u0219\u0218\3\2\2\2\u0219\u021a")
        buf.write("\3\2\2\2\u021a\u021c\3\2\2\2\u021b\u021d\t \2\2\u021c")
        buf.write("\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u021c\3\2\2\2")
        buf.write("\u021e\u021f\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u023e\5")
        buf.write("\u00adW\2\u0221\u0223\t \2\2\u0222\u0221\3\2\2\2\u0223")
        buf.write("\u0226\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225\3\2\2\2")
        buf.write("\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u0229\7")
        buf.write("\60\2\2\u0228\u0227\3\2\2\2\u0228\u0229\3\2\2\2\u0229")
        buf.write("\u022b\3\2\2\2\u022a\u022c\t \2\2\u022b\u022a\3\2\2\2")
        buf.write("\u022c\u022d\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022e\3")
        buf.write("\2\2\2\u022e\u023e\3\2\2\2\u022f\u0231\t \2\2\u0230\u022f")
        buf.write("\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0230\3\2\2\2\u0232")
        buf.write("\u0233\3\2\2\2\u0233\u0235\3\2\2\2\u0234\u0236\7\60\2")
        buf.write("\2\u0235\u0234\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u023a")
        buf.write("\3\2\2\2\u0237\u0239\t \2\2\u0238\u0237\3\2\2\2\u0239")
        buf.write("\u023c\3\2\2\2\u023a\u0238\3\2\2\2\u023a\u023b\3\2\2\2")
        buf.write("\u023b\u023e\3\2\2\2\u023c\u023a\3\2\2\2\u023d\u01fb\3")
        buf.write("\2\2\2\u023d\u020a\3\2\2\2\u023d\u0215\3\2\2\2\u023d\u0224")
        buf.write("\3\2\2\2\u023d\u0230\3\2\2\2\u023e\u00ac\3\2\2\2\u023f")
        buf.write("\u0241\t\6\2\2\u0240\u0242\7/\2\2\u0241\u0240\3\2\2\2")
        buf.write("\u0241\u0242\3\2\2\2\u0242\u0244\3\2\2\2\u0243\u0245\t")
        buf.write(" \2\2\u0244\u0243\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0244")
        buf.write("\3\2\2\2\u0246\u0247\3\2\2\2\u0247\u00ae\3\2\2\2\u0248")
        buf.write("\u024d\7$\2\2\u0249\u024c\5\u00b1Y\2\u024a\u024c\n!\2")
        buf.write("\2\u024b\u0249\3\2\2\2\u024b\u024a\3\2\2\2\u024c\u024f")
        buf.write("\3\2\2\2\u024d\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e")
        buf.write("\u0250\3\2\2\2\u024f\u024d\3\2\2\2\u0250\u0251\7$\2\2")
        buf.write("\u0251\u0252\bX\3\2\u0252\u00b0\3\2\2\2\u0253\u0254\7")
        buf.write("^\2\2\u0254\u0255\t\"\2\2\u0255\u00b2\3\2\2\2\u0256\u0257")
        buf.write("\13\2\2\2\u0257\u0258\bZ\4\2\u0258\u00b4\3\2\2\2\u0259")
        buf.write("\u025e\7$\2\2\u025a\u025d\n!\2\2\u025b\u025d\5\u00b1Y")
        buf.write("\2\u025c\u025a\3\2\2\2\u025c\u025b\3\2\2\2\u025d\u0260")
        buf.write("\3\2\2\2\u025e\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f")
        buf.write("\u0262\3\2\2\2\u0260\u025e\3\2\2\2\u0261\u0263\t#\2\2")
        buf.write("\u0262\u0261\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0265\b")
        buf.write("[\5\2\u0265\u00b6\3\2\2\2\u0266\u026b\7$\2\2\u0267\u026a")
        buf.write("\5\u00b1Y\2\u0268\u026a\n$\2\2\u0269\u0267\3\2\2\2\u0269")
        buf.write("\u0268\3\2\2\2\u026a\u026d\3\2\2\2\u026b\u026c\3\2\2\2")
        buf.write("\u026b\u0269\3\2\2\2\u026c\u026e\3\2\2\2\u026d\u026b\3")
        buf.write("\2\2\2\u026e\u026f\t%\2\2\u026f\u0270\n\"\2\2\u0270\u0271")
        buf.write("\3\2\2\2\u0271\u0272\b\\\6\2\u0272\u00b8\3\2\2\2\"\2\u00ef")
        buf.write("\u00f7\u0103\u0110\u0118\u01f2\u01f8\u01fd\u0201\u0206")
        buf.write("\u020c\u020f\u0215\u0219\u021e\u0224\u0228\u022d\u0232")
        buf.write("\u0235\u023a\u023d\u0241\u0246\u024b\u024d\u025c\u025e")
        buf.write("\u0262\u0269\u026b\7\b\2\2\3X\2\3Z\3\3[\4\3\\\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOL_LIT = 1
    COMMENT1 = 2
    COMMENT2 = 3
    COMMENT3 = 4
    WS = 5
    BREAK = 6
    CONTINUE = 7
    FOR = 8
    TO = 9
    DOWNTO = 10
    DO = 11
    IF = 12
    THEN = 13
    ELSE = 14
    RETURN = 15
    WHILE = 16
    BEGIN = 17
    END = 18
    FUNCTION = 19
    PROCEDURE = 20
    VAR = 21
    TRUE = 22
    FALSE = 23
    ARRAY = 24
    OF = 25
    REAL = 26
    BOOLEAN = 27
    INTEGER = 28
    STRING = 29
    NOT = 30
    AND = 31
    OR = 32
    DIV = 33
    MOD = 34
    WITH = 35
    ADD = 36
    SUB = 37
    MUL = 38
    DIVISION = 39
    NOTEQ = 40
    EQ = 41
    LESS = 42
    GREATER = 43
    LEQ = 44
    GEQ = 45
    LSB = 46
    RSB = 47
    COLON = 48
    LB = 49
    RB = 50
    SEMI = 51
    DD = 52
    COMMA = 53
    LK = 54
    RK = 55
    ASSIGN = 56
    IDENTIFIER = 57
    INT_LIT = 58
    REAL_LIT = 59
    STRING_LIT = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'<>'", "'='", "'<'", "'>'", "'<='", 
            "'>='", "'['", "']'", "':'", "'('", "')'", "';'", "'..'", "','", 
            "'{'", "'}'", "':='" ]

    symbolicNames = [ "<INVALID>",
            "BOOL_LIT", "COMMENT1", "COMMENT2", "COMMENT3", "WS", "BREAK", 
            "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", 
            "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
            "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
            "STRING", "NOT", "AND", "OR", "DIV", "MOD", "WITH", "ADD", "SUB", 
            "MUL", "DIVISION", "NOTEQ", "EQ", "LESS", "GREATER", "LEQ", 
            "GEQ", "LSB", "RSB", "COLON", "LB", "RB", "SEMI", "DD", "COMMA", 
            "LK", "RK", "ASSIGN", "IDENTIFIER", "INT_LIT", "REAL_LIT", "STRING_LIT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "BOOL_LIT", "COMMENT1", "COMMENT2", 
                  "COMMENT3", "WS", "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", 
                  "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", 
                  "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", 
                  "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", 
                  "NOT", "AND", "OR", "DIV", "MOD", "WITH", "ADD", "SUB", 
                  "MUL", "DIVISION", "NOTEQ", "EQ", "LESS", "GREATER", "LEQ", 
                  "GEQ", "LSB", "RSB", "COLON", "LB", "RB", "SEMI", "DD", 
                  "COMMA", "LK", "RK", "ASSIGN", "IDENTIFIER", "INT_LIT", 
                  "REAL_LIT", "EXP", "STRING_LIT", "EscapeSequence", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[86] = self.STRING_LIT_action 
            actions[88] = self.ERROR_CHAR_action 
            actions[89] = self.UNCLOSE_STRING_action 
            actions[90] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
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
                    
     


