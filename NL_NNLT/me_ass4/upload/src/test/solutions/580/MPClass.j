.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MPClass.i I
Label2:
	getstatic MPClass.i I
	bipush 10
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
	getstatic MPClass.i I
	iconst_5
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
	goto Label4
Label9:
Label3:
	getstatic MPClass.i I
	iconst_1
	iadd
	putstatic MPClass.i I
	goto Label2
Label4:
	getstatic MPClass.i I
	invokestatic io/putIntLn(I)V
	iconst_0
	putstatic MPClass.i I
Label10:
	getstatic MPClass.i I
	bipush 100
	if_icmpgt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label12
	getstatic MPClass.i I
	bipush 10
	if_icmplt Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label17
	goto Label11
	goto Label18
Label17:
	getstatic MPClass.i I
	invokestatic io/putInt(I)V
Label18:
Label11:
	getstatic MPClass.i I
	iconst_1
	iadd
	putstatic MPClass.i I
	goto Label10
Label12:
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
