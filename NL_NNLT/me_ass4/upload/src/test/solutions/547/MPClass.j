.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	bipush 10
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_0
	istore_2
Label6:
	iload_2
	bipush 10
	if_icmpgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
	iload_2
	iconst_2
	irem
	iconst_0
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
	goto Label7
Label13:
	iload_1
	iload_2
	invokestatic MPClass/foo(II)I
	invokestatic io/putIntLn(I)V
Label7:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label8:
	iload_1
	iconst_2
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	goto Label3
Label16:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static foo(II)I
.var 0 is i I from Label0 to Label1
.var 1 is j I from Label0 to Label1
Label0:
	iload_0
	bipush 10
	imul
	iload_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
