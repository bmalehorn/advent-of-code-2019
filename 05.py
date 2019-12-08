import math
from collections import defaultdict
from aoc import parse, flatten, pp, uniqc, trace
import aoc


# @trace
def read(mem, posdata, eip, index):
    val = mem[eip + index]
    for i in range(index - 1):
        posdata //= 10
    if posdata % 10 == 0:
        return mem[val]
    elif posdata % 10 == 1:
        return val
    else:
        raise Exception(
            "read(%r, %r, %r, %r) has bad posdata %r" % (mem, posdata, val, i, posdata)
        )


def step(mem, eip):
    a = mem[eip]
    opcode = a % 100
    posdata = a // 100
    if opcode == 1:
        mem[mem[eip + 3]] = read(mem, posdata, eip, 1) + read(mem, posdata, eip, 2)
        return eip + 4
    elif opcode == 2:
        mem[mem[eip + 3]] = read(mem, posdata, eip, 1) * read(mem, posdata, eip, 2)
        return eip + 4
    elif opcode == 3:
        print("input")
        mem[mem[eip + 1]] = 1
        return eip + 2
    elif opcode == 4:
        output = read(mem, posdata, eip, 1)
        print("output %r" % output)
        return eip + 2
    elif opcode == 99:
        return None
    else:
        raise Exception("bad opcode %r" % opcode)


def part1():
    mem = flatten(parse("05.txt"))
    eip = 0
    while eip is not None:
        eip = step(mem, eip)
    # pp(mem)


def part2():
    pass


part1()
