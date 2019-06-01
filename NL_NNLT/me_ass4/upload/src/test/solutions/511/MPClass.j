.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is s I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
Label0:
	iconst_1
	istore_2
Label2:
	iload_2
	bipush 10
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_2
	iconst_4
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iload_2
	bipush 7
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iand
	ifle Label10
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label10:
	iconst_0
	istore_1
	iload_2
	bipush 10
	imul
	istore_3
Label11:
	iload_3
	iload_2
	iconst_1
	iadd
	bipush 10
	imul
	if_icmpgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label13
	iload_3
	iconst_2
	irem
	iconst_0
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	goto Label12
Label18:
	iload_1
	iload_3
	iadd
	istore_1
Label12:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label11
Label13:
	iload_2
	invokestatic io/putInt(I)V
	ldc ", "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	invokestatic io/putInt(I)V
	invokestatic io/putLn()V
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label1:
	return
.limit stack 3
.limit locals 4
.end method

.method public static fact(I)I
.var 0 is x I from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is f I from Label0 to Label1
Label0:
	iconst_1
	istore_2
	iconst_1
	istore_1
Label2:
	iload_1
	iload_0
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
	iload_2
	iload_1
	imul
	istore_2
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
	iload_2
	ireturn
Label1:
.limit stack 2
.limit locals 3
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
