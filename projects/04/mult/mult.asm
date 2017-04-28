// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@R1
D=M
@n
M=D    //n=R1
@i
M=1   //i=1
@R2
M=0   //mult=0

(LOOP)
@i
D=M
@n
D=D-M
@STOP
D;JGT

@R2
D=M
@R0
D=D+M
@R2
M=D
@i
M=M+1

@LOOP
0;JMP

(STOP)

(END)
@END
0;JMP
