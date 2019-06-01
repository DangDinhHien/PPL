import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):    
    def test_funccall(self):
        """More complex program"""
        input = """
        function foo (c,d : integer):INTEGER;
        var d : real;
        begin
        end"""
        #expect param : name, param, local, body, returnType
        expect = str(Program([
            FuncDecl(Id("foo"),
            [VarDecl(Id("c"),IntType()),VarDecl(Id("d"),IntType())],
            [VarDecl(Id("d"),FloatType())],
            [],
            IntType())]))
        self.assertTrue(TestAST.test(input,expect,304))
    
    def test_arrayvar(self):
        input = """
        var a : array [1 .. 4] of integer;
        """
        expect = str(Program([VarDecl(Id("a"),ArrayType("1","4",IntType()))]))
        self.assertTrue(TestAST.test(input,expect,305))
    
    def test_simple_assign(self):
        input = """
        function main ():real;
        begin
            a:=c;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
            [],
            [],
            [Assign(Id("a"),Id("c"))],
            FloatType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_simple_procedure(self):
        input = """
        procedure main();
        var x : string;
        begin 
        end
        """
        expect = str(Program([
            FuncDecl(Id("main"),
            [],
            [VarDecl(Id("x"),StringType())],
            [],
            VoidType())]))
        self.assertTrue(TestAST.test(input,expect,307))
    
    def test_simple_assign_with_idexp(self):
        input = """
        procedure main();
        begin
            a[2] := k;
        end 
        """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(ArrayCell(Id("a"),IntLiteral(2)),Id("k"))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,308))
    
    def test_simple_while(self):
        input = """
        procedure main();
        begin
            while (a>3) do a:=b;
        end 
        """
        expect = str(
            Program([FuncDecl(Id("main"),
            [],
            [],
            [While(BinaryOp(">",Id("a"),IntLiteral(3)),[Assign(Id("a"),Id("b"))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,309))
    
    def test_simple_if(self):
        input = """
        procedure main();
        begin
            if(a>=3) then a:=3;
        end 
        """
        expect = str(Program([
            FuncDecl(Id("main"),
            [],
            [],
            [If(BinaryOp(">=",Id("a"),IntLiteral(3)),[Assign(Id("a"),IntLiteral(3))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,310))
    
    def test_complex_if(self):
        input = """
        procedure main();
        begin
            if(a>3) then 
                if(a<4) then
                    a := a+1;
        end 
        """
        expect = str(Program([
            FuncDecl(Id("main"),[],[],
            [If(BinaryOp(">",Id("a"),IntLiteral(3)),
            [If(BinaryOp("<",Id("a"),IntLiteral(4)),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,311))
    
    def test_simple_for(self):
        input = """
        procedure main();
        begin
            for x:=1 to 10 do a:=a+1;
        end 
        """
        expect = str(Program([
            FuncDecl(Id("main"),[],[],
            [For(Id("x"),IntLiteral(1),IntLiteral(10),True,[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],
            VoidType())]))
        self.assertTrue(TestAST.test(input,expect,312))
    
    def test_special_exp0(self): 
        input = """
        procedure main();
        begin
            if(x=true) then a[2]:=-a[3];
        end 
        """
        expect = str(Program([
            FuncDecl(Id("main"),[],[],
            [If(BinaryOp("=",Id("x"),BooleanLiteral(True)),[Assign(ArrayCell(Id("a"),IntLiteral(2)),UnaryOp("-",ArrayCell(Id("a"),IntLiteral(3))))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,313))
    
    def test_special_exp1(self):
        input = """
        procedure main();
        begin
            if(x=true) then a[2]:=-a[3]+a[q[2]]*10;
        end 
        """
        expect = str(Program([
            FuncDecl(Id("main"),[],[],
            [If(BinaryOp("=",Id("x"),BooleanLiteral(True)),
            [Assign(ArrayCell(Id("a"),IntLiteral(2)),BinaryOp("+",UnaryOp("-",ArrayCell(Id("a"),IntLiteral(3))),BinaryOp("*",ArrayCell(Id("a"),ArrayCell(Id("q"),IntLiteral(2))),IntLiteral(10))))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,314))
    
    def test_funccall(self):
        input = """
        procedure main();
        begin
            func(a,1);
        end 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        [],
                        [CallStmt(Id("func"),[Id("a"),IntLiteral(1)]
                        )])])
        )
        self.assertTrue(TestAST.test(input,expect,315))
    
    def test_special_exp2(self):
        input = """
        procedure main();
        begin
            if (a>10) then 
            begin 
                s:=1;
                func()[s] := s+1; 
            end
        end 
        """
        expect = str(Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    [If(BinaryOp(">",Id("a"),IntLiteral(10)),[Assign(Id("s"),IntLiteral("1")),
                    Assign(ArrayCell(CallExpr(Id("func"),[]),Id("s")),BinaryOp("+",Id("s"),IntLiteral(1)))],[])],
                    VoidType())]))
        self.assertTrue(TestAST.test(input,expect,316))
    
    def test_special_exp3(self):
        input = """
        procedure main();
        begin
            while (a>5) do
                begin
                    s:=s/s[i];
                    print(func(a,b)[s]);
                end
        end 
        """
        expect = str(Program(
            [
                FuncDecl(
                    Id("main"),
                    [],[],
                    [While(BinaryOp(">",Id("a"),IntLiteral(5)),[Assign(Id("s"),BinaryOp("/",Id("s"),ArrayCell(Id("s"),Id("i")))),CallStmt(Id("print"),[ArrayCell(CallExpr(Id("func"),[Id("a"),Id("b")]),Id("s"))])])],VoidType())])

        )
        self.assertTrue(TestAST.test(input,expect,317))
    
    def test_many_variable_decl(self):
        input = """
        var a,b:integer;c:array[1 .. 10] of real; str : string;
        """
        expect = str(
            Program(
                [VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType("1","10",FloatType())),VarDecl(Id("str"),StringType())])
        )
        self.assertTrue(TestAST.test(input,expect,318))
    
    def test_some_funcall(self):
        input = """
        procedure main();
        begin
            sum(a,b);
            print("Hello world");
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],
            [],
            [CallStmt(Id("sum"),[Id("a"),Id("b")]),CallStmt(Id("print"),[StringLiteral("Hello world")])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,319))
    

    def test_many_func1(self):
        input = """
        function sum(a:integer; b:integer):integer;
        begin
            return a+b;
        end
        procedure main();
        begin
            print(sum(a,b));
        end
        """
        expect = str(Program(
            [FuncDecl(Id("sum"),
            [VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],
            [],
            [Return(BinaryOp("+",Id("a"),Id("b")))],IntType()),
            FuncDecl(Id("main"),[],[],
            [CallStmt(Id("print"),[CallExpr(Id("sum"),[Id("a"),Id("b")])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,320))
    
    def test_many_func(self):
        input = """
        function print(a : string): string;
        begin 
        end
        function sum(a : array[1 .. 5] of real):real;
        begin
        end
        procedure main();
        begin
        end
        """
        expect = str(
            Program(
                [FuncDecl(Id("print"),[VarDecl(Id("a"),StringType())],[],[],StringType()),
                FuncDecl(Id("sum"),[VarDecl(Id("a"),ArrayType("1","5",FloatType()))],[],[],FloatType()),
                FuncDecl(Id("main"),[],[],[],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,321))

    def test_simple_realnumber(self):
        input = """
        procedure main();
        begin
            number := 2e-2;
            hack(number);
        end
        """
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [Assign(Id("number"),FloatLiteral("2e-2")),CallStmt(Id("hack"),[Id("number")])],VoidType())])    
        )        
        self.assertTrue(TestAST.test(input,expect,322))

    def test_compound_stm0(self):
        input = """
        procedure main();
        begin 
            while(true) do
                begin
                    a:=(a*1+2)/3;
                    is := true;
                end
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),
            [],
            [],
            [While(BooleanLiteral(True),[Assign(Id("a"),BinaryOp("/",BinaryOp("+",BinaryOp("*",Id("a"),IntLiteral(1)),IntLiteral(2)),IntLiteral(3))),
            Assign(Id("is"),BooleanLiteral(True ))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,323))
    
    def test_compound_stm1(self):
        input = """
        procedure main();
        begin 
            while(a = 10) do
                begin
                    if (a<20) then 
                        a := -func(pass);
                end
        end
        """
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [While(BinaryOp("=",Id("a"),IntLiteral(10)),
                    [If(BinaryOp("<",Id("a"),IntLiteral(20)),
                        [Assign(Id("a"),UnaryOp("-",CallExpr(Id("func"),[Id("pass")])))],[])])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,324))

    def test_compound_stm2(self):
        input = """
        procedure main();
        begin 
            if (a>10) then
                while (a<15) do
                    s := s+1;
        end
        """
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [If(BinaryOp(">",Id("a"),IntLiteral(10)),
                    [While(BinaryOp("<",Id("a"),IntLiteral(15)),[Assign(Id("s"),BinaryOp("+",Id("s"),IntLiteral(1)))])],[])],
                    VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,325))

    def test_compound_stm3(self):
        input = """
        procedure main();
        begin 
            if (a>10) then
                while (a<15) do
                    s := s+1;
            else
                s := s;
        end
        """
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],[],
                [If(BinaryOp(">",Id("a"),IntLiteral(10)),
                    [While(BinaryOp("<",Id("a"),IntLiteral(15)),
                        [Assign(Id("s"),BinaryOp("+",Id("s"),IntLiteral(1)))])],[Assign(Id("s"),Id("s"))])],
                        VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,326))
    
    def test_compound_stm4(self):
        input = """
        procedure main();
        begin 
            if (a>10) then
                while (a<15) do
                    s := s+1;
            else
                print("Dont do everythg");
        end
        """
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],[],
                [If(BinaryOp(">",Id("a"),IntLiteral(10)),
                    [While(BinaryOp("<",Id("a"),IntLiteral(15)),
                        [Assign(Id("s"),BinaryOp("+",Id("s"),IntLiteral(1)))])],[CallStmt(Id("print"),[StringLiteral("Dont do everythg")])])],
                        VoidType())])
        )
        
        self.assertTrue(TestAST.test(input,expect,327))
    

    def test_many_assign(self):
        input = """
        function main ():real;
        begin
            a:=b:=c:=exp;
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [Assign(Id("c"),Id("exp")),Assign(Id("b"),Id("c")),Assign(Id("a"),Id("b"))],
                FloatType())])
        )
        self.assertTrue(TestAST.test(input,expect,328))

    def test_special_exp4(self):
        input = """
        function main ():string;
        begin
            test := -(1+2*3/4-5);
        end"""
        expect = str(
            Program([
                FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("test"),UnaryOp("-",BinaryOp("-",BinaryOp("+",IntLiteral(1),BinaryOp("/",BinaryOp("*",IntLiteral(2),IntLiteral(3)),IntLiteral(4))),IntLiteral(5))))]
                ,StringType())])
        )
        self.assertTrue(TestAST.test(input,expect,329))
    
    def test_special_exp5(self):
        input = """
        function main ():string;
        begin
            test := 6*3 and then 3;
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [Assign(Id("test"),BinaryOp("andthen",BinaryOp("*",IntLiteral(6),IntLiteral(3)),IntLiteral(3)))],StringType())
                ])
        )
        self.assertTrue(TestAST.test(input,expect,329))

    def test_complex_funcall(self):
        input = """ Procedure main();
                    begin 
                        func(3,a+1,m(2));
                    end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [CallStmt(Id("func"),[IntLiteral(3),BinaryOp("+",Id("a"),IntLiteral(1)),CallExpr(Id("m"),[IntLiteral(2)])])],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,330))

    def test_cp_with_manyexp(self):
        input = """ Procedure main();
                    begin 
                        begin
                            s:=s+1;
                            s:=s*2;
                            a:=-6--5+2;
                        end
                    end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [Assign(Id("s"),BinaryOp("+",Id("s"),IntLiteral(1))),
                Assign(Id("s"),BinaryOp("*",Id("s"),IntLiteral(2))),
                Assign(Id("a"),BinaryOp("+",BinaryOp("-",UnaryOp("-",IntLiteral(6)),UnaryOp("-",IntLiteral(5))),IntLiteral(2)))],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,331))
    
    def test_cp_with_manyexp(self):
        input = """ procedure main();
                    begin
                        with a : real; m: array[1 .. 4] of real;
                        do
                            While (A=10) Do Sum:=Sum+1;
                    end
                    """
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [With([VarDecl(Id("a"),FloatType()),VarDecl(Id("m"),ArrayType("1","4",FloatType()))],
                [While(BinaryOp("=",Id("A"),IntLiteral(10)),[Assign(Id("Sum"),BinaryOp("+",Id("Sum"),IntLiteral(1)))])])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,332))
    
    def test_simple_for1(self):
        input = """ procedure main();
                    begin
                        for i:=1 to 10 do mul := mul - 1;
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],[],
            [For(Id("i"),IntLiteral(1),IntLiteral("10"),True,[Assign(Id("mul"),BinaryOp("-",Id("mul"),IntLiteral(1)))])],
            VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,333))
    
    def test_break_stm(self):
        input = """ procedure main();
                    begin
                        while (true) do 
                            begin
                                s:=s+1;
                                break;
                            end
                    end
                    """
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [While(BooleanLiteral(True),[Assign(Id("s"),BinaryOp("+",Id("s"),IntLiteral(1))),Break()])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,334))
    
    def test_compound_stm5(self):
        input = """ procedure main();
                    begin
                        begin
                        end
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],[],[],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,335))

    def test_compound_type(self):
        input = """ procedure main();
                    var test : array[-1 .. 1] of string;
                    begin
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],[VarDecl(Id("test"),ArrayType("-1","1",StringType()))],[],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,336))
    
    def test_float_etype(self):
        input = """ procedure main();
                    begin
                        a:=1.2;
                        b:=2e-2;
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),FloatLiteral(1.2)),Assign(Id("b"),FloatLiteral(2e-2))],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,337))
    
    def test_float_etype(self):
        input = """ procedure main();
                    begin
                        a:=1.2;
                        b:=2e-2;
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),FloatLiteral(1.2)),Assign(Id("b"),FloatLiteral("2e-2"))],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,337))
    
    def test_complex_if1(self):
        input = """ procedure main();
                    begin
                        if (a>10) then
                            if(a<10) then
                                a:=10;
                            else
                                a:=11;
                    end
                    """
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],[If(BinaryOp(">",Id("a"),IntLiteral(10)),
                [If(BinaryOp("<",Id("a"),IntLiteral(10)),[Assign(Id("a"),IntLiteral(10))],[Assign(Id("a"),IntLiteral(11))])],[])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,338))
    
    def test_program1(self):
        input = """ procedure main();
                    var a : array[-1 .. 1] of string;
                    begin
                        while ((a<=10) and (b=true)) do
                            begin
                                l:=l+func(a);
                            end
                    end
                    """
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[VarDecl(Id("a"),ArrayType("-1","1",StringType()))],
                [While(BinaryOp("and",BinaryOp("<=",Id("a"),IntLiteral(10)),BinaryOp("=",Id("b"),BooleanLiteral(True))),
                [Assign(Id("l"),BinaryOp("+",Id("l"),CallExpr(Id("func"),[Id("a")])))])],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,339))

    def test_program2(self):
        input = """ procedure main();
                    begin
                        a := b[a]/2;
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],[],
            [Assign(Id("a"),BinaryOp("/",ArrayCell(Id("b"),Id("a")),IntLiteral(2)))],
            VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,340))

    def test_program3(self):
        input = """ function main(n:real):real;
                    var x : real;
                    begin
                        x := 10;
                        for i:=1 downto n do
                            x:=x div i;
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),
            [VarDecl(Id("n"),FloatType())],
            [VarDecl(Id("x"),FloatType())],
            [Assign(Id("x"),IntLiteral(10)),
            For(Id("i"),IntLiteral(1),Id("n"),False,[Assign(Id("x"),BinaryOp("div",Id("x"),Id("i")))])],
            FloatType())])
        )
        self.assertTrue(TestAST.test(input,expect,341))
    
    def test_program4(self):
        input = """ function main(n:real):real;
                    var x : real;
                    begin
                        x := 10;
                        for i:=1 downto n do
                            x:=x div i;
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),
            [VarDecl(Id("n"),FloatType())],
            [VarDecl(Id("x"),FloatType())],
            [Assign(Id("x"),IntLiteral(10)),
            For(Id("i"),IntLiteral(1),Id("n"),False,[Assign(Id("x"),BinaryOp("div",Id("x"),Id("i")))])],
            FloatType())])
        )
        self.assertTrue(TestAST.test(input,expect,341))
    
    def test_program5(self):
        input = """ var a : real;
                    var b : string;
                    procedure main();
                    begin
                        if((a=1) or (a=2)) then
                            begin
                                print();
                            end
                    end
                    """
        expect = str(
            Program(
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),StringType()),
                FuncDecl(Id("main"),[],[],
                [If(BinaryOp("or",BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("a"),IntLiteral(2))),[CallStmt(Id("print"),[])],[])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,342))
    
    def test_program6(self):
        input = """ procedure main();
                    begin
                        func(arra(1),z[1]);
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],[],
            [CallStmt(Id("func"),[CallExpr(Id("arra"),[IntLiteral(1)]),ArrayCell(Id("z"),IntLiteral(1))])],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,343))

    def test_complex_if2(self):
        input = """ procedure main();
                    begin
                        if (true) then
                            if(true) then
                                call1();
                            else
                                call2();
                        else
                            call3();
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],[],
            [If(BooleanLiteral(True),
                [If(BooleanLiteral(True),
                    [CallStmt(Id("call1"),[])],[CallStmt(Id("call2"),[])])],[CallStmt(Id("call3"),[])])],
            VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,344))
    
    def test_complex_if3(self):
        input = """ procedure main();
                    begin
                        if (true) then
                            if(true) then
                                call1();
                        else
                            call3();
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),
            [],
            [],
            [If(BooleanLiteral(True),[If(BooleanLiteral(True),[CallStmt(Id("call1"),[])],[CallStmt(Id("call3"),[])])],[])],
            VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,345))
    
    def test_many_assign1(self):
        input = """ function main():real;
                    begin
                        a:=b:=foo();
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],[],[Assign(Id("b"),CallExpr(Id("foo"),[])),Assign(Id("a"),Id("b"))],FloatType())])
        )
        self.assertTrue(TestAST.test(input,expect,346))

    def test_special_exp6(self):
        input = """ procedure main();
                    var a : boolean;
                    begin
                        a:=true;
                        b:= not a;
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],
            [VarDecl(Id("a"),BoolType())],[Assign(Id("a"),BooleanLiteral(True)),Assign(Id("b"),UnaryOp("not",Id("a")))],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,347))

    def test_special_exp7(self):
        input = """ procedure main();
                    var a : integer;
                    begin
                        a := 1;
                        b:= --a;
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],
            [VarDecl(Id("a"),IntType())],
            [Assign(Id("a"),IntLiteral(1)),Assign(Id("b"),UnaryOp("-",UnaryOp("-",Id("a"))))],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,348))
    
    def test_special_exp8(self):
        input = """ procedure main();
                    var a : integer;
                    begin
                        a := 1;
                        b:= not not q;
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],
            [VarDecl(Id("a"),IntType())],
            [Assign(Id("a"),IntLiteral(1)),Assign(Id("b"),UnaryOp("not",UnaryOp("not",Id("q"))))],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,349))

    def test_special_exp9(self):
        input = """ procedure main();
                    var a : integer;
                    //var b : real 
                    //skip this 
                    begin
                        a := 1;
                        b:= not not q;
                    end
                    """
        expect = str(
            Program([FuncDecl(Id("main"),[],
            [VarDecl(Id("a"),IntType())],
            [Assign(Id("a"),IntLiteral(1)),Assign(Id("b"),UnaryOp("not",UnaryOp("not",Id("q"))))],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,350))
    
    def test_special_exp10(self):
        input = """ procedure main();
                    begin
                        hello(b mod q);
                    end
                    """
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [CallStmt(Id("hello"),[BinaryOp("mod",Id("b"),Id("q"))])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,351))
    
    def test_special_exp11(self):
        input = """
        function main(x,y : real): real;
        var xy:real;
        begin
            for i:=1 to n do
                begin
                    putInt(5);
                end
        end """
        expect = str(Program(
            [FuncDecl(Id("main"),
            [VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType())],
            [VarDecl(Id("xy"),FloatType())],
            [For(Id("i"),IntLiteral(1),Id("n"),True,[CallStmt(Id("putInt"),[IntLiteral(5)])])],
            FloatType())]))
        self.assertTrue(TestAST.test(input,expect,352))
    
    def test_special_exp12(self):
        input = """
        function main(x,y : real): real;
        var xy:real;
        begin
            for i:=1 to n do
                begin
                    if (a <> b) then a:=a+1;
                end
        end """
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType())],
                [VarDecl(Id("xy"),FloatType())],
                [For(Id("i"),IntLiteral(1),Id("n"),True,
                [If(BinaryOp("<>",Id("a"),Id("b")),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],[])])],
                FloatType())])
        )
        self.assertTrue(TestAST.test(input,expect,353))
    
    def test_compound_stm6(self):
        input = """
        procedure main();
        begin 
            A(b[func(x)]);
        end
        """
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [CallStmt(Id("A"),[ArrayCell(Id("b"),CallExpr(Id("func"),[Id("x")]))])],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,354))
    
    def test_compound_stm7(self):
        input = """
        procedure main();
        begin 
            if(a > func[a]) then
            begin 
                a := -a;
            end
        end
        """
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [If(BinaryOp(">",Id("a"),ArrayCell(Id("func"),Id("a"))),[Assign(Id("a"),UnaryOp("-",Id("a")))],[])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,355))
    
    def test_program7(self):
        input = """
        var bin : array [1 .. 10] of string;
        procedure main();
        begin 
            if(a > func[a]) then
            begin 
                a := -a;
            end
        end
        """
        expect = str(
            Program(
                [VarDecl(Id("bin"),ArrayType("1","10",StringType())),
                FuncDecl(Id("main"),
                [],
                [],
                [If(BinaryOp(">",Id("a"),ArrayCell(Id("func"),Id("a"))),[Assign(Id("a"),UnaryOp("-",Id("a")))],[])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,356))

    def test_program8(self):
        input = """
        var bin : array [1 .. 10] of string;
        procedure main();
        begin 
            if(a >= func[a]) then
            begin 
                a := -a;
            end
        end
        """
        expect = str(
            Program(
                [VarDecl(Id("bin"),ArrayType("1","10",StringType())),
                FuncDecl(Id("main"),[],[],
                [If(BinaryOp(">=",Id("a"),ArrayCell(Id("func"),Id("a"))),[Assign(Id("a"),UnaryOp("-",Id("a")))],[])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,357))

    def test_program9(self):
        input = """
        var bin : string;
        procedure main();
        begin 
            if(a >= func[a]) then
            begin 
                a := -a;
            end
        end
        """
        expect = str(
            Program(
                [VarDecl(Id("bin"),StringType()),
                FuncDecl(Id("main"),[],[],
                [If(BinaryOp(">=",Id("a"),ArrayCell(Id("func"),Id("a"))),[Assign(Id("a"),UnaryOp("-",Id("a")))],[])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,358))
    
    def test_program10(self):
        input = """
        procedure main();
        begin 
            x := a >= b;
        end
        """
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("x"),BinaryOp(">=",Id("a"),Id("b")))],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,359))
    
    def test_program11(self):
        input = """
        procedure main();
        begin 
            x := a >= b;
        end
        """
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("x"),BinaryOp(">=",Id("a"),Id("b")))],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,360))
    
    def test_program12(self):
        input = """
        procedure main();
        begin 
            n := not q;
            n := -1 * 3;
        end
        """
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("n"),UnaryOp("not",Id("q"))),Assign(Id("n"),BinaryOp("*",UnaryOp("-",IntLiteral(1)),IntLiteral(3)))],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,361))
    
    def test_program13(self):
        input = """ 
        Procedure main();
        begin
            a:= 1.25;
            b:= 1. ;
            c:= .1 ;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("a"),FloatLiteral(1.25)),
                Assign(Id("b"),FloatLiteral(1.0)),
                Assign(Id("c"),FloatLiteral(0.1))
                ],
                VoidType())]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_program14(self):
        input = """ 
        Procedure main();
        begin
            q[a] := 1*fung(fung());
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [Assign(ArrayCell(Id("q"),Id("a")),BinaryOp("*",IntLiteral(1),CallExpr(Id("fung"),[CallExpr(Id("fung"),[])])))],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,363))

    def test_program15(self):
        input = """ 
        Procedure main();
        begin
            m1 := q(1,2)[w[1.2]];
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [Assign(Id("m1"),ArrayCell(CallExpr(Id("q"),[IntLiteral(1),IntLiteral(2)]),ArrayCell(Id("w"),FloatLiteral(1.2))))],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,364))
    
    def test_program16(self):
        input = """ 
        Procedure main();
        begin
            _m1 := q(1,2)[w[1.2]];
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [Assign(Id("_m1"),ArrayCell(CallExpr(Id("q"),[IntLiteral(1),IntLiteral(2)]),ArrayCell(Id("w"),FloatLiteral(1.2))))],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,365))

    def test_program17(self):
        input = """ 
        Procedure main();
        begin
            for id:=1 downto n do 
                begin
                end
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],[For(Id("id"),IntLiteral(1),Id("n"),False,[])],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,366))
    
    def test_program18(self):
        input = """ 
        Procedure main();
        begin
            for id:=1 downto n do 
                begin
                    compare(max(1),min[1]);
                end
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],[For(Id("id"),IntLiteral(1),Id("n"),False,
                [CallStmt(Id("compare"),[CallExpr(Id("max"),[IntLiteral(1)]),ArrayCell(Id("min"),IntLiteral(1))])])],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,367))
    
    def test_program19(self):
        input = """ 
        Procedure main();
        begin
            for id:=1 downto n do 
                begin
                    if(m mod 2 = 0) then println("m");
                    else 
                        begin
                            iNum := iNum - 1;
                        end
                end
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [For(Id("id"),IntLiteral(1),Id("n"),False,
                [If(BinaryOp("=",BinaryOp("mod",Id("m"),IntLiteral(2)),IntLiteral(0)),
                [CallStmt(Id("println"),[StringLiteral("m")])],[Assign(Id("iNum"),BinaryOp("-",Id("iNum"),IntLiteral(1)))])])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,368))
    
    def test_program20(self):
        input = """ 
        Procedure main();
        begin
            for i:=1 to n do
                for j:=1 to i-1 do
                    text();
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [For(Id("i"),IntLiteral(1),Id("n"),True,
                [For(Id("j"),IntLiteral(1),BinaryOp("-",Id("i"),IntLiteral(1)),True,
                [CallStmt(Id("text"),[])])])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,369))
    
    def test_program21(self):
        input = """ 
        Procedure main();
        begin
            for i:=1 to n do
                if (k1=k2) then
                    break;
                else 
                    continue;
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [For(Id("i"),IntLiteral(1),Id("n"),True,
                    [If(BinaryOp("=",Id("k1"),Id("k2")),[Break()],[Continue()])])],VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,370))
    
    def test_program22(self):
        input = """ 
        Procedure main();
        begin
            n:=100;
            S:=100;
            for i:=1 to n do
            begin
                S:=S*i;
                if(S>200) then
                    break;
            end
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('n'),IntLiteral(100)),
                Assign(Id('S'),IntLiteral(100)),
                For(Id('i'),IntLiteral(1),
                    Id('n'),True,
                    [
                    Assign(Id('S'),
                        BinaryOp('*',Id('S'),Id('i'))),
                    If(BinaryOp('>',Id('S'),IntLiteral(200)),
                        [Break()],[])
                    ])
                ],
                VoidType())]))
        self.assertTrue(TestAST.test(input,expect,371))
    
    def test_program23(self):
        input = """ 
        Procedure main();
        begin
            n:=100;
            S:=100;
            for i:=1 to n do
            begin
                S:=S+i;
                if(S>200) then
                    break;
            end
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('n'),IntLiteral(100)),
                Assign(Id('S'),IntLiteral(100)),
                For(Id('i'),IntLiteral(1),
                    Id('n'),True,
                    [
                    Assign(Id('S'),
                        BinaryOp('+',Id('S'),Id('i'))),
                    If(BinaryOp('>',Id('S'),IntLiteral(200)),
                        [Break()],[])
                    ])
                ],
                VoidType())]))
        self.assertTrue(TestAST.test(input,expect,372))
    
    def test_program24(self):
        input = """ 
        Procedure main();
        begin
            n:=100;
            S:=100;
            for i:=1 to n do
            begin
                S:=S div i;
                if(S>200) then
                    break;
            end
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('n'),IntLiteral(100)),
                Assign(Id('S'),IntLiteral(100)),
                For(Id('i'),IntLiteral(1),
                    Id('n'),True,
                    [
                    Assign(Id('S'),
                        BinaryOp('div',Id('S'),Id('i'))),
                    If(BinaryOp('>',Id('S'),IntLiteral(200)),
                        [Break()],[])
                    ])
                ],
                VoidType())]))
        self.assertTrue(TestAST.test(input,expect,373))
    
    def test_program25(self):
        input = """ 
        Procedure main();
        begin
            n:=100;
            S:=100;
            for i:=1 to n do
            begin
                S:=S div i;
                if(S>200) then
                    continue;
            end
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('n'),IntLiteral(100)),
                Assign(Id('S'),IntLiteral(100)),
                For(Id('i'),IntLiteral(1),
                    Id('n'),True,
                    [
                    Assign(Id('S'),
                        BinaryOp('div',Id('S'),Id('i'))),
                    If(BinaryOp('>',Id('S'),IntLiteral(200)),
                        [Continue()],[])
                    ])
                ],
                VoidType())]))
        self.assertTrue(TestAST.test(input,expect,374))
    
    def test_program26(self):
        input = """ 
        Procedure main();
        begin
            N:=M:=KUNG(N);
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),[],[],
                [Assign(Id("M"),CallExpr(Id("KUNG"),[Id("N")])),Assign(Id("N"),Id("M"))],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,375))
    
    def test_program27(self):
        input = """ 
        Procedure main();
        begin
            while (x<=1) do
                for x:=1 to x+1 do
                    helloworld("helloworld");
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [While(BinaryOp("<=",Id("x"),IntLiteral(1)),
                    [For(Id("x"),IntLiteral(1),BinaryOp("+",Id("x"),IntLiteral(1)),True,
                        [CallStmt(Id("helloworld"),[StringLiteral("helloworld")])])])],
                        VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,376))
    
    def test_program28(self):
        input = """ 
        Procedure main();
        begin
            while (x<=1) do
                for x:=1 to x+1 do
                    begin
                    helloworld("helloworld");
                    a();
                    end
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [While(BinaryOp("<=",Id("x"),IntLiteral(1)),
                [For(Id("x"),IntLiteral(1),BinaryOp("+",Id("x"),IntLiteral(1)),True,
                    [CallStmt(Id("helloworld"),[StringLiteral("helloworld")]),CallStmt(Id("a"),[])])])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,377))
    
    def test_program29(self):
        input = """ 
        Procedure main();
        begin
            while (x<=1) do
                for x:=1 to x+1 do
                    begin
                    helloworld("helloworld");
                    a(arr[x]);
                    end
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [While(BinaryOp("<=",Id("x"),IntLiteral(1)),
                    [For(Id("x"),IntLiteral(1),BinaryOp("+",Id("x"),IntLiteral(1)),True,
                        [CallStmt(Id("helloworld"),[StringLiteral("helloworld")]),
                            CallStmt(Id("a"),[ArrayCell(Id("arr"),Id("x"))])])])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,378))
    
    def test_program30(self):
        input = """ 
        Procedure main();
        begin
            while (x<=1) do
                for x:=1 to m[2] do
                    begin
                    helloworld("helloworld");
                    a(arr[x]);
                    end
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [While(BinaryOp("<=",Id("x"),IntLiteral(1)),
                    [For(Id("x"),IntLiteral(1),ArrayCell(Id("m"),IntLiteral(2)),True,
                        [CallStmt(Id("helloworld"),[StringLiteral("helloworld")]),CallStmt(Id("a"),[ArrayCell(Id("arr"),Id("x"))])])])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,379))
    
    def test_program30(self):
        input = """ 
        Procedure main();
        begin
            while (x<=1) do
                for x:=1 to m[2] do
                    begin
                        gu();
                    end
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("main"),
                [],
                [],
                [While(BinaryOp("<=",Id("x"),IntLiteral(1)),
                    [For(Id("x"),IntLiteral(1),ArrayCell(Id("m"),IntLiteral(2)),True,
                        [CallStmt(Id("gu"),[])])])],
                VoidType())])
        )
        self.assertTrue(TestAST.test(input,expect,380))

    

    
    

    
    
    
    


    



    

    

    

