.source a.java
.class public a
.super java.lang.Object
.field static d F
.field static bb F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is e Z from Label0 to Label1
Label0:
	iconst_0
	istore_2
	bipush 10
	istore_1
.var 3 is a F from Label2 to Label3
Label2:
	ldc 4.0
	fstore_3
	fload_3
	invokestatic io/writeFloat(F)V
Label3:
	iload_1
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public <init>()V
.var 0 is this La; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
