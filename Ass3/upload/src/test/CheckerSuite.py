import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_Redeclared_1(self):
        input = """
            class io {

            }

            """

        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input, expect, 301))

    def test_Redeclared_2(self):
        input = """
            class a {
            
            }

            class a{

            }

            """

        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 302))

    def test_Redeclared_3(self):
        input = """
            class b {

            }

            class a {
            
            }

            class b{

            }

            """

        expect = "Redeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 303))

    def test_Redeclared_4(self):
        input = """
            class a {
                a: int;
                static a: float;
            }

            """

        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 304))

    def test_Redeclared_5(self):
        input = """
            class a {
                a: int;
                static b: float;
                final int b = 1;
            }

            """

        expect = "Redeclared Constant: b"
        self.assertTrue(TestChecker.test(input, expect, 305))

    def test_Redeclared_6(self):
        input = """
            class a {
                a: int;
                static b: float;
                final int c = 1;

                void c(){

                }
            }

            """

        expect = "Redeclared Method: c"
        self.assertTrue(TestChecker.test(input, expect, 306))

    def test_Redeclared_7(self):
        input = """
            class a {
                a: int;
                static b: float;
                final int c = 1;

                void tinh(d,d:int){
                
                }
            }

            """

        expect = "Redeclared Parameter: d"
        self.assertTrue(TestChecker.test(input, expect, 307))

    def test_Redeclared_8(self):
        input = """
            class a {
                a: int;
                static b: float;
                final int c = 1;

                void tinh(d,e:int; f:string; e:boolean){
                
                }
            }

            """

        expect = "Redeclared Parameter: e"
        self.assertTrue(TestChecker.test(input, expect, 308))

    def test_Redeclared_9(self):
        input = """
            class a {
                a: int;
                static b: float;
                final int c = 1;

                void main(d,e:int; f:string){
                    e: float;
                
                }
            }

            """

        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input, expect, 309))

    def test_Redeclared_10(self):
        input = """
            class a {
                a: int;
                static b: float;
                final int c = 1;

                void mainc(){
                    static e: float;
                    final string f = "Str";
                }

                int mainc(){

                }
            }

            """

        expect = "Redeclared Method: mainc"
        self.assertTrue(TestChecker.test(input, expect, 310))

    def test_Redeclared_11(self):
        input = """
            class a {
                a: int;
                static b: float;
                final int c = 1;

                void mainc(){
                    static e: float;
                    final string f = "Str";
                    mainc: float;
                    e : int;
                }
            }

            """

        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input, expect, 311))

    def test_Undeclared_12(self):
        input = """
            class a extends b {
                a: int;
                static b: float;
                final int c = 1;

                void main(){

                }
            }

            """

        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 312))

    def test_Undeclared_13(self):
        input = """
            class a extends b {
                a: int;
                static b: float;
                final int c = 1;

                void main(){
                    aa := 1;

                }
            }

            class b{

            }

            """

        expect = "Undeclared Identifier: aa"
        self.assertTrue(TestChecker.test(input, expect, 313))

    def test_Undeclared_14(self):
        input = """
            class a extends b {
                a: int;
                static b: float;
                final int c = 1;

                void main(){
                    aaa := 1;

                }
            }

            class b{
                aaa : int;

            }

            """

        expect = "Undeclared Identifier: aaa"
        self.assertTrue(TestChecker.test(input, expect, 314))

    def test_Undeclared_15(self):
        input = """
            class a extends b {
                a: int;
                static b: float;
                final int c = 1;

                void main(){
                    this.aaa := 1;

                }
            }

            class b{
                aaa : int;

            }

            """

        expect = "Undeclared Attribute: aaa"
        self.assertTrue(TestChecker.test(input, expect, 315))

    def test_Undeclared_16(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(){
                    a := b.dem;

                }
            }

            class b{
                dem : int;

            }

            """

        expect = "Undeclared Attribute: dem"
        self.assertTrue(TestChecker.test(input, expect, 316))

    def test_Undeclared_17(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int foo(){

                }

                void main(){
                    a := b.dem;

                    a := this.foo0();

                }
            }

            class b{
                static dem : int;

            }

            """

        expect = "Undeclared Method: foo0"
        self.assertTrue(TestChecker.test(input, expect, 317))

    def test_Undeclared_18(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int foo(){

                }

                void main(){
                    a := b.dem;

                    a := cc.foo();

                }
            }

            class b{
                static dem : int;

            }

            """

        expect = "Undeclared Class: cc"
        self.assertTrue(TestChecker.test(input, expect, 318))

    def test_Undeclared_19(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int foo(){

                }

                void main(){
                    a := b.dem;

                    a := b.foo();

                }
            }

            class b{
                static dem : int;

            }

            """

        expect = "Undeclared Method: foo"
        self.assertTrue(TestChecker.test(input, expect, 319))

    def test_Undeclared_20(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int foo(){

                }

                void main(){
                    if (temp > 1) then {

                    }
                }
            }

            class b{
                static dem : int;

            }

            """

        expect = "Undeclared Identifier: temp"
        self.assertTrue(TestChecker.test(input, expect, 320))

    def test_Undeclared_21(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int foo(){

                }

                void main(){
                    for temp := 1 to 10 do{

                    }
                }
            }

            class b{
                static dem : int;

            }

            """

        expect = "Undeclared Identifier: temp"
        self.assertTrue(TestChecker.test(input, expect, 321))

    def test_CanNotAssignToConstant_22(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int foo(){

                }

                void main(){
                    this.dem := 10;
                }
            }

            class b{
                static final int dem = 1;

            }

            """

        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(SelfLiteral(),Id(dem)),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input, expect, 322))

    def test_CanNotAssignToConstant_23(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int foo(){

                }

                void main(){
                    c := 10;
                }
            }

            class b{
                static final int dem = 1;

            }

            """

        expect = "Cannot Assign To Constant: AssignStmt(Id(c),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input, expect, 323))

    def test_CanNotAssignToConstant_24(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int foo(){
                    static final string foc = "S";

                }

                void main(){
                    final float b = 1.1;
                    {
                        b := 1;
                    }
                }
            }

            class b{
                static final int dem = 1;

            }

            """

        expect = "Cannot Assign To Constant: AssignStmt(Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 324))

    def test_TypeMismatchInStatement_25(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final int c = 1;

                void main(){
                    if (c) then {

                    }
                }
            }

            """

        expect = "Type Mismatch In Statement: If(Id(c),Block(List(),List()))"
        self.assertTrue(TestChecker.test(input, expect, 325))

    def test_TypeMismatchInStatement_26(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final int c = 1;

                void main(){
                    if (c + a) then {

                    }
                }
            }

            """

        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(c),Id(a)),Block(List(),List()))"
        self.assertTrue(TestChecker.test(input, expect, 326))

    def test_TypeMismatchInStatement_27(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    for i := 1 to j do {

                    }
                }
            }

            """

        expect = "Type Mismatch In Statement: For(Id(i),IntLiteral(1),Id(j),True,Block(List(),List())])"
        self.assertTrue(TestChecker.test(input, expect, 327))

    def test_TypeMismatchInStatement_28(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:float;j:float;k:string){
                    for i := 1 to 10 do {
                    
                    }
                }
            }

            """

        expect = "Type Mismatch In Statement: For(Id(i),IntLiteral(1),IntLiteral(10),True,Block(List(),List())])"
        self.assertTrue(TestChecker.test(input, expect, 328))

    def test_TypeMismatchInStatement_29(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:string;j:float;k:string){
                    for i := 1 to 10 do {
                    
                    }
                }
            }

            """

        expect = "Type Mismatch In Statement: For(Id(i),IntLiteral(1),IntLiteral(10),True,Block(List(),List())])"
        self.assertTrue(TestChecker.test(input, expect, 329))

    def test_TypeMismatchInStatement_30(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    for i := 1.1 to 10 do {
                    
                    }
                }
            }

            """

        expect = "Type Mismatch In Statement: For(Id(i),FloatLiteral(1.1),IntLiteral(10),True,Block(List(),List())])"
        self.assertTrue(TestChecker.test(input, expect, 330))

    def test_TypeMismatchInStatement_31(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    for i := this.len to 10 do {
                    
                    }
                }
            }

            class b {
                static len: float;

            }

            """

        expect = "Type Mismatch In Statement: For(Id(i),FieldAccess(SelfLiteral(),Id(len)),IntLiteral(10),True,Block(List(),List())])"
        self.assertTrue(TestChecker.test(input, expect, 331))

    def test_TypeMismatchInStatement_32(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    for i := this.len to b.n do {
                    
                    }
                }
            }

            class b {
                static len: int;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Statement: For(Id(i),FieldAccess(SelfLiteral(),Id(len)),FieldAccess(Id(b),Id(n)),True,Block(List(),List())])"
        self.assertTrue(TestChecker.test(input, expect, 332))

    def test_TypeMismatchInStatement_33(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    for i := this.len to (1 > 0) do {
                    
                    }
                }
            }

            class b {
                static len: int;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Statement: For(Id(i),FieldAccess(SelfLiteral(),Id(len)),BinaryOp(>,IntLiteral(1),IntLiteral(0)),True,Block(List(),List())])"
        self.assertTrue(TestChecker.test(input, expect, 333))

    def test_TypeMismatchInStatement_34(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    for c := this.len to 10 do {
                    
                    }
                }
            }

            class b {
                static len: int;

                static final string n = "t";

            }

            """

        expect = "Cannot Assign To Constant: For(Id(c),FieldAccess(SelfLiteral(),Id(len)),IntLiteral(10),True,Block(List(),List())])"
        self.assertTrue(TestChecker.test(input, expect, 334))

    def test_TypeMismatchInStatement_35(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    i := 1.1;
                }
            }

            class b {
                static len: int;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(i),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 335))

    def test_TypeMismatchInStatement_36(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    i := "Anh sai roi";
                }
            }

            class b {
                static len: int;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(i),StringLiteral(\"Anh sai roi\"))"
        self.assertTrue(TestChecker.test(input, expect, 336))

    def test_TypeMismatchInStatement_37(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    i := this.len;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(i),FieldAccess(SelfLiteral(),Id(len)))"
        self.assertTrue(TestChecker.test(input, expect, 337))

    def test_TypeMismatchInStatement_38(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    i := this.foo();
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){


                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(i),CallExpr(SelfLiteral(),Id(foo),List()))"
        self.assertTrue(TestChecker.test(input, expect, 338))

    def test_TypeMismatchInStatement_39(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    a :int[5];
                    a[1] := 1.1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),IntLiteral(1)),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 339))


    def test_TypeMismatchInStatement_40(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    a :boolean[5];
                    a[1] := b.foo();
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),IntLiteral(1)),CallExpr(Id(b),Id(foo),List()))"
        self.assertTrue(TestChecker.test(input, expect, 340))

    def test_TypeMismatchInStatement_41(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    a :boolean[5];
                    a[1] := (1 > 1);
                    a[2] := this.foo();
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),IntLiteral(2)),CallExpr(SelfLiteral(),Id(foo),List()))"
        self.assertTrue(TestChecker.test(input, expect, 341))

    def test_TypeMismatchInStatement_42(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    io.readInt();
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: CallStmt(Id(io),Id(readInt),[])"
        self.assertTrue(TestChecker.test(input, expect, 342))

    def test_TypeMismatchInStatement_43(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    io.readStr();
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: CallStmt(Id(io),Id(readStr),[])"
        self.assertTrue(TestChecker.test(input, expect, 343))


    def test_TypeMismatchInStatement_44(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    c.readStr();
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: CallStmt(Id(c),Id(readStr),[])"
        self.assertTrue(TestChecker.test(input, expect, 344))

    def test_TypeMismatchInStatement_45(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    cc.readStr();
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Undeclared Class: cc"
        self.assertTrue(TestChecker.test(input, expect, 345))

    def test_TypeMismatchInStatement_46(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    this.main(1,1);
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: CallStmt(SelfLiteral(),Id(main),[IntLiteral(1),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input, expect, 346))

    def test_TypeMismatchInStatement_47(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    this.main(1,1, "2");
                    this.main();
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: CallStmt(SelfLiteral(),Id(main),[])"
        self.assertTrue(TestChecker.test(input, expect, 347))

    def test_TypeMismatchInStatement_48(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    this.main(1,1, "2");
                    this.main(1.1, 1, "s");
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: CallStmt(SelfLiteral(),Id(main),[FloatLiteral(1.1),IntLiteral(1),StringLiteral(\"s\")])"
        self.assertTrue(TestChecker.test(input, expect, 348))

    def test_TypeMismatchInStatement_49(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    this.main(1,1, this.foo());
                    this.main(1.1, 1, (i < 1));
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: CallStmt(SelfLiteral(),Id(main),[FloatLiteral(1.1),IntLiteral(1),BinaryOp(<,Id(i),IntLiteral(1))])"
        self.assertTrue(TestChecker.test(input, expect, 349))

    def test_TypeMismatchInStatement_50(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                void main(i:int;j:float;k:string){
                    return 0;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input, expect, 350))

    def test_TypeMismatchInStatement_51(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int main(i:int;j:float;k:string){
                    return 1.1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 351))

    def test_TypeMismatchInStatement_52(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int main(i:int;j:float;k:string){
                    return "Sai";
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: Return(StringLiteral(\"Sai\"))"
        self.assertTrue(TestChecker.test(input, expect, 352))

    def test_TypeMismatchInStatement_53(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int main(i:int;j:float;k:string){
                    return this.foo();
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return n;
                }

            }

            """

        expect = "Type Mismatch In Statement: Return(CallExpr(SelfLiteral(),Id(foo),List()))"
        self.assertTrue(TestChecker.test(input, expect, 353))

    def test_TypeMismatchInStatement_54(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int main(i:int;j:float;k:string){
                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return 1 > 0;
                }

            }

            """

        expect = "Type Mismatch In Statement: Return(BinaryOp(>,IntLiteral(1),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input, expect, 354))


    def test_TypeMismatchInStatement_55(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int main(i:int;j:float;k:string){
                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

                string foo(){
                

                    return 1 <= 0;
                }

            }

            """

        expect = "Type Mismatch In Statement: Return(BinaryOp(<=,IntLiteral(1),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input, expect, 354))

    def test_TypeMismatchInExpression_56(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int main(i:int;j:float;k:string){
                    a[1] := 1;

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 356))

    def test_TypeMismatchInExpression_57(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int main(i:int;j:float;k:string){
                    at[1] := 1;

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Undeclared Identifier: at"
        self.assertTrue(TestChecker.test(input, expect, 357))

    def test_TypeMismatchInExpression_58(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int main(i:int;j:float;k:string){
                    at: float[10];
                    at[j] := 1;

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: ArrayCell(Id(at),Id(j))"
        self.assertTrue(TestChecker.test(input, expect, 358))

    def test_TypeMismatchInExpression_59(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                int main(i:int;j:float;k:string){
                    at: float[10];
                    at[1.3] := 1;

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: ArrayCell(Id(at),FloatLiteral(1.3))"
        self.assertTrue(TestChecker.test(input, expect, 359))

    def test_TypeMismatchInExpression_60(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string){
                    at: float[10];
                    at[this.main()] := 1;

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: CallExpr(SelfLiteral(),Id(main),List())"
        self.assertTrue(TestChecker.test(input, expect, 360))

    def test_TypeMismatchInExpression_61(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string){
                    at: float[10];
                    at[(1+1.1)] := 1;

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: ArrayCell(Id(at),BinaryOp(+,IntLiteral(1),FloatLiteral(1.1)))"
        self.assertTrue(TestChecker.test(input, expect, 361))

    def test_TypeMismatchInExpression_62(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string){
                    i := i + k;

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: BinaryOp(+,Id(i),Id(k))"
        self.assertTrue(TestChecker.test(input, expect, 362))

    def test_TypeMismatchInExpression_63(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string){
                    i := "1" + 1;

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(\"1\"),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 363))

    def test_TypeMismatchInExpression_64(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float){
                    i := this.main(1,1) - (1>1);

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: BinaryOp(-,CallExpr(SelfLiteral(),Id(main),List(IntLiteral(1),IntLiteral(1))),BinaryOp(>,IntLiteral(1),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 364))

    def test_TypeMismatchInExpression_65(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float){
                    i := this.a * "t";

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: BinaryOp(*,FieldAccess(SelfLiteral(),Id(a)),StringLiteral(\"t\"))"
        self.assertTrue(TestChecker.test(input, expect, 365))

    def test_TypeMismatchInExpression_66(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float){
                    i := this.a % 4;
                    j := this.a % 2.5;

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: BinaryOp(%,FieldAccess(SelfLiteral(),Id(a)),FloatLiteral(2.5))"
        self.assertTrue(TestChecker.test(input, expect, 366))

    def test_TypeMismatchInExpression_67(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    i := this.a % 4;
                    j := this.a % 2;
                    k := "111" ^ "222";
                    k := "111" ^ 1;
                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: BinaryOp(^,StringLiteral(\"111\"),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 367))

    def test_TypeMismatchInExpression_68(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    i := this.a % 4;
                    j := this.a % 2;
                    k := "111" ^ "222";
                    k := "111" ^ 1.4;
                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: BinaryOp(^,StringLiteral(\"111\"),FloatLiteral(1.4))"
        self.assertTrue(TestChecker.test(input, expect, 368))

    def test_TypeMismatchInExpression_69(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    l := (1>1);
                    l := (5 <= k);
                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: BinaryOp(<=,IntLiteral(5),Id(k))"
        self.assertTrue(TestChecker.test(input, expect, 369))

    def test_TypeMismatchInExpression_70(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    l := (1>1);
                    l := (5 == k);
                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: BinaryOp(==,IntLiteral(5),Id(k))"
        self.assertTrue(TestChecker.test(input, expect, 370))

    def test_TypeMismatchInExpression_71(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    if (l == 1) then {

                    }


                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: BinaryOp(==,Id(l),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 371))

    def test_TypeMismatchInExpression_72(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    l := -"1";

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: UnaryOp(-,StringLiteral(\"1\"))"
        self.assertTrue(TestChecker.test(input, expect, 372))

    def test_TypeMismatchInExpression_73(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    l := +"str";

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: UnaryOp(+,StringLiteral(\"str\"))"
        self.assertTrue(TestChecker.test(input, expect, 373))

    def test_TypeMismatchInExpression_74(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    i := -10;

                    l := !l;
                    l := !i;

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: UnaryOp(!,Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 374))

    def test_TypeMismatchInExpression_75(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    i := -10;

                    l := !l;
                    l := !k;

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: UnaryOp(!,Id(k))"
        self.assertTrue(TestChecker.test(input, expect, 375))

    def test_TypeMismatchInExpression_76(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    i := -10;

                    l := (1<1) && true;

                    l := true && "s" || false;
                    

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: BinaryOp(&&,BooleanLiteral(True),StringLiteral(\"s\"))"
        self.assertTrue(TestChecker.test(input, expect, 376))

    def test_TypeMismatchInExpression_77(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    i := -10;

                    l := (1<1) && true;

                    l := true || false;

                    l := !1;
                    

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: UnaryOp(!,IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 377))

    def test_TypeMismatchInExpression_78(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    t : b;

                    t := new b(1);

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: NewExpr(Id(b),List(IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 378))

    def test_TypeMismatchInExpression_79(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    t : b;

                    i := new b();

                    return 1;
                }
            }

            class b {
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(i),NewExpr(Id(b),List()))"
        self.assertTrue(TestChecker.test(input, expect, 379))

    def test_TypeMismatchInExpression_80(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    t : b;

                    t := new b(1,1);
                    t := new b(1,1.1);
                    return 1;
                }
            }

            class b {
                b(a,b:int){

                }
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: NewExpr(Id(b),List(IntLiteral(1),FloatLiteral(1.1)))"
        self.assertTrue(TestChecker.test(input, expect, 380))

    def test_TypeMismatchInExpression_81(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    t : b;

                    t := new b(1,1);
                    t := new b(1,1.1,9);
                    return 1;
                }
            }

            class b {
                b(a,b:int){

                }
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: NewExpr(Id(b),List(IntLiteral(1),FloatLiteral(1.1),IntLiteral(9)))"
        self.assertTrue(TestChecker.test(input, expect, 381))

    def test_TypeMismatchInExpression_82(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    t : b;

                    t := new b(1,1);
                    t := new b(1,tem);
                    return 1;
                }
            }

            class b {
                b(a,b:int){

                }
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Undeclared Identifier: tem"
        self.assertTrue(TestChecker.test(input, expect, 382))

    def test_TypeMismatchInExpression_83(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    t : b;

                    t := new b(1,1);
                    t := new b(1,"cc");
                    return 1;
                }
            }

            class b {
                b(a,b:int){

                }
                static len: float;

                static final string n = "t";

            }

            """

        expect = "Type Mismatch In Expression: NewExpr(Id(b),List(IntLiteral(1),StringLiteral(\"cc\")))"
        self.assertTrue(TestChecker.test(input, expect, 383))

    def test_TypeMismatchInExpression_84(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    t : b;

                    return 1;
                }
            }

            class b extends c{

            }

            """

        expect = "Undeclared Class: c"
        self.assertTrue(TestChecker.test(input, expect, 384))

    def test_TypeMismatchInExpression_85(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    i := this.foo();
                    l := this.foo();
                    return 1;
                }
            }

            class b extends c{

            }

            class c{
                int foo(){
                    return 1;
                }
            }


            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(l),CallExpr(SelfLiteral(),Id(foo),List()))"
        self.assertTrue(TestChecker.test(input, expect, 385))

    def test_TypeMismatchInExpression_86(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    this.foo();
                    return 1;
                }
            }

            class b extends c{

            }

            class c{
                int foo(){
                    return 1;
                }
            }


            """

        expect = "Type Mismatch In Statement: CallStmt(SelfLiteral(),Id(foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 386))

    def test_TypeMismatchInExpression_87(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    i := this.foo(1);
                    i := this.foo();
                    return 1;
                }
            }

            class b extends c{

            }

            class c{
                int foo(a:int){
                    return 1;
                }
            }


            """

        expect = "Type Mismatch In Expression: CallExpr(SelfLiteral(),Id(foo),List())"
        self.assertTrue(TestChecker.test(input, expect, 387))

    def test_TypeMismatchInExpression_88(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    i := this.a;
                    i := this.aa;
                    return 1;
                }
            }

            class b extends c{

            }

            class c{
                int foo(a:int){
                    return 1;
                }
            }


            """

        expect = "Undeclared Attribute: aa"
        self.assertTrue(TestChecker.test(input, expect, 388))

    def test_TypeMismatchInExpression_89(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    i := c.a;
                    k := c.a;
                    return 1;
                }
            }

            class b extends c{

            }

            class c{
                static final int a = 1;
                int foo(a:int){
                    return 1;
                }
            }


            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(k),FieldAccess(Id(c),Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 389))

    def test_TypeMismatchInExpression_90(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    i := c.a;
                    l := c.a;
                    return 1;
                }
            }

            class b extends c{

            }

            class c{
                static final int a = 1;
                int foo(a:int){
                    return 1;
                }
            }


            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(l),FieldAccess(Id(c),Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 390))

    def test_TypeMismatchInExpression_91(self):
        input = """
            class a extends b {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    i := c.a;
                    j := this.aa;
                    return 1;
                }
            }

            class b extends c{
                static aa: string;

            }

            class c{
                static final int a = 1;
                int foo(a:int){
                    return 1;
                }
            }


            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(j),FieldAccess(SelfLiteral(),Id(aa)))"
        self.assertTrue(TestChecker.test(input, expect, 391))

    def test_TypeMismatchInConstant_92(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    final int c = 1.1;
                    return 1;
                }
            }


            """

        expect = "Type Mismatch In Constant Declaration: AttributeDecl(Instance,ConstDecl(Id(c),IntType,FloatLiteral(1.1)))"
        self.assertTrue(TestChecker.test(input, expect, 392))

    def test_TypeMismatchInConstant_93(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final int c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    final int c = l;
                    return 1;
                }
            }


            """

        expect = "Type Mismatch In Constant Declaration: AttributeDecl(Instance,ConstDecl(Id(c),IntType,Id(l)))"
        self.assertTrue(TestChecker.test(input, expect, 393))

    def test_TypeMismatchInConstant_94(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final float c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    final int c = 1 + c;
                    return 1;
                }
            }


            """

        expect = "Type Mismatch In Constant Declaration: AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(+,IntLiteral(1),Id(c))))"
        self.assertTrue(TestChecker.test(input, expect, 394))


    def test_TypeMismatchInConstant_95(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final float c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    final int c = 1 + "cc";
                    return 1;
                }
            }


            """

        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),StringLiteral(\"cc\"))"
        self.assertTrue(TestChecker.test(input, expect, 395))

    def test_TypeMismatchInConstant_96(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final float c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    final int c = 1 + true;
                    return 1;
                }
            }


            """

        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input, expect, 396))

    def test_Breaknotinloop_97(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final float c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    break;
                    return 1;
                }
            }


            """

        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 397))

    def test_Breaknotinloop_98(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final float c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    for i := 1 to 10 do {
                        break;
                    }

                    {
                        if 1>1 then {
                            {
                                break;
                            }
                        }
                    }
                    return 1;
                }
            }


            """

        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 398))

    def test_Continuenotinloop_99(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final float c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    for i := 1 to 10 do {
                        break;
                    }

                    {
                        if 1>1 then {
                            {
                                continue;
                            }
                        }
                    }
                    return 1;
                }
            }


            """

        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 399))

    def test_Continuenotinloop_100(self):
        input = """
            class a {
                a: int;
                static bb: float;
                final float c = 1;

                float main(i:int;j:float;k:string;l:boolean){
                    continue;
                    return 1;
                }
            }


            """

        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 400))