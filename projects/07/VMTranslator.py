from sys import argv
from random import randint
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
        if any(x in self.nextLine for x in ('add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not')):
            return 'C_ARITHMETIC'
        elif 'push' in self.nextLine:
            return 'C_PUSH'
        elif 'pop' in self.nextLine:
            return 'C_POP'
        else:
            return 'C_RETURN'

    def arg1(self):
        if self.commandType() == 'C_ARITHMETIC':
            return self.nextLine
        elif self.commandType() == 'C_PUSH':
            return self.nextLine.split(' ')[1]
        elif self.commandType() == 'C_POP':
            return self.nextLine.split(' ')[1]
        else:
            return 0

    def arg2(self):
        return self.nextLine.split(' ')[2]

class CodeWriter(object):

    f = ''
    filename = ''
    def __init__(self, filename):
        self.f = open(filename, "w")

    def setFileName(self, filename):
        self.filename = filename

    def incrementSP(self):
        self.f.writelines(['@SP', '\n', 'A=M', '\n', 'M=D', '\n', '@SP', '\n', 'M=M+1', '\n'])

    def decrementSP(self):
        self.f.writelines([])

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

        #self.incrementSP()
        #self.f.write(command)
        #self.f.write('\n')

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

    def close(self):
        self.f.close()

def main():
    readFile = argv[1]
    writeFile = argv[2]
    parser = Parser(readFile)
    writer = CodeWriter(writeFile)
    writer.setFileName(writeFile)
    while parser.hasMoreCommands():
        parser.advance()
        writer.f.writelines(['\n', '//',parser.nextLine])
        ctype = parser.commandType()

        if(ctype == 'C_ARITHMETIC'):
            command = parser.arg1().strip()
            writer.writeArithmetic(command)

        elif(ctype == 'C_PUSH' or ctype == 'C_POP'):
            segment = parser.arg1().strip()
            index = parser.arg2().strip()
            writer.writePushPop(ctype, segment, index)

    writer.writeEnd()
    writer.close()

main()
