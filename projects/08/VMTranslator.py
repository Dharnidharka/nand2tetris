from sys import argv
from random import randint
import os
from os.path import basename

class Parser(object):

    f = ''
    tempLine = ''
    nextLine = ''

    def __init__(self, filename):
        self.f = open(filename, "r")

    def hasMoreCommands(self):
        self.tempLine = self.f.readline().strip(' ')

        if(self.tempLine == ''):
            return False

        elif(self.tempLine[0] == '/'):              #ignoring lines starting with comments
            while self.tempLine[0] == '/':
                self.tempLine = self.f.readline().strip(' ')
            return True

        else:
            return True


    def advance(self):
        self.nextLine = self.tempLine

    def commandType(self):

        if 'push' in self.nextLine:
            return 'C_PUSH'
        elif 'pop' in self.nextLine:
            return 'C_POP'
        elif 'label' in self.nextLine:
            return 'C_LABEL'
        elif 'if-goto' in self.nextLine:
            return 'C_IF'
        elif 'function' in self.nextLine:
            return 'C_FUNCTION'
        elif 'return' in self.nextLine:
            return 'C_RETURN'
        elif 'call' in self.nextLine:
            return 'C_CALL'
        elif 'goto' in self.nextLine:
            return 'C_GOTO'
        elif any(x in self.nextLine for x in ('add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not')):
            return 'C_ARITHMETIC'
        else:
            return


    def arg1(self):
        if self.commandType() == 'C_ARITHMETIC':
            return self.nextLine
        else:
            return self.nextLine.split(' ')[1]

    def arg2(self):
        return self.nextLine.split(' ')[2]

