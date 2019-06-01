.source a.java
.class public a
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is dem I from Label0 to Label1
Label0:
	invokestatic b/foo2()Z
	istore_1
	invokestatic b/foo2()Z
	invokestatic io/writeBool(Z)V
Label1:
	return
.limit stack 1
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
