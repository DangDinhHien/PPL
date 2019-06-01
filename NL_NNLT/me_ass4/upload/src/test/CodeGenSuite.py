import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test10(self):
        input = """
function fact(x: integer): integer;
var i, f : integer;
begin
    f := 1;
    for i := 1 to x do f := f * i;
    return f;
end

procedure main();
var s, i : integer;
begin
    i := 1;
    s := 0;

    while i <= 10 do 
    begin
        putIntLn(fact(i));
        i := i + 1;
    end

end
        """
        expect = """1
2
6
24
120
720
5040
40320
362880
3628800
"""
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test11(self):
        input = """
procedure main();
var s, i, j : integer;
begin
    i := 1;

    while i <= 10 do 
    begin
        if (i > 4) and (i < 7) then 
        begin
            i := i + 1;
            continue;
        end

        s := 0;
        for j := i * 10 to (i + 1)*10 do
        begin
            if (j mod 2 = 0) then continue;
            s := s + j;
        end
        putInt(i);
        putString(", ");
        putInt(s);
        putLn();
        i := i + 1;
    end

end

function fact(x: integer): integer;
var i, f : integer;
begin
    f := 1;
    for i := 1 to x do f := f * i;
    return f;
end
        """
        expect = """1, 75
2, 125
3, 175
4, 225
7, 375
8, 425
9, 475
10, 525
"""
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test12(self):
        input = """
procedure main();
var s, i, j : integer;
begin
    i := 1;
    putIntLn(fact(7));
end

function fact(x: integer): integer;
begin
    if x < 2 then
        return 1;
    else
    return x * fact(x - 1);
end
        """
        expect = """5040\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 512))


    def test17(self):
        input = """
       procedure main();
       var x: integer;
       begin
            x := 1;
            with x : integer; do 
            begin
                x := 2;
                with x : integer; do
                begin
                    x := 3;
                    putInt(x);
                end
                putInt(x);
            end
       end
        """
        expect = """32"""
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test18(self):
        input = """

    var x: integer;
    
    function foo(): boolean;
    begin
        putString("in foo");
        return false;
    end

    procedure main();
    begin
        x := 10;
        if (x > 100 and then foo()) then
            putStringLn("in then");
        else
            putStringLn("in else");
    end
        """
        expect = """in else\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test20(self):
        input = """
    var x: integer;
    
    function foo(): boolean;
    begin
        putString("in foo ");
        x := 1000;
        return true;
    end

    procedure main();
    begin
        x := 10;

        if (x < 100 and then foo()) then
            putStringLn("in then");
        else
            putStringLn("in else");
    end        """
        expect = """in foo in then\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test19(self):
        input = """
    var x: integer;
    
    function foo(): boolean;
    begin
        putString("in foo ");
        return false;
    end

    procedure main();
    begin
        x := 10;

        if (x < 100 and then foo()) then
            putStringLn("in then");
        else
            putStringLn("in else");
    end        """
        expect = """in foo in else\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test21(self):
        input = """
    var x: integer;
    
    function foo(): boolean;
    begin
        putString("in foo ");
        x := 1000;
        return true;
    end

    procedure main();
    begin
        x := 10;

        if (x > 100 and then foo()) then
            putStringLn("in then");
        else
            putStringLn("in else");

        putIntLn(x);
    end        """
        expect = """in else\n10\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test22(self):
        input = """
       function foo(): real;
       begin
            return 1;
        end

        procedure main();
        begin
            putFloat(foo());
        end
        """
        expect = """1.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test23(self):
        input = """
        procedure main();
        var x, y: integer;
        begin
            x := 10;
            y := 12;
            putInt(gcd(x + y, x));
        end

        function gcd(a,b : integer): integer;
        begin
            if b = 0 then
                return a;
            else
                return gcd(b, a mod b);
        end        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input, expect, 523))


    def test34(self):
        input = """
		procedure main();
		var x: integer;
		begin
			x := 10;
			foo(x);
			putFloat(x);
		end

		procedure foo(x: real);
		begin
			putFloat(x);
		end        """
        expect = """10.010.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 534))

#     def test35(self):
#         input = """
# 		procedure main();
# 		var x: array[-5 .. 5] of integer; y: integer;
# 		begin
# 			x := foo(-3);
# 			putIntLn(x[-3]);
# 			y := 12;
# 			putIntLn(y);
# 		end

