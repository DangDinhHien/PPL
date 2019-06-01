.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x I

.method public static foo()Z
Label0:
	ldc "in foo"
	invokestatic io/putString(Ljava/lang/String;)V
	iconst_0
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	putstatic MPClass.x I
	getstatic MPClass.x I
	bipush 100
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	invokestatic MPClass/foo()Z
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	ldc "in then"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	goto Label7
Label6:
	ldc "in else"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label7:
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
