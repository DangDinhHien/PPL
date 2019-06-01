.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static giaithua(I)I
.var 0 is n I from Label0 to Label1
.var 1 is GT I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_1
	istore_2
Label2:
	iload_2
	iload_0
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
	iload_1
	iload_2
	imul
	istore_1
Label3:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label4:
	iload_1
	ireturn
Label1:
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
.var 2 is y F from Label0 to Label1
.var 3 is n I from Label0 to Label1
Label0:
	iconst_5
	istore_3
	iload_3
	invokestatic MPClass/giaithua(I)I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
.limit locals 4
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
