
//

//push constant 7
@7
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

//neg
@SP
AM=M-1
D=-M
M=D
@SP
M=M+1

//push constant 5
@5
D=A
@SP
A=M
M=D
@SP
M=M+1

//lt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@TRUE267223
D;JLT
@FALSE267223
D;JGT

(TRUE267223)
@SP
A=M
M=-1
@SP
M=M+1
@END267223
0;JMP

(FALSE267223)
@SP
A=M
M=0
@SP
M=M+1
@END267223
0;JMP

(END267223)
//push constant 10
@10
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 20
@20
D=A
@SP
A=M
M=D
@SP
M=M+1

//gt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@TRUE173406
D;JGT
@FALSE173406
D;JLT

(TRUE173406)
@SP
A=M
M=-1
@SP
M=M+1
@END173406
0;JMP

(FALSE173406)
@SP
A=M
M=0
@SP
M=M+1
@END173406
0;JMP

(END173406)
(END)
@END
0;JMP