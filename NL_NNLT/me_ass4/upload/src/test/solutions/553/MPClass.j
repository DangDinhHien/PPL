.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static b1()Z
Label0:
	ldc "call b1"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_1
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static b2()Z
Label0:
	ldc "call b2"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_1
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static b3()Z
Label0:
	ldc "call b3"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_1
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/b1()Z
	ifgt Label2
	invokestatic MPClass/b2()Z
	ifgt Label2
	iconst_0
	goto Label3
Label2:
	iconst_1
Label3:
	ifgt Label4
	invokestatic MPClass/b3()Z
	ifgt Label4
	iconst_0
	goto Label5
Label4:
	iconst_1
Label5:
	invokestatic io/putBool(Z)V
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
