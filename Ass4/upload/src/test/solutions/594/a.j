.source a.java
.class public a
.super java.lang.Object
.field static d F
.field static bb F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is d I from Label0 to Label1
.var 2 is f I from Label0 to Label1
.var 3 is e Z from Label0 to Label1
Label0:
	iconst_1
	iconst_3
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_3
	iconst_1
	istore_1
Label4:
	iload_1
	iconst_3
	iconst_2
	isub
	if_icmpgt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
	iload_3
	invokestatic io/writeBool(Z)V
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label6:
Label1:
	return
.limit stack 3
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
