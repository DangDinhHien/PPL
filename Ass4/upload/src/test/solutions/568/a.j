.source a.java
.class public a
.super java.lang.Object
.field static d F
.field static bb F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is d F from Label0 to Label1
.var 2 is e Z from Label0 to Label1
Label0:
	ldc 4.5
	fstore_1
	fload_1
	iconst_1
	i2f
	fcmpl
	ifge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	fload_1
	ldc 3.3
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	istore_2
	iload_2
	invokestatic io/writeBool(Z)V
Label1:
	return
.limit stack 3
.limit locals 3
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
