
//

//push constant 0    
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop local 0         // initializes sum = 0
@LCL
D=M
@0
D=D+A
@addr
M=D
@SP
AM=M-1
D=M
@addr
A=M
M=D

//label LOOP_START
(LOOP_START)

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

//pop local 0	        // sum = sum + counter
@LCL
D=M
@0
D=D+A
@addr
M=D
@SP
AM=M-1
D=M
@addr
A=M
M=D

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

//push constant 1
@1
D=A
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

//pop argument 0      // counter--
@ARG
D=M
@0
D=D+A
@addr
M=D
@SP
AM=M-1
D=M
@addr
A=M
M=D

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

//if-goto LOOP_START  // If counter > 0, goto LOOP_START
@SP
AM=M-1
D=M
@LOOP_START
D;JNE

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

(END)
@END
0;JMP