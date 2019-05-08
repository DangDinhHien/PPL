import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_integer(self):
        self.assertTrue(TestLexer.test("123","123,<EOF>",101))
    def test_integer1(self):
        self.assertTrue(TestLexer.test("-123","-,123,<EOF>",102))
    def test_integer2(self):
        self.assertTrue(TestLexer.test("--123","-,-,123,<EOF>",103))
    def test_integer3(self):
        self.assertTrue(TestLexer.test("123_","123,_,<EOF>",104))
    def test_integer4(self):
        self.assertTrue(TestLexer.test("12a3","12,a3,<EOF>",105))

    def test_identifier(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",106))
    def test_identifier1(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",107))
    def test_identifier2(self):
        self.assertTrue(TestLexer.test("aAsVN","aAsVN,<EOF>",108))
    def test_identifier3(self):
        self.assertTrue(TestLexer.test("___","___,<EOF>",109))
    def test_identifier4(self):
        self.assertTrue(TestLexer.test("_a123","_a123,<EOF>",110))
    def test_identifier5(self):
        self.assertTrue(TestLexer.test("123_a","123,_a,<EOF>",111))
    def test_identifier6(self):
        self.assertTrue(TestLexer.test("12\"","12,Unclosed String: ",112))
    def test_identifier7(self):
        self.assertTrue(TestLexer.test("123@","123,Error Token @",113))
    def test_identifier8(self):
        self.assertTrue(TestLexer.test("123t12a","123,t12a,<EOF>",114))

    def test_float(self):
        self.assertTrue(TestLexer.test("123.1","123.1,<EOF>",115))
    def test_float1(self):
        self.assertTrue(TestLexer.test("123.1E10","123.1E10,<EOF>",116))
    def test_float2(self):
        self.assertTrue(TestLexer.test("23.1E-10","23.1E-10,<EOF>",117))
    def test_float3(self):
        self.assertTrue(TestLexer.test(".1e5-1",".,1e5,-,1,<EOF>",118))
    def test_float4(self):
        self.assertTrue(TestLexer.test("1e+23.15","1e+23,.,15,<EOF>",119))
    def test_float5(self):
        self.assertTrue(TestLexer.test("123e","123,e,<EOF>",120))
    def test_float6(self):
        self.assertTrue(TestLexer.test("123e1","123e1,<EOF>",121))

    def test_string(self): 
        self.assertTrue(TestLexer.test(""" " " """,""" ,<EOF>""",122))
    def test_string1(self): 
        self.assertTrue(TestLexer.test(" \"\\\\\\t\" " ,"""\\\\\\t,<EOF>""",123))
    def test_string2(self): 
        self.assertTrue(TestLexer.test(""" "\\"aadadddldld\\"" ""","""\\"aadadddldld\\",<EOF>""",124))
    def test_string3(self): 
        self.assertTrue(TestLexer.test(""" "a@@#$$%%" ""","""a@@#$$%%,<EOF>""",125))
    def test_string4(self): 
        self.assertTrue(TestLexer.test(""" "akdkkk\\\\kadadad" ""","""akdkkk\\\\kadadad,<EOF>""",126))
    def test_string5(self): 
        self.assertTrue(TestLexer.test(""" "\\t" ""","""\\t,<EOF>""",127))
    def test_string6(self): 
        self.assertTrue(TestLexer.test(" \"\\takvjv\" " ,"""\\takvjv,<EOF>""",128))
    def test_string7(self): 
        self.assertTrue(TestLexer.test(" \"aaaa\\t\" " ,"""aaaa\\t,<EOF>""",129))
    def test_string8(self): 
        self.assertTrue(TestLexer.test(" \"\\\"nbnbn\" " ,"""\\\"nbnbn,<EOF>""",130))
    def test_string9(self): 
        self.assertTrue(TestLexer.test(" \"\\\\\" " ,"""\\\\,<EOF>""",131))    

    def test_illegal_escape(self):
        self.assertTrue(TestLexer.test(""" "aa\\kbb" ""","""Illegal Escape In String: aa\\""",132))
    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.test(""" "akdkkk\\\\\\kadadad" ""","""Illegal Escape In String: akdkkk\\\\\\""",133))
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.test(""" "akdkkk\\\\ka\\da\\\\dad" ""","""Illegal Escape In String: akdkkk\\\\ka\\""",134))
    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.test(""" "akdkkk\\\\k...1..a\\da\\\\dad" ""","""Illegal Escape In String: akdkkk\\\\k...1..a\\""",135))
    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.test(""" "aakdkdk\\t\\hbb" ""","""Illegal Escape In String: aakdkdk\\t\\""",136)) 
    def test_illegal_escape5(self):
        self.assertTrue(TestLexer.test(""" "\\k" ""","""Illegal Escape In String: \\""",137))    
    def test_illegal_escape6(self):
        self.assertTrue(TestLexer.test(" \"\\ ","Illegal Escape In String: \\",138))
    def test_illegal_escape7(self):
        self.assertTrue(TestLexer.test(" \"\\t\\ ","Illegal Escape In String: \\t\\",139))
    def test_illegal_escape8(self):
        self.assertTrue(TestLexer.test(" \"\\k\\\\ ","Illegal Escape In String: \\",140))
    def test_illegal_escape9(self):
        self.assertTrue(TestLexer.test(" \"\\\\\\u\" ","Illegal Escape In String: \\\\\\",141))


    def test_unclosed_string(self):
        self.assertTrue(TestLexer.test("\"\\\\\\\" ","Unclosed String: \\\\\\\" ",142))
    def test_unclosed_string1(self):
        self.assertTrue(TestLexer.test(" \"\\\" " ,"""Unclosed String: \\" """,143))
    def test_unclosed_string2(self):
        self.assertTrue(TestLexer.test(" \"avcdq","""Unclosed String: avcdq""",144))
    def test_unclosed_string3(self):
        self.assertTrue(TestLexer.test(" \"a@@#$$%% ","""Unclosed String: a@@#$$%% """,145))
    def test_unclosed_string4(self):
        self.assertTrue(TestLexer.test(" \"abcd\" \"xyz ","""abcd,Unclosed String: xyz """,146))
    def test_unclosed_string5(self):
        self.assertTrue(TestLexer.test(" \"\"\" ",""",Unclosed String:  """,147))
    def test_unclosed_string6(self):
        self.assertTrue(TestLexer.test(" \" abc\\r\\n \" ",""" abc\\r\\n ,<EOF>""",148))
    def test_unclosed_string7(self):
        self.assertTrue(TestLexer.test(" \"\\t ","Unclosed String: \\t ",149))
    def test_unclosed_string8(self):
        self.assertTrue(TestLexer.test(" \"\\h ","Illegal Escape In String: \\",150))
    def test_unclosed_string9(self):
        self.assertTrue(TestLexer.test(" \"\\b ","Unclosed String: \\b ",151))

    def test_array(self):
        self.assertTrue(TestLexer.test("r,s:float;","r,,,s,:,float,;,<EOF>",152))
    def test_array1(self):
        self.assertTrue(TestLexer.test("a,b:int[5];","a,,,b,:,int,[,5,],;,<EOF>",153))
    def test_array2(self):
        self.assertTrue(TestLexer.test("1..","1.,.,<EOF>",154))
    def test_array3(self):
        self.assertTrue(TestLexer.test("1 ..","1,.,.,<EOF>",155))
    def test_array4(self):
        self.assertTrue(TestLexer.test("143e","143,e,<EOF>",156))

    def test_separator(self):
        self.assertTrue(TestLexer.test("a:=b[10];","a,:=,b,[,10,],;,<EOF>",157))
    def test_separator1(self):
        self.assertTrue(TestLexer.test("n==0","n,==,0,<EOF>",158))
    def test_separator2(self):
        self.assertTrue(TestLexer.test("a(5);","a,(,5,),;,<EOF>",159))
    def test_separator3(self):
        self.assertTrue(TestLexer.test("a,b,c:int;","a,,,b,,,c,:,int,;,<EOF>",160))
    def test_separator4(self):
        self.assertTrue(TestLexer.test("a[int(5)]","a,[,int,(,5,),],<EOF>",161))

    def test_operator(self):
        self.assertTrue(TestLexer.test("x==5;","x,==,5,;,<EOF>",162))
    def test_operator1(self):
        self.assertTrue(TestLexer.test("6>=5;","6,>=,5,;,<EOF>",163))
    def test_operator2(self):
        self.assertTrue(TestLexer.test("x<=y && y<=5;","x,<=,y,&&,y,<=,5,;,<EOF>",164))
    def test_operator3(self):
        self.assertTrue(TestLexer.test("x>z;","x,>,z,;,<EOF>",165))
    def test_operator4(self):
        self.assertTrue(TestLexer.test("a==x || z","a,==,x,||,z,<EOF>",166))
    def test_operator5(self):
        self.assertTrue(TestLexer.test("a*b+c--d","a,*,b,+,c,-,-,d,<EOF>",167))
    def test_operator6(self):
        self.assertTrue(TestLexer.test("a/b/d-2","a,/,b,/,d,-,2,<EOF>",168))
    def test_operator7(self):
        self.assertTrue(TestLexer.test("n:=n--1","n,:=,n,-,-,1,<EOF>",169))
    def test_operator8(self):
        self.assertTrue(TestLexer.test("a % b == c","a,%,b,==,c,<EOF>",170))
    def test_operator9(self):
        self.assertTrue(TestLexer.test("-a+d","-,a,+,d,<EOF>",171))

    def test_keywords(self):
        self.assertTrue(TestLexer.test("final int My1stCons = 1 + 5;","final,int,My1stCons,=,1,+,5,;,<EOF>",172))
    def test_keywords1(self):
        self.assertTrue(TestLexer.test("static final int My2ndCons = 2;","static,final,int,My2ndCons,=,2,;,<EOF>",173))
    def test_keywords2(self):
        self.assertTrue(TestLexer.test("if(a>b)","if,(,a,>,b,),<EOF>",174))
    def test_keywords3(self):
        self.assertTrue(TestLexer.test("return true false","return,true,false,<EOF>",175))
    def test_keywords4(self):
        self.assertTrue(TestLexer.test("int main();","int,main,(,),;,<EOF>",176))
    def test_keywords5(self):
        self.assertTrue(TestLexer.test("begin end","begin,end,<EOF>",177))
    def test_keywords6(self):
        self.assertTrue(TestLexer.test("return this.length*this.width;","return,this,.,length,*,this,.,width,;,<EOF>",178))
    def test_keywords7(self):
        self.assertTrue(TestLexer.test("x.b[2] := x.m()[3];","x,.,b,[,2,],:=,x,.,m,(,),[,3,],;,<EOF>",179))
    def test_keywords8(self):
        self.assertTrue(TestLexer.test("i:string;","i,:,string,;,<EOF>",180))
    def test_keywords9(self):
        self.assertTrue(TestLexer.test("if(S>20) then break;","if,(,S,>,20,),then,break,;,<EOF>",181))
    def test_keywords10(self):
        self.assertTrue(TestLexer.test("if(S>20) then continue;","if,(,S,>,20,),then,continue,;,<EOF>",182))
    def test_keywords11(self):
        self.assertTrue(TestLexer.test("a && b || not c","a,&&,b,||,not,c,<EOF>",183))
    def test_keywords12(self):
        self.assertTrue(TestLexer.test("g >= 5 + a / b","g,>=,5,+,a,/,b,<EOF>",184))

    def test_all(self): 
        self.assertTrue(TestLexer.test("x.b[2] := x.m()[3]+10;","x,.,b,[,2,],:=,x,.,m,(,),[,3,],+,10,;,<EOF>",185))
    def test_all1(self): 
        self.assertTrue(TestLexer.test("class a{ }","class,a,{,},<EOF>",186))
    def test_all2(self): 
        self.assertTrue(TestLexer.test("s := new Rectangle(3,4);","s,:=,new,Rectangle,(,3,,,4,),;,<EOF>",187))
    def test_all3(self): 
        self.assertTrue(TestLexer.test("if(S>20) then a:=5;","if,(,S,>,20,),then,a,:=,5,;,<EOF>",188))
    def test_all4(self): 
        self.assertTrue(TestLexer.test("return this.length*this.width / 2;","return,this,.,length,*,this,.,width,/,2,;,<EOF>",189))
    def test_all5(self): 
        self.assertTrue(TestLexer.test("n:= a || b || c && d;","n,:=,a,||,b,||,c,&&,d,;,<EOF>",190))
    def test_all6(self): 
        self.assertTrue(TestLexer.test("if ((n<10) && (a>b)) then","if,(,(,n,<,10,),&&,(,a,>,b,),),then,<EOF>",191))
    def test_all7(self): 
        self.assertTrue(TestLexer.test("a:= 5+bcd()+edf()[1];","a,:=,5,+,bcd,(,),+,edf,(,),[,1,],;,<EOF>",192))
    def test_all8(self): 
        self.assertTrue(TestLexer.test("n:= a(1,2)[b(123+5)[c(174.145)]];","n,:=,a,(,1,,,2,),[,b,(,123,+,5,),[,c,(,174.145,),],],;,<EOF>",193))
    def test_all9(self): 
        self.assertTrue(TestLexer.test("for i := 1 to 100 do","for,i,:=,1,to,100,do,<EOF>",194))
    def test_all10(self): 
        self.assertTrue(TestLexer.test("for x := 5 downto 2 do","for,x,:=,5,downto,2,do,<EOF>",195))
    def test_all11(self): 
        self.assertTrue(TestLexer.test("if n == 0 then return 1;","if,n,==,0,then,return,1,;,<EOF>",196))
    def test_all12(self): 
        self.assertTrue(TestLexer.test("io.writeIntLn(this.factorial(x));","io,.,writeIntLn,(,this,.,factorial,(,x,),),;,<EOF>",197))
    def test_all13(self): 
        self.assertTrue(TestLexer.test("putIntLn(main );","putIntLn,(,main,),;,<EOF>",198))
    def test_all14(self): 
        self.assertTrue(TestLexer.test("def test_call_function_249(self):","def,test_call_function_249,(,self,),:,<EOF>",199))
    def test_all15(self): 
        self.assertTrue(TestLexer.test("def test:","def,test,:,<EOF>",200))