.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 9
	putstatic MPClass.i I
Label2:
	getstatic MPClass.i I
	iconst_5
	if_icmplt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
	getstatic MPClass.i I
	iconst_3
	irem
	iconst_0
	if_icmpne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
	getstatic MPClass.i I
	iconst_3
	idiv
	i2f
	invokestatic io/putFloatLn(F)V
Label9:
Label3:
	getstatic MPClass.i I
	iconst_1
	isub
	putstatic MPClass.i I
	goto Label2
Label4:
Label1:
	return
.limit stack 2
.limit locals 1
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
