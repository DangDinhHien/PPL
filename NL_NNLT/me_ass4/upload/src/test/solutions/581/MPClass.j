.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static i I
.field static j I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	iconst_1
	ifle Label3
	ldc "LOOPING..."
	invokestatic io/putStringLn(Ljava/lang/String;)V
	goto Label3
	goto Label2
Label3:
	iconst_1
	putstatic MPClass.i I
Label4:
	getstatic MPClass.i I
	bipush 100
	if_icmpgt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
Label9:
	iconst_0
	ifgt Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifgt Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label10
	goto Label10
	goto Label9
Label10:
	bipush 9
	ineg
	putstatic MPClass.j I
Label17:
	getstatic MPClass.j I
	iconst_1
	ineg
	if_icmpgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label19
	getstatic MPClass.j I
	getstatic MPClass.i I
	imul
	ineg
	invokestatic io/putInt(I)V
Label18:
	getstatic MPClass.j I
	iconst_1
	iadd
	putstatic MPClass.j I
	goto Label17
Label19:
	goto Label6
Label5:
	getstatic MPClass.i I
	iconst_1
	iadd
	putstatic MPClass.i I
	goto Label4
Label6:
Label1:
	return
.limit stack 7
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
