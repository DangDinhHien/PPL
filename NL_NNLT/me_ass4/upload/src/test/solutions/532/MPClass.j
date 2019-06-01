.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label2 to Label3
.var 2 is y F from Label2 to Label3
Label2:
	iconst_1
	istore_1
	iload_1
	iload_1
	imul
	iconst_5
	iadd
	i2f
	fstore_2
	fload_2
	invokestatic io/putFloat(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
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
