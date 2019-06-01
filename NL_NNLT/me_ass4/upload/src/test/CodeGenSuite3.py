import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_00(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(100); end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_1(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putInt"),[IntLiteral(5)])])])
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_2(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(100.0); end"""
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_3(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(100.0); end"""
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_4(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(10+2); end"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_5(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(10.0+2.0); end"""
        expect = "12.0"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_6(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(10+2.0); end"""
        expect = "12.0"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test_7(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(10*2.0); end"""
        expect = "20.0"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_8(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(10-2.0); end"""
        expect = "8.0"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test_9(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(2.0-10); end"""
        expect = "-8.0"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test_10(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(2.0-10+10); end"""
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    def test_11(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(2.0 / 10.0); end"""
        expect = "0.2"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_12(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(4+2/2); end"""
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_13(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(100 div 2); end"""
        expect = "50"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    def test_14(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putBool(true); end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    def test_15(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(-9); end"""
        expect = "-9"
        self.assertTrue(TestCodeGen.test(input,expect,515))
    def test_16(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(-9.5); end"""
        expect = "-9.5"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    def test_17(self):
        """Simple program: int main() {} """
        input = """
        //var x:integer;
        procedure main();
        begin 
            putString("Hello World"); 
        end"""
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    def test_18(self):
        """Simple program: int main() {} """
        input = """
        //var x:integer;
        procedure main();
        begin 
            putBool(not false); 
        end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    def test_19(self):
        """Simple program: int main() {} """
        input = """
        //var x:integer;
        procedure main();
        begin 
            putInt(1 mod 2); 
        end"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    def test_20(self):
        """Simple program: int main() {} """
        input = """
        procedure main();
        var x:integer;
        begin
            x := 1;
            putInt(x);
            x:=10;
            putInt(x*2);
        end

        """
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    def test_21(self):
        """Simple program: int main() {} """
        input = """
        var x:integer;
        procedure main();
        begin
            x := 1;
            putInt(x);
            x:=10;
            putInt(x*2);
        end
        """
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,521))
    def test_22(self):
        """Simple program: int main() {} """
        input = """
        procedure main();
        var x:integer;
        begin
            x := 1;
            x := (x + 10)mod 5 + 20;
            putInt(x*2);
        end
        """
        expect = "42"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    def test_23(self):
        """Simple program: int main() {} """
        input = """
        procedure main();
        var x:real;
        begin
            x := 1;
            x := x + 10;
            putFloat(x*2);
        end

        """
        expect = "22.0"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    def test_24(self):

        input = """
        procedure main();
        var x:real;
        begin
            if(true) then
            begin
                putInt(100);
            end
        end
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    def test_25(self):

        input = """
        procedure main();
        var x:real;
        begin
            if(1>2) then
            begin
                putInt(100);
            end
            else putInt(101);
        end

        """
        expect = "101"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_26(self):

        input = """
        procedure main();
        var x:integer;
        begin
            x := 0;
            while(x<5) do
            begin
                x := x + 1;
                putInt(x);
            end
        end

        """
        expect = "12345"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_27(self):

        input = """
        procedure main();
        var x:integer;
        begin
            for x:=0 to 5 do
            begin
                putInt(x);
            end
        end

        """
        expect = "012345"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_28(self):

        input = """
        procedure main();
        var x:real;
        begin
            x := 1;
            putBool(x < 2);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,528))
    def test_29(self):

        input = """
        procedure main();
        var x:integer;
        begin
            for x:=0 to 5 do
            begin
                if(x<=2) then
                    putInt(x);
                else break;
            end
        end
        """
        expect = "012"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_30(self):

        input = """
        var x:integer;
        procedure main();
        begin
            for x:=5 downto 0 do
                putInt(x);
        end

        """
        expect = "543210"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_31(self):

        input = """
        function f():integer;
        begin
            return 1;
        end
        var x:integer;
        procedure main();
        begin
            putInt(f());
        end

        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_32(self):

        input = """
        
        procedure main();
        begin
            with
                x:integer;
                y:real;
            do begin
                x:=1;
                y:=x*x+5;
                putFloat(y);
            end
        end
        var x:integer;
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input,expect,532))
    def test_33(self):

        input = """
        function f():real;
        begin
            return 2.0;
        end
        
        procedure main();
        begin
            with
                y:integer;
                z:real;
                x:real;
            do begin

            for y:=5 downto 0 do
                putInt(y);
            
            end

        end

        var x:integer;

        """
        expect = "543210"
        self.assertTrue(TestCodeGen.test(input,expect,533))
    def test_34(self):
        input = """
        function f():integer;
        begin
            return 2; 
        end
        procedure main ();
        var x,y:real;
        begin
            with x,y:integer;
            do begin
                y := 5;
                for x:= y to 100 do
                begin
                    if(x>100)then
                        break;
                    else x:=x+50;
                end
                putInt(x);
            end
        end
        """
        expect = "107"
        self.assertTrue(TestCodeGen.test(input,expect,534))
    def test_35(self):
        input = """
        function giaithua(n:integer):integer;
        var GT,i:integer;
        begin
            GT:=1;
            for i:=1 to n do
                GT:=GT*i;
            return GT;
        end
        procedure main ();
        var x,y:real;
            n:integer;
        begin
            n:=5;
            putIntLn(giaithua(n));
        end
        """ 
        expect = "120\n"
        self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_37(self):
        input = """
        function tong(a,b:integer):integer;
        begin
            return a+b;
        end
        procedure main ();
        var x,y:real;
            n:integer;
        begin
            putIntLn(tong(1,2));
        end
        """ 
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    def test_38(self):
        input = """
        function square(x:integer):integer;
        begin
            return x*x;
        end
        procedure main ();
        begin
            putInt(square(3));
        end
        """ 
        expect = "9"
        self.assertTrue(TestCodeGen.test(input,expect,538))
    def test_39(self):
        input = """
        function sub(x,y:integer):integer;
        begin
            return x-y;
        end
        procedure main ();
        begin
            putInt(sub(1,2));
        end
        """ 
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,539))
    def test_40(self):
        input = """
        function tong(a,b:integer):integer;
        begin
            return a+b;
        end
        function square(x:integer):integer;
        begin
            return x*x;
        end
        function sub(x,y:integer):integer;
        begin
            return x-y;
        end
        procedure main ();
        begin
            putInt(square(sub(1,2)*tong(1,2)));
        end
        """ 
        expect = "9"
        self.assertTrue(TestCodeGen.test(input,expect,540))
    def test_41(self):
        input = """
        function cmp(a,b:integer):boolean;
        begin
            if (a-5)>b then return true;
            else return false;
        end
        procedure main ();
        var a,b:integer;
        begin
            a:=8;
            b:=2;
            if(cmp(a,b)) then putInt(a);
            else putInt(b);
        end
        """ 
        expect = "8"
        self.assertTrue(TestCodeGen.test(input,expect,541))
    def test_42(self):
        input = """
        procedure main ();
        var a,b,res:integer;
        begin
            a:=1;
            b:=1;
            res:=foo(a,b);
            putInt(res);
        end
        function foo(a,b:integer):integer;
        begin
            if(a=b) then return 111;
            else return 222;
        end
        """ 
        expect = "111"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    def test_43(self):
        input = """
        function giaithua(n:integer):integer;
        begin
            if(n=1) then return n;
            else return n*giaithua(n-1);
        end
        procedure main ();
        begin
            putIntLn(giaithua(5));
        end
        """ 
        expect = "120\n"
        self.assertTrue(TestCodeGen.test(input,expect,543))
    def test_44(self):
        input = """
        function fibonaci(n:integer):integer;
        begin
            if(n=0) then return 1;
            else
                if(n=1) then return 1;
                else return fibonaci(n-1)+fibonaci(n-2);
        end
        procedure main ();
        begin
            putIntLn(fibonaci(4));
        end
        """ 
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    def test_45(self):
        input = """
        function fact(x,n:integer):integer;
        begin
            if(n=0) then return 1;
            else return x*fact(x,n-1);
        end
        procedure main ();
        begin
            putInt(fact(3,3));
        end
        """ 
        expect = "27"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    def test_46(self):
        input = """
        function sumofdigit(n:integer):integer;
        begin
            if(n<10) then return n;
            else return (n mod 10) + sumofdigit(n div 10);
        end
        procedure main ();
        begin
            putInt(sumofdigit(1234));
        end
        """ 
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,546))
    def test_47(self):
        input = """
        function temp(n:integer):boolean;
        begin
            if(n=5) then return true;
            else return false;
        end
        procedure main ();
        begin
            putBool(temp(5));
        end
        """ 
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    def test_48(self):
        input = """
        procedure main ();
        begin
            putBool((1>2)or(2>1));
        end
        """ 
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,548))
    def test_49(self):
        input = """
        procedure main ();
        begin
            putBool((1>2)and(2>1));
        end
        """ 
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,549))

    def test_50(self):
        input = """
        procedure main ();
        begin
            putBool(((1>2)or(2>1))and(100<1000));
        end
        """ 
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,550))

    def test_51(self):
        input = """
        procedure main ();
        begin
            putBool((1>2)or(1>1)or(3<15.5));
        end
        """ 
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,551))
    def test_52(self):
        input = """
        procedure main ();
        begin
            putBool((1<2)or else(1>1)or else(3<15.5));
        end
        """ 
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,552))
    def test_53(self):
        input = """
        function b1():boolean;
        begin
            putStringLn("call b1");
            return true;
        end
        function b2():boolean;
        begin
            putStringLn("call b2");
            return true;
        end
        function b3():boolean;
        begin
            putStringLn("call b3");
            return true;
        end
        procedure main ();
        begin
            putBool(b1() or else b2() or else b3());
        end
        """ 
        expect = "call b1\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,553))

    def test_54(self):
        input = """
        function b1():boolean;
        begin
            putStringLn("call b1");
            return false;
        end
        function b2():boolean;
        begin
            putStringLn("call b2");
            return true;
        end
        function b3():boolean;
        begin
            putStringLn("call b3");
            return true;
        end
        procedure main ();
        begin
            putBool(b2() and then b1() and then b3());
        end
        """ 
        expect = "call b2\ncall b1\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_55(self):
        input = """
        procedure main ();
        begin
            putBool(true AND THEN false);
        end
        """ 
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_56(self):
        input = """
        function b1():boolean;
        begin
            putStringLn("call b1");
            return true;
        end
        function b2():boolean;
        begin
            putStringLn("call b2");
            return true;
        end
        function b3():boolean;
        begin
            putStringLn("call b3");
            return true;
        end
        procedure main ();
        begin
            putBool(b2() and then b1() or else b3());
        end
        """ 
        expect = "call b2\ncall b1\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,556))
    def test_57(self):
        input = """
        procedure main();
        var n,S,i:integer;
        begin 
            n:=10;
            S:=0;
            for i:=0 to n do
            begin
                S:=S+i;
            end
            putInt(S);
        end
        """ 
        expect = "55"
        self.assertTrue(TestCodeGen.test(input,expect,557))
    def test_58(self):
        input = """
        procedure main();
        var n,S,i:integer;
        begin 
            n := 10;
            S := 0;
            i := 0;
            while(i<n) do
            begin
                S:=S+i;
                i:=i+1;
            end
            putInt(S);
        end
        """ 
        expect = "45"
        self.assertTrue(TestCodeGen.test(input,expect,558))
    def test_59(self):
        input = """
        function tong_n(n:integer):integer;
        begin
            if(n=0) then  return n;
            return n+tong_n(n-1);
        end
        procedure main();
        var n:integer;
        begin
            n:=10;
            putInt(tong_n(n));
        end
        """ 
        expect = "55"
        self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_60(self):
        input = """
        function demsochuso(n:integer):integer;
        begin
            if(n<10) then  return 1;
            return 1+demsochuso(n div 10);
        end
        procedure main();
        var n:integer;
        begin
            n:=1000;
            putInt(demsochuso(n));
        end
        """ 
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,560))
    def test_61(self):
        input = """
        function max(a,b,c:integer):integer;
        var max:integer;
        begin
            if(a>b) then
                if(a>c) then max:=a;
                else max := c;
            else
                if(b>c) then max:=b;
                else max := c;
            return max;
        end
        procedure main();
        begin
            with
                a,b,c:integer;
            do begin
                a:=b:=c:=100;
                putInt(max(a,c,b));
            end
        end
        """ 
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,561))
    def test_62(self):
        input = """
        function max(a,b,c:integer):integer;
        var max:integer;
        begin
            if(a>b) then
                if(a>c) then max:=a;
                else max := c;
            else
                if(b>c) then max:=b;
                else max := c;
            return max;
        end
        procedure main();
        begin
            with
                a,b,c:integer;
                d:boolean;
            do begin
                a:=500;
                b:=c:=100;
                d:=c=b;
                putInt(max(a,b,c));
                if(d and (max(a,c,b)=a)) then putBool(d);
            end
        end
        """ 
        expect = "500true"
        self.assertTrue(TestCodeGen.test(input,expect,562))

    def test_63(self):
        input = """
        function UCLN(a,b:integer):integer;
        begin
            while(a<>b) do
            begin
                if(a>b) then a:= a-b;
            else b:=b-a;
            end
            return a;
        end
        procedure main();
        begin
            with
                a,b,c:integer;
                d:boolean;
            do begin
                a:=8;
                b:=4;
                putInt(UCLN(a,b));
            end
        end
        """ 
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,563))

    def test_64(self):
        input = """
        function UCLN(a,b:integer):integer;
        begin
            if(a>b) then return UCLN(a-b,b);
            else
                if(a<b) then return UCLN(a,b-a);
                else return a;
        end
        procedure main();
        begin
            with
                a,b,c:integer;
                d:boolean;
            do begin
                a:=8;
                b:=4;
                putInt(UCLN(a,b));
            end
        end
        """ 
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,564))

     # def test_65(self):

     #    input = """
     #    var a:integer;
     #    procedure main(); 
     #    begin 
     #        a:=5;
     #        putInt(a); 
     #    end"""
     #    expect = "5"
     #    self.assertTrue(TestCodeGen.test(input,expect,565))

    def test_66(self):
        """Simple program: int main() {} """
        input = """
        var a:integer;
        procedure main(); 
        begin 
            for a:=1 to 5 do
            begin
                putInt(a);
            end
        end"""
        expect = "12345"
        self.assertTrue(TestCodeGen.test(input,expect,566))
    def test_67(self):
        """Simple program: int main() {} """
        input = """
        var a:integer;
        procedure main(); 
        begin 
            for A:=1 to 5 do
            begin
                putINt(A);
            end
        end"""
        expect = "12345"
        self.assertTrue(TestCodeGen.test(input,expect,567))
    def test_68(self):
        """Simple program: int main() {} """
        input = """
        var A:integer;
        procedure main(); 
        begin 
            a:=10;
            putint(A);
        end"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,568))
    def test_69(self):
        """Simple program: int main() {} """
        input = """
        var x:real;
        procedure main(); 
        begin 
            x:=10;
            putfloat(X);
        end"""
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,569))
    def test_70(self):
        """Simple program: int main() {} """
        input = """
        var x:boolean;
        procedure main(); 
        begin 
            x:=10<5;
            X:= not x;
            putbool(x);
        end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,570))
    def test_71(self):
        """Simple program: int main() {} """
        input = """
        var x:boolean;
        procedure main(); 
        var x: real;
        begin 
            X:=10;
            putfloat(X);
        end"""
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,571))
    def test_72(self):
        """Simple program: int main() {} """
        input = """
        var x:boolean;
        procedure main(); 
        var x: real;
        begin 
            X:=10;
            putfloat(X);
            with
                x,y:boolean;
            do begin
                x:= false;
                putBool(x);
            end
        end"""
        expect = "10.0false"
        self.assertTrue(TestCodeGen.test(input,expect,572))
    def test_73(self):
        """Simple program: int main() {} """
        input = """
        var x:boolean;
        procedure main(); 
        var x: real;
        begin 
            X:=10;
            putfloat(X);
            with
                x,y:boolean;
            do begin
                x:= true;
                if(x) then putfloat(5);
            end
        end"""
        expect = "10.05.0"
        self.assertTrue(TestCodeGen.test(input,expect,573))
    def test_74(self):
        """Simple program: int main() {} """
        input = """
        var x:boolean;
        procedure main(); 
        var x: real;
        begin 
            X:=10;
            putfloat(X);
            with
                x,y:boolean;
            do begin
                with 
                    x:integer;
                do begin
                    x:=1;
                    putInt(x);
                end
            end
        end"""
        expect = "10.01"
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_75(self):
        """Simple program: int main() {} """
        input = """
        function sum(a,n:integer):integer;
        begin
            if n<0 then return 0;
            else return n + sum(a,n-1);
        end
        procedure main();
        var a,b:integer;
        begin
            a:=1;
            b:=9;
            PUTINT(sum(a,b));
        end
        """
        expect = "45"
        self.assertTrue(TestCodeGen.test(input,expect,575))
    def test_76(self):
        """Simple program: int main() {} """
        input = """
        function digit1(n:integer):integer;
        begin
            if n<10 then return n;
            return digit1(n div 10);
        end
        procedure main();
        var a,b:integer;
        begin
            PUTINT(digit1(14526));
            PUTINT(digit1(4526));
        end
        """
        expect = "14"
        self.assertTrue(TestCodeGen.test(input,expect,576))
    def test_78(self):
        """Simple program: int main() {} """
        input = """
        var x:boolean;
        procedure main();
        var a,b:integer;
        begin
            x:= 5>7;
            putbool(x);
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,578))
    def test_79(self):
        """Simple program: int main() {} """
        input = """
        var x:integer;
        procedure main();
        var a,b:integer;
        begin
            x := 9;
            putfloat(x);
        end
        """
        expect = "9.0"
        self.assertTrue(TestCodeGen.test(input,expect,579))
    def test_80(self):
        """Simple program: int main() {} """
        input = """
        var x:integer;
        procedure main();
        var a,b:integer;
        begin
            x := 9;
            putfloat(x);
        end
        """
        expect = "9.0"
        self.assertTrue(TestCodeGen.test(input,expect,580))
    def test_81(self):
        """Simple program: int main() {} """
        input = """
        function foo1(a,b:real):real;
        begin
            a:= a+b;
            b:= a-b;
            a:= a-b;
            return a;
        end
        procedure main();
        begin
            putFloat(foo1(1,9));  
        end
        """
        expect = "9.0"
        self.assertTrue(TestCodeGen.test(input,expect,581))
    def test_82(self):
        """Simple program: int main() {} """
        input = """
        function sum(a,b:real):real;
        begin
            return a+b;
        end
        procedure main();
        begin
            putFloat(sum(1,9));  
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,582))

    def test_83(self):
        """Simple program: int main() {} """
        input = """
        var f:real;
        function f1():real;
        begin
            return 10.2;
        end
        procedure main();
        var x:integer;
            y:real;
            z:boolean;
        begin
            f:= 10;
            putFloat(F);
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,583))
    def test_84(self):

        input = """
        var f:real;
        procedure main();
        var x:integer;
            y:real;
            z:boolean;
        begin
            putFloat(1/2);
        end
        """
        expect = "0.5"
        self.assertTrue(TestCodeGen.test(input,expect,584))
    def test_85(self):
        
        input = """
        var f:real;
        procedure main();
        var x:integer;
            y:real;
            z:boolean;
        begin
            putFloat(5/2);
        end
        """
        expect = "2.5"
        self.assertTrue(TestCodeGen.test(input,expect,585))
    def test_86(self):
        """Simple program: int main() {} """
        input = """
        var f:real;
        procedure main();
        var x:integer;
            y:real;
            z:boolean;
        begin
            putFloat(5/2);
        end
        """
        expect = "2.5"
        self.assertTrue(TestCodeGen.test(input,expect,586))
    def test_87(self):
        """Simple program: int main() {} """
        input = """
        function sum(a,b:real):real;
        begin
            return a+b;
        end
        procedure main();
        begin
            putbool(1<>2);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,587))
    def test_88(self):
        """Simple program: int main() {} """
        input = """
        procedure main();
        begin
            putFloat(5*-2.4);
        end
        """
        expect = "-12.0"
        self.assertTrue(TestCodeGen.test(input,expect,588))
    def test_89(self):
        """Simple program: int main() {} """
        input = """
        procedure main();
        var c:string;
        begin
            c:= "str";
            putBool(c="str");
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,589))
    def test_90(self):
        """Simple program: int main() {} """
        input = """
        procedure main();
        var c:string;
        begin
            c:= "str";
            putString(c);
        end
        """
        expect = "str"
        self.assertTrue(TestCodeGen.test(input,expect,590))
    def test_91(self):
        """Simple program: int main() {} """
        input = """
        procedure main();
        var c:string;
        begin
            putBool(0);
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,591))
    def test_92(self):
        """Simple program: int main() {} """
        input = """
        var a:string;
        procedure main();
        var c:string;
        begin
            a:= "UNNNDJ";
            putString(a);
        end
        """
        expect = "UNNNDJ"
        self.assertTrue(TestCodeGen.test(input,expect,592))
    def test_93(self):
        """Simple program: int main() {} """
        input = """
        var a:string;
        var e:integer;
        procedure main();
        var c:string;
        begin
            e:=0;
            while e < 5 do
            begin
                e:=e+1;
                if(e mod 2 =0) then continue;
                else putInt(e);
            end
        end
        """
        expect = "135"
        self.assertTrue(TestCodeGen.test(input,expect,593))
    def test_94(self):
        """Simple program: int main() {} """
        input = """
        function m():real;
        begin
            return 1.0;
        end
        procedure main();
        var c:string;
        begin
            putFloat(-m());
        end
        """
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input,expect,594))
    def test_95(self):
        """Simple program: int main() {} """
        input = """
        function m():real;
        begin
            return 1.0;
        end
        procedure main();
        var c:string;
        begin
            putBool(not not not true);
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,595))


