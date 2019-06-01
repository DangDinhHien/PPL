.source a.java
.class public a
.super java.lang.Object
.field static d F
.field static bb F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is d F from Label0 to Label1
Label0:
	iconst_5
	i2f
	ldc 3.0
	fadd
	fstore_1
	fload_1
	iconst_1
	i2f
	fadd
	fstore_1
	fload_1
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 2
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
