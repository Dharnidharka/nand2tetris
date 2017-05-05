import sys
import re

def getComp(comp):
    return {
        '0' : '0101010',
        '1' : '0111111',
        '-1': '0111010',
        'D' : '0001100',
        'A' : '0110000',
        'M' : '1110000',
        '!D': '0001101',
        '!A': '0110001',
        '!M': '1110001',
        '-D': '0001111',
        '-A': '0110011',
        '-M': '1110011',
        'D+1':'0011111',
        'A+1':'0110111',
        'M+1':'1110111',
        'D-1':'0001110',
        'A-1':'0110010',
        'M-1':'1110010',
        'D+A':'0000010',
        'D+M':'1000010',
        'D-A':'0010011',
        'D-M':'1010011',
        'A-D':'0000111',
        'M-D':'1000111',
        'D&A':'0000000',
        'D&M':'1000000',
        'D|A':'0010101',
        'D|M':'1010101'
    }[comp]

def getDest(dest):
    return {
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111'
    }[dest]

def getJmp(jmp):
    return {
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }[jmp]


def A_instruction(symbol):
    if(not symbol.isdigit()):
        symbol = symbolTable[symbol]

    symbol = int(symbol)
    f.write('0' + bin(symbol)[2:].zfill(15) + '\n')

def C_instruction(line):
    comp = ''
    dest = ''
    jmp = ''
    comp_jmp = ''
    if '=' in line:
        dest_comp_jmp = line.split('=')
        dest = getDest(dest_comp_jmp[0])
        comp_jmp = dest_comp_jmp[1]
    else:
        dest = '000'
        comp_jmp = line

    if ';' in comp_jmp:
        comp_jmp_spl = comp_jmp.split(';')
        jmp= getJmp(comp_jmp_spl[1])
        comp = comp_jmp_spl[0]
    else:
        jmp = '000'
        comp = comp_jmp

    #print comp
    comp = getComp(comp)
    f.write('111' + comp + dest + jmp + '\n')


def parser(content):
    content = [x.strip() for x in content]
    n = len(content)
    for x in range(n):
        line = content[x].strip()
        if(len(line) > 0):
            if(line[0] == '/'):
                continue
            elif(line[0] == '@'):
                A_instruction(line[1:])
            else:
                C_instruction(line)

def getPredefinedSymbols():
    return {
        'R0': 0,
        'R1': 1,
        'R2': 2,
        'R3': 3,
        'R4': 4,
        'R5': 5,
        'R6': 6,
        'R7': 7,
        'R8': 8,
        'R9': 9,
        'R10': 10,
        'R11': 11,
        'R12': 12,
        'R13': 13,
        'R14': 14,
        'R15': 15,
        'SCREEN': 16384,
        'KBD': 24576,
        'SP': 0,
        'LCL': 1,
        'ARG': 2,
        'THIS': 3,
        'THAT': 4,
    }

def first_pass(content, symbolTable):
        content = [x.strip() for x in content]
        n = len(content)
        count = 0
        content_pass1 = [];
        for x in range(n):
            line = content[x].strip()
            if(len(line) > 0):
                if(line[0] == '/'):
                    continue
                elif(line[0] == '('):
                    symbolTable[line[1:-1]] = count
                else:
                    temp = line.split('/')[0].strip()
                    content_pass1.append(temp)
                    count = count + 1

        return content_pass1

def second_pass(content, symbolTable):
        n = len(content)
        RAM = 16
        for x in range(n):
            line = content[x].strip("'")
            if(line[0] == '@'):
                symbol = line.split('@')[1]
                if(not symbol.isdigit()):
                    if(symbol not in symbolTable):
                        symbolTable[symbol] = RAM
                        RAM = RAM + 1

fname = sys.argv[1]
wname = sys.argv[2]
with open(fname) as f:
    content = f.readlines()

f = open(wname, 'w')
symbolTable = getPredefinedSymbols()

content_pass = first_pass(content, symbolTable)
second_pass(content_pass, symbolTable)

parser(content_pass)
f.close()
