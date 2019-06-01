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
	iconst_3
	istore_1
Label2:
	iload_1
	iconst_1
	if_icmplt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
	iload_1
	iconst_1
	if_icmpne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
	goto Label4
Label9:
Label3:
	iload_1
	iconst_1
	isub
	istore_1
	goto Label2
Label4:
	iload_1
	invokestatic io/writeInt(I)V
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