class CodeWriter(object):

    f = ''
    filename = ''
    counter = 0
    def __init__(self, filename):
        self.f = open(filename, "w")

    def setFileName(self, filename):
        self.filename = filename

    def incrementSP(self):
        self.f.writelines(['@SP', '\n', 'A=M', '\n', 'M=D', '\n', '@SP', '\n', 'M=M+1', '\n'])

    def getSegmentName(self, segment):
        return {
            'local' : 'LCL',
            'argument' : 'ARG',
            'this' : 'THIS',
            'that' : 'THAT'
        }[segment]

    def writeEnd(self):
        self.f.writelines(['\n', '(END)', '\n', '@END', '\n', '0;JMP'])

    def writeTrueFalse(self):
        self.f.writelines(['\n', '(TRUE)', '\n', '@SP', '\n', 'A=M', '\n', 'M=-1', '\n', '@SP', '\n', 'M=M+1', '\n', '@END', '\n', '0;JMP', '\n'])
        self.f.writelines(['\n', '(FALSE)', '\n', '@SP', '\n', 'A=M', '\n', 'M=0', '\n', '@SP', '\n', 'M=M+1', '\n', '@END', '\n', '0;JMP', '\n'])

    def writeArithmetic(self, command):
        print command
        if(command == 'add'):
            self.f.writelines(['@SP', '\n', 'M=M-1', '\n', 'A=M', '\n', 'D=M', '\n', '@SP', '\n', 'M=M-1', '\n', 'A=M', '\n', 'M=D+M', '\n',  '@SP', '\n', 'M=M+1', '\n'])
        elif(command == 'sub'):
            self.f.writelines(['@SP', '\n', 'M=M-1', '\n', 'A=M', '\n', 'D=M', '\n', '@SP', '\n', 'M=M-1', '\n', 'A=M', '\n', 'M=M-D', '\n',  '@SP', '\n', 'M=M+1', '\n'])
        elif(command == "neg"):
            self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=-M', '\n', 'M=D', '\n', '@SP', '\n', 'M=M+1', '\n'])
        elif(command == "not"):
            self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=!M', '\n', 'M=D', '\n', '@SP', '\n', 'M=M+1', '\n'])
        elif(command == "and"):
            self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=M', '\n', '@SP', '\n', 'AM=M-1', '\n', 'M=D&M', '\n', '@SP', '\n', 'M=M+1', '\n'])
        elif(command == "or"):
            self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=M', '\n', '@SP', '\n', 'AM=M-1', '\n', 'M=D|M', '\n', '@SP', '\n', 'M=M+1', '\n'])
        elif(command == 'eq'):
            randIndex = str(randint(1, 999999))
            self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=M', '\n', '@SP', '\n', 'AM=M-1', '\n', 'D=D-M', '\n', '@TRUE', randIndex, '\n', 'D;JEQ', '\n'])
            self.f.writelines(['@FALSE', randIndex, '\n', 'D;JNE', '\n'])
            self.f.writelines(['\n', '(TRUE', randIndex, ')', '\n', '@SP', '\n', 'A=M', '\n', 'M=-1', '\n', '@SP', '\n', 'M=M+1', '\n', '@END', randIndex, '\n', '0;JMP', '\n'])
            self.f.writelines(['\n', '(FALSE', randIndex, ')', '\n', '@SP', '\n', 'A=M', '\n', 'M=0', '\n', '@SP', '\n', 'M=M+1', '\n', '@END', randIndex, '\n', '0;JMP', '\n'])
            self.f.writelines(['\n', '(END', randIndex, ')'])
        elif(command == 'gt'):
            randIndex = str(randint(1, 999999))
            self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=M', '\n', '@SP', '\n', 'AM=M-1', '\n', 'D=M-D', '\n', '@TRUE', randIndex, '\n', 'D;JGT', '\n'])
            self.f.writelines(['@FALSE', randIndex, '\n', 'D;JLE', '\n'])
            self.f.writelines(['\n', '(TRUE', randIndex, ')', '\n', '@SP', '\n', 'A=M', '\n', 'M=-1', '\n', '@SP', '\n', 'M=M+1', '\n', '@END', randIndex, '\n', '0;JMP', '\n'])
            self.f.writelines(['\n', '(FALSE', randIndex, ')', '\n', '@SP', '\n', 'A=M', '\n', 'M=0', '\n', '@SP', '\n', 'M=M+1', '\n', '@END', randIndex, '\n', '0;JMP', '\n'])
            self.f.writelines(['\n', '(END', randIndex, ')'])
        elif(command == 'lt'):
            randIndex = str(randint(1, 999999))
            self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=M', '\n', '@SP', '\n', 'AM=M-1', '\n', 'D=M-D', '\n', '@TRUE', randIndex, '\n', 'D;JLT', '\n'])
            self.f.writelines(['@FALSE', randIndex, '\n', 'D;JGE', '\n'])
            self.f.writelines(['\n', '(TRUE', randIndex, ')', '\n', '@SP', '\n', 'A=M', '\n', 'M=-1', '\n', '@SP', '\n', 'M=M+1', '\n', '@END', randIndex, '\n', '0;JMP', '\n'])
            self.f.writelines(['\n', '(FALSE', randIndex, ')', '\n', '@SP', '\n', 'A=M', '\n', 'M=0', '\n', '@SP', '\n', 'M=M+1', '\n', '@END', randIndex, '\n', '0;JMP', '\n'])
            self.f.writelines(['\n', '(END', randIndex, ')'])
        else:
            print "invalid command"

    def writePushPop(self, command, segment, index):
        segmentName = ''
        if(command == 'C_PUSH'):
            if(segment in ['local', 'argument', 'this', 'that']):
                segmentName = self.getSegmentName(segment)
                self.f.writelines(['@', segmentName, '\n', 'D=M', '\n', '@', index, '\n', 'A=D+A', '\n', 'D=M', '\n'])
            elif(segment == 'constant'):
                self.f.writelines(['@', index, '\n', 'D=A', '\n'])
            elif(segment == 'temp'):
                tempIndex = str(int(index) + 5)
                self.f.writelines(['@', tempIndex, '\n', 'D=M', '\n'])
            elif(segment == 'pointer'):
                temp = 'THIS'
                if(int(index) == 1):
                    temp = 'THAT'
                self.f.writelines(['@', temp, '\n', 'D=M', '\n'])
            else:
                varname = basename(self.filename) + index
                self.f.writelines(['@', varname, '\n', 'D=M', '\n'])

            self.incrementSP()

        elif(command == 'C_POP'):
            if(segment in ['local', 'argument', 'this', 'that']):
                segmentName = self.getSegmentName(segment)
                self.f.writelines(['@', segmentName, '\n', 'D=M', '\n', '@', index, '\n', 'D=D+A', '\n', '@addr', '\n', 'M=D', '\n'])
                self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=M', '\n', '@addr', '\n', 'A=M', '\n', 'M=D', '\n'])
            elif(segment == 'temp'):
                tempIndex = str(int(index) + 5)
                self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=M', '\n', '@', tempIndex, '\n', 'M=D', '\n'])
            elif(segment == 'pointer'):
                temp = 'THIS'
                if(int(index) == 1):
                    temp = 'THAT'
                self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=M', '\n', '@', temp, '\n', 'M=D', '\n'])
            elif(segment == 'static'):
                varname = basename(self.filename) + index
                self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=M', '\n'])
                self.f.writelines(['@', varname, '\n', 'M=D', '\n'])
            else:
                return

        else:
            return

    def writeLabel(self, label):
        self.f.writelines(['(', label, ')', '\n'])

    def writeIf(self, label):
        self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=M', '\n', '@', label, '\n', 'D;JNE', '\n'])

    def writeGoto(self, label):
        self.f.writelines(['@', label, '\n', '0;JMP', '\n'])

    def writeCall(self, functionName, numArgs):
        self.f.writelines(['@', functionName, '$ret.', str(self.counter), '\n', 'D=A', '\n'])
        self.incrementSP()
        self.f.writelines(['@LCL', '\n', 'D=M', '\n'])
        self.incrementSP()
        self.f.writelines(['@ARG', '\n', 'D=M', '\n'])
        self.incrementSP()
        self.f.writelines(['@THIS', '\n', 'D=M', '\n'])
        self.incrementSP()
        self.f.writelines(['@THAT', '\n', 'D=M', '\n'])
        self.incrementSP()
        self.f.writelines(['@SP', '\n', 'D=M', '\n', '@', str(numArgs), '\n', 'D=D-A', '\n', '@5', '\n', 'D=D-A', '\n', '@ARG', '\n', 'M=D', '\n'])
        self.f.writelines(['@SP', '\n', 'D=M', '\n', '@LCL', '\n', 'M=D', '\n'])
        self.f.writelines(['@', functionName, '\n', '0;JMP', '\n'])
        self.f.writelines(['(', functionName, '$ret.', str(self.counter), ')', '\n'])

    def writeReturn(self):
        self.f.writelines(['@LCL', '\n', 'D=M', '\n', '@FRAME', '\n', 'M=D', '\n'])
        self.f.writelines(['@5', '\n', 'D=D-A', '\n', 'A=D', '\n', 'D=M', '\n', '@RET', '\n', 'M=D', '\n'])
        self.f.writelines(['@SP', '\n', 'AM=M-1', '\n', 'D=M', '\n', '@ARG', '\n', 'A=M', '\n', 'M=D', '\n'])
        self.f.writelines(['@ARG', '\n', 'D=M+1', '\n', '@SP', '\n', 'M=D', '\n'])
        self.f.writelines(['@FRAME', '\n', 'D=M', '\n', '@1', '\n', 'D=D-A', '\n', 'A=D', '\n', 'D=M', '\n', '@THAT', '\n', 'M=D', '\n'])
        self.f.writelines(['@FRAME', '\n', 'D=M', '\n', '@2', '\n', 'D=D-A', '\n', 'A=D', '\n', 'D=M', '\n', '@THIS', '\n', 'M=D', '\n'])
        self.f.writelines(['@FRAME', '\n', 'D=M', '\n', '@3', '\n', 'D=D-A', '\n', 'A=D', '\n', 'D=M', '\n', '@ARG', '\n', 'M=D', '\n'])
        self.f.writelines(['@FRAME', '\n', 'D=M', '\n', '@4', '\n', 'D=D-A', '\n', 'A=D', '\n', 'D=M', '\n', '@LCL', '\n', 'M=D', '\n'])
        self.f.writelines(['@RET', '\n', 'A=M', '\n', '0;JMP', '\n'])


    def writeFunction(self, functionName, numLocals):
        self.f.writelines(['(', functionName , ')', '\n'])
        self.f.writelines(['@', numLocals, '\n', 'D=A', '\n'])
        self.f.writelines(['(', functionName, '.localInit )', '\n'])
        self.f.writelines(['@', functionName, '.localEnd', '\n', 'D;JEQ', '\n'])
        self.f.writelines(['@SP', '\n', 'A=M', '\n', 'M=0', '\n', '@SP', '\n', 'M=M+1', '\n', 'D=D-1', '\n'])
        self.f.writelines(['@', functionName, '.localInit', '\n', '0;JMP', '\n'])
        self.f.writelines(['(', functionName, '.localEnd )', '\n'])

    def close(self):
        self.f.close()

