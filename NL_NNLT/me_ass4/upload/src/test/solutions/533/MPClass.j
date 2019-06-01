.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x I

.method public static f()F
Label0:
	ldc 2.0
	freturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is y I from Label2 to Label3
.var 2 is z F from Label2 to Label3
.var 3 is x F from Label2 to Label3
Label2:
	iconst_5
	istore_1
Label4:
	iload_1
	iconst_0
	if_icmplt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
	iload_1
	invokestatic io/putInt(I)V
Label5:
	iload_1
	iconst_1
	isub
	istore_1
	goto Label4
Label6:
Label3:
Label1:
	return
.limit stack 2
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
