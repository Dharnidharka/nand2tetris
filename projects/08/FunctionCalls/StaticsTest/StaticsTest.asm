@256
D=A
@SP
M=D
@Sys.init$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init$ret.0)

//

//function Class1.set 0
(Class1.set)
@0
D=A
(Class1.set.localInit )
@Class1.set.localEnd
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
D=D-1
@Class1.set.localInit
0;JMP
(Class1.set.localEnd )

//push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//pop static 0
@SP
AM=M-1
D=M
@Class1.vm0
M=D

//push argument 1
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//pop static 1
@SP
AM=M-1
D=M
@Class1.vm1
M=D

//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

//return
@LCL
D=M
@FRAME
M=D
@5
D=D-A
A=D
D=M
@RET
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@FRAME
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@FRAME
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@FRAME
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@FRAME
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@RET
A=M
0;JMP

//

//function Class1.get 0
(Class1.get)
@0
D=A
(Class1.get.localInit )
@Class1.get.localEnd
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
D=D-1
@Class1.get.localInit
0;JMP
(Class1.get.localEnd )

//push static 0
@Class1.vm0
D=M
@SP
A=M
M=D
@SP
M=M+1

//push static 1
@Class1.vm1
D=M
@SP
A=M
M=D
@SP
M=M+1

//sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1

//return
@LCL
D=M
@FRAME
M=D
@5
D=D-A
A=D
D=M
@RET
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@FRAME
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@FRAME
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@FRAME
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@FRAME
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@RET
A=M
0;JMP

//

//function Class2.set 0
(Class2.set)
@0
D=A
(Class2.set.localInit )
@Class2.set.localEnd
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
D=D-1
@Class2.set.localInit
0;JMP
(Class2.set.localEnd )

//push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//pop static 0
@SP
AM=M-1
D=M
@Class2.vm0
M=D

//push argument 1
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//pop static 1
@SP
AM=M-1
D=M
@Class2.vm1
M=D

//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

//return
@LCL
D=M
@FRAME
M=D
@5
D=D-A
A=D
D=M
@RET
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@FRAME
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@FRAME
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@FRAME
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@FRAME
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@RET
A=M
0;JMP

//

//function Class2.get 0
(Class2.get)
@0
D=A
(Class2.get.localInit )
@Class2.get.localEnd
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
D=D-1
@Class2.get.localInit
0;JMP
(Class2.get.localEnd )

//push static 0
@Class2.vm0
D=M
@SP
A=M
M=D
@SP
M=M+1

//push static 1
@Class2.vm1
D=M
@SP
A=M
M=D
@SP
M=M+1

//sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1

//return
@LCL
D=M
@FRAME
M=D
@5
D=D-A
A=D
D=M
@RET
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@FRAME
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@FRAME
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@FRAME
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@FRAME
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@RET
A=M
0;JMP

//

//function Sys.init 0
(Sys.init)
@0
D=A
(Sys.init.localInit )
@Sys.init.localEnd
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
D=D-1
@Sys.init.localInit
0;JMP
(Sys.init.localEnd )

//push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

//call Class1.set 2
@Class1.set$ret.2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(Class1.set$ret.2)

//pop temp 0 // Dumps the return value
@SP
AM=M-1
D=M
@5
M=D

//push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

//call Class2.set 2
@Class2.set$ret.3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(Class2.set$ret.3)

//pop temp 0 // Dumps the return value
@SP
AM=M-1
D=M
@5
M=D

//call Class1.get 0
@Class1.get$ret.4
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.get
0;JMP
(Class1.get$ret.4)

//call Class2.get 0
@Class2.get$ret.5
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.get
0;JMP
(Class2.get$ret.5)

//label WHILE
(WHILE)

//goto WHILE
@WHILE
0;JMP

(END)
@END
0;JMP