.source a.java
.class public a
.super java.lang.Object

.method public static foo2()V
Label0:
	iconst_1
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	invokestatic io/writeInt(I)V
	invokestatic b/foo2()V
Label1:
	return
.limit stack 1
.limit locals 1
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
