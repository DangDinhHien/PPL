.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	bipush 10
	bipush 10
	idiv
	istore_1
Label2:
	iload_1
	bipush 9
	bipush 19
	imul
	bipush 10
	idiv
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
Label7:
	iconst_5
	iload_1
	if_icmple Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
	iload_1
	invokestatic io/putInt(I)V
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label7
Label8:
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
	ldc ""
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
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
