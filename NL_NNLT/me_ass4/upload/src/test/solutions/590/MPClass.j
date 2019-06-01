.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static i I

.method public static foo()V
Label0:
	iconst_0
	putstatic MPClass.i I
	getstatic MPClass.i I
	invokestatic io/putInt(I)V
.var 0 is i I from Label2 to Label3
Label2:
.var 1 is f F from Label4 to Label5
.var 2 is i F from Label4 to Label5
Label4:
.var 3 is i Z from Label6 to Label7
Label6:
	iconst_1
	iconst_5
	ineg
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	istore_3
	iload_3
	invokestatic io/putBool(Z)V
Label7:
Label5:
Label3:
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_1
	ineg
	istore_1
	iload_1
	invokestatic io/putInt(I)V
	invokestatic MPClass/foo()V
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 2
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