# 		function foo(x: integer): array[-5 .. 5] of integer;
# 		var a: array[-5 .. 5] of integer;
# 		begin
# 			a[-3] := 10;
# 			a[x] := a[x] + x*x;
# 			putIntLn(a[-3]);
# 			return a;
# 		end        """
#         expect = """19
# 19
# 12
# """
#         self.assertTrue(TestCodeGen.test(input, expect, 535))



    def test38(self):
        input = """
        var i: integer;
        procedure main();
        begin
            foo();
            putInt(i);
        end

        procedure foo();
        begin
            i := 100;
        end
        """
        expect = """100"""
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test39(self):
        input = """
        var x: integer;

        procedure main();
        var n, i, j : integer;
        begin
            n := 10;
            for i := 1 to n do
            begin
                for j := 1 to i do
                    putString("*");
                putLn();
            end
        end

        """
        expect = """*
**
***
****
*****
******
*******
********
*********
**********
"""
        self.assertTrue(TestCodeGen.test(input, expect, 539))


    def test41(self):
        input = """
        var x: integer;
        procedure main();

        begin
            for x := 0 to 0 do
                continue;
            putInt(x);

        end
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test42(self):
        input = """
        function fib(x : integer):integer;
        begin
            if (x < 2) then return 1;
            return fib(x-1) + fib(x-2);
        end

        procedure main();
        var x : integer;

        begin
            putInt(fib(5));
        end
        """
        expect = """8"""
        self.assertTrue(TestCodeGen.test(input, expect, 542))


    def test46(self):
        input = """
        procedure main();
        var i, sum: integer; 
        begin

            i := 0;
            sum := 0;

            while i < 100 do begin
                sum := sum +i;
                i := i + 1;
            end

            putInt(sum);

            sum := sum + 100;

            putInt(sum);

        end
        """
        expect = """49505050"""
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test47(self):
        input = """
        procedure main();
        var i, j: integer;
        begin
            i := 0;
            while i < 10 do begin
                for j := 0 to 10 do begin
                    if j mod 2 = 0 then continue;
                    putIntLn(foo(i, j));
                end
                if i > 2 then break; 
                i := i + 1;
            end
        end

        function foo(i, j: integer): integer;
        begin
            return i*10 + j;
        end
        """
        expect = """1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
"""
        self.assertTrue(TestCodeGen.test(input, expect, 547))


    def test50(self):
        input = """
        procedure main();
        var X: integer;
        begin
            x := 12;
            putint(X);
            Foo();
        end

        procedure foo();
        begin
            putString("Hello world");
        end
        """
        expect = """12Hello world"""
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_assign3(self):
        input = """
            var d: integer;
            procedure main();
            var a,b: boolean;
                c: String;
            begin
                a := True;
                b := False;
                c := "ahihi";
                d := 1 + 2;
                putBool(a or b and not b or False);
                putString(c);
                putInt(d);
            end
        """
        expect = "trueahihi3"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_scope1(self):
        input = """
            procedure main();
            var a: integer;
                b: real;
            begin
                a := 1;
                putInt(a);
                with a: real; b: integer; do begin
                    a := 1.5;
                    b := 1;
                    putFloat(a+b+0.15);
                end
                with a: boolean ; b: boolean; do begin
                    b := true;
                    a := b;
                    putBool(a);
                end
                a := a + 2;
                putInt(3);
            end
        """
        expect = "12.65true3"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_while1(self):
        input = """
            procedure main();
            var a,i: integer;
                b: real;
            begin
                i := 8 ;
                a := 1 ;
                while (i>0) do begin
                    a := a * i;
                    i := i - 1;
                    if i = 4 then break;
                end
                putInt(a);
            end
            """
        expect = "1680"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_bool_ast5(self):
        input = """
            procedure main();
            var a,b: boolean;
            begin
                a := True;
                b := False;
                putbool(a and b and then a and not b and test());
            end
            function test(): boolean;
            var a: real;
                res: boolean;
            begin
                res := false;
                a := 9.5;
                putFloat(a);
                return res;
            end
            """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_bool_ast6(self):
        input = """
            procedure main();
            var a,b: boolean;
            begin
                a := True;
                b := False;
                putBool((a or test()) or else a and not b and test());
            end
            function test(): boolean;
            var a: real;
                res: boolean;
            begin
                res := false;
                a := 9.5;
                putFloat(a);
                return res;
            end
            """
        expect = "9.5true"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_for1(self):
        input = """
            procedure main();
            var a,i: integer;
                b: real;

            begin
                up := 10;
                a := 0;
                for i:=up downto 1 do begin
                    if a > 40 then continue;
                    a := a + i;
                end
                putInt(a);
            end
            var up:integer;
            """
        expect = "45"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_call_stmt1(self):
        input = """
            procedure main();
            var a,b: integer;
            begin
                b := 6;
                a := factor(b);
                putInt(a);
            end
            function factor(a: integer): integer;
            begin
                if a <= 1 then
                    return 1;
                else
                    return a * factor(a-1);
            end
        """
        expect = "720"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test64(self):
        input = """
            procedure main();
            var a,b: integer;
            begin
                b := 6;
                a := factor(b);
                putInt(a);
            end
            function factor(a: integer): integer;
            begin
                if a <= 1 then
                    return 1;
                else
                    return a * factor(a-1);
            end
        """
        expect = """720"""
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test99(self):
        input = """
        procedure main();
        begin
        end
        """
        expect = """"""
        self.assertTrue(TestCodeGen.test(input, expect, 599))
