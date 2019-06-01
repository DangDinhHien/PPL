.source a.java
.class public a
.super java.lang.Object
.field static d F
.field static bb F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
.var 2 is e Z from Label0 to Label1
Label0:
	iconst_0
	istore_2
.var 3 is a I from Label2 to Label3
.var 4 is b I from Label2 to Label3
Label2:
	iconst_0
	istore_3
.var 5 is b F from Label4 to Label5
Label4:
	iload_3
	invokestatic io/writeInt(I)V
Label5:
Label3:
Label1:
	return
.limit stack 2
.limit locals 6
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
