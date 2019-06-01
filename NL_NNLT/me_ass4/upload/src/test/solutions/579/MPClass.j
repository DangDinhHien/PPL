.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 100
	ineg
	putstatic MPClass.i I
Label2:
	getstatic MPClass.i I
	bipush 100
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
	iconst_0
	putstatic MPClass.i I
Label7:
	getstatic MPClass.i I
	bipush 100
	if_icmpgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
Label8:
	getstatic MPClass.i I
	iconst_1
	iadd
	putstatic MPClass.i I
	goto Label7
Label9:
Label3:
	getstatic MPClass.i I
	iconst_1
	iadd
	putstatic MPClass.i I
	goto Label2
Label4:
	getstatic MPClass.i I
	invokestatic io/putInt(I)V
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
