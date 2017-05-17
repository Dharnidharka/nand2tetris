
//

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

//push constant 4000	// test THIS and THAT context save

//pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D

//push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D

//call Sys.main 0
@Sys.main$ret.1
D=M
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
M=D@SP
D=M
@LCL
M=D
@Sys.main
0;JMP
(Sys.main$ret.1)

//pop temp 1
@SP
AM=M-1
D=M
@6
M=D

//label LOOP
(LOOP)

//goto LOOP
@LOOP
0;JMP

//

//

//function Sys.main 5
(Sys.main)
@5
D=A
(Sys.main.localInit )
@Sys.main.localEnd
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
D=D-1
@Sys.main.localInit
0;JMP
(Sys.main.localEnd )

//push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D

//push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D

//push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop local 1
@LCL
D=M
@1
D=D+A
@addr
M=D
@SP
AM=M-1
D=M
@addr
A=M
M=D

//push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop local 2
@LCL
D=M
@2
D=D+A
@addr
M=D
@SP
AM=M-1
D=M
@addr
A=M
M=D

//push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop local 3
@LCL
D=M
@3
D=D+A
@addr
M=D
@SP
AM=M-1
D=M
@addr
A=M
M=D

//push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

//call Sys.add12 1

//pop temp 0
@SP
AM=M-1
D=M
@5
M=D

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

//push local 2
@LCL
D=M
@2
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//push local 3
@LCL
D=M
@3
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//push local 4
@LCL
D=M
@4
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
0;JMP

//

//

//function Sys.add12 0

//push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D

//push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 1
@SP
AM=M-1
D=M
@THAT
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

//push constant 12
@12
D=A
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
0;JMP

(END)
@END
0;JMP