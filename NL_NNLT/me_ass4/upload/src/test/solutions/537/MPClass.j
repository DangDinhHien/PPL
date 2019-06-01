.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/T()Z
	invokestatic io/putBoolLn(Z)V
	invokestatic MPClass/F()Z
	invokestatic io/putBoolLn(Z)V
	invokestatic MPClass/T()Z
	ifle Label2
	invokestatic MPClass/FOO()Z
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBoolLn(Z)V
	invokestatic MPClass/F()Z
	ifle Label4
	invokestatic MPClass/FOO()Z
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static T()Z
Label0:
	iconst_1
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static F()Z
Label0:
	iconst_0
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static FOO()Z
Label0:
	ldc "FOO!"
	invokestatic io/putString(Ljava/lang/String;)V
	iconst_0
	ireturn
Label1:
.limit stack 2
.limit locals 0
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
