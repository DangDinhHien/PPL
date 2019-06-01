.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is c Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "UNNNDJ"
	putstatic MPClass.a Ljava/lang/String;
	getstatic MPClass.a Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
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