def writeToFile(parser, writer):
    while parser.hasMoreCommands():
        parser.advance()
        writer.f.writelines(['\n', '//',parser.nextLine])
        if('//' in parser.nextLine):
            parser.nextLine = parser.nextLine.split('//')[0]

        ctype = parser.commandType()

        if(ctype == 'C_PUSH' or ctype == 'C_POP'):
            segment = parser.arg1().strip()
            index = parser.arg2().strip()
            writer.writePushPop(ctype, segment, index)

        elif(ctype == 'C_LABEL'):
            label = parser.arg1().strip()
            writer.writeLabel(label)

        elif(ctype == 'C_GOTO'):
            label = parser.arg1().strip()
            writer.writeGoto(label)

        elif(ctype == 'C_IF'):
            label = parser.arg1().strip()
            writer.writeIf(label)

        elif(ctype == 'C_FUNCTION'):
            label = parser.arg1().strip()
            numLocals = parser.arg2().strip()
            writer.writeFunction(label, numLocals)

        elif(ctype == 'C_RETURN'):
            writer.writeReturn()

        elif(ctype == 'C_CALL'):
            print "counter ", writer.counter
            writer.counter=writer.counter+1
            functionName = parser.arg1().strip()
            numArgs = parser.arg2().strip()
            writer.writeCall(functionName, numArgs)

        elif(ctype == 'C_ARITHMETIC'):
            command = parser.arg1().strip()
            writer.writeArithmetic(command)

def main():
    readFile = argv[1]
    writeFile = argv[2]

    if('.vm' in readFile):
        parser = Parser(readFile)
        writer = CodeWriter(writeFile)
        writer.setFileName(writeFile)
        writeToFile(parser, writer)
        writer.writeEnd()
        writer.close()

    else:
        writer = CodeWriter(writeFile)
        writer.setFileName(writeFile)
        writer.f.writelines(['@256', '\n', 'D=A', '\n', '@SP', '\n', 'M=D', '\n'])
        writer.writeCall('Sys.init', 0)
        writer.counter = writer.counter + 1

        for file in os.listdir(readFile):
            if file.endswith(".vm"):
                filename = os.path.join(readFile, file)
                writer.setFileName(file)
                parser = Parser(filename)
                writeToFile(parser, writer)

        writer.writeEnd()
        writer.close()

main()
