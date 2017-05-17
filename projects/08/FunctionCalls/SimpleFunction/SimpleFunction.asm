
//

//function SimpleFunction.test 2
(SimpleFunction.test)
@2
D=A
(SimpleFunction.test.localInit )
@SimpleFunction.test.localEnd
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
D=D-1
@SimpleFunction.test.localInit
0;JMP
(SimpleFunction.test.localEnd )

//push local 0
@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//push local 1
@LCL
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1

//not
@SP
AM=M-1
D=!M
M=D
@SP
M=M+1

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

//add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1

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

(END)
@END
0;JMP