import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n\n") if line]
REGISTERS = [
    int(x)
    for x in lines[0]
    .replace("Register ", "")
    .replace("A: ", "")
    .replace("B: ", "")
    .replace("C: ", "")
    .split("\n")
]
commands = [int(x) for x in lines[1].replace("Program: ", "").split(",")]

A = 0
B = 1
C = 2


def to_param(registers, d):
    if d >= 0 and d < 4:
        return d
    elif d == 4:
        return registers[A]
    elif d == 5:
        return registers[B]
    elif d == 6:
        return registers[C]
    else:
        return None


def xor(a, b):
    a = f"{a:01000b}"
    b = f"{b:01000b}"
    result = ""
    for i, j in zip(a, b):
        if i == "1" and j == "0":
            result += "1"
        elif i == "0" and j == "1":
            result += "1"
        else:
            result += "0"
    return int(result, 2)


def solve(registers):
    ip = 0
    output = []

    while ip < len(commands):
        opcode = commands[ip]
        param = to_param(registers, commands[ip + 1])
        # print("ip", "command", "param", "registers")
        # print(ip, commands[ip], param, registers)
        # input()

        if opcode == 0:
            # ADV => A div 2^ param
            registers[A] = int(registers[A] // (2**param))
        elif opcode == 1:
            # BXL => bitwise XOR of B and param
            registers[B] = xor(registers[B], commands[ip + 1])
        elif opcode == 2:
            # BST => param mod 8
            registers[B] = param % 8
        elif opcode == 3:
            # JNZ => jump based on A
            if registers[A] != 0:
                ip = commands[ip + 1]
                continue
        elif opcode == 4:
            # BXC => bitwise XOR of B and C
            registers[B] = xor(registers[B], registers[C])
        elif opcode == 5:
            # OUT
            output.append(param % 8)
        elif opcode == 6:
            # BDV => ADV but for B
            registers[B] = int(registers[A] // (2**param))
        elif opcode == 7:
            # CDV => ADV but for C
            registers[C] = int(registers[A] // (2**param))
        else:
            assert False
        ip += 2
    return output


result = ",".join([str(x) for x in solve(REGISTERS[:])])

# Part 1 = 6,0,6,3,0,2,3,1,6
print(f"answer = {result}")

# There is a pattern in the output, for example the last digit rotates through the values 7 5 6 2 3 0 1
# But as more digits are added to the front, the last digit rotates slower with A. E.g. when there are two digits, we get eight 7s then eight 5s, and so.
# When there are x digits, the last digit rotates every 8**(x-1), the second to last rotates every 8**(x-2), and so on.
# In other words:
#   The first value changes when increasing A by one
#   The second value changes when increasing A by 8
#   The third value changes when increasing A by 64
#   And so on

a = 1
output = []

while output != commands:
    registers = REGISTERS[:]
    registers[A] = a
    output = solve(registers)
    if len(output) < len(commands):
        # Short cut: multiplying by 8 increases the number of digits outputed by 1
        a *= 8
        continue
    for i in range(len(output)):
        if output[~i] != commands[~i]:
            a += 8 ** (len(commands) - 1 - i)
            break

# Part 2 = 236539226447469
print(f"answer = {a}")
