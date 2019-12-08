import math
from collections import defaultdict, deque
from aoc import parse, flatten, pp, uniqc, trace
import aoc


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


def step(mem, eip, input):
    a = mem[eip]
    opcode = a % 100
    posdata = a // 100
    output = None

    if opcode == 1:
        mem[mem[eip + 3]] = read(mem, posdata, eip, 1) + read(mem, posdata, eip, 2)
        eip += 4
    elif opcode == 2:
        mem[mem[eip + 3]] = read(mem, posdata, eip, 1) * read(mem, posdata, eip, 2)
        eip += 4
    elif opcode == 3:
        print("input %r" % input)
        mem[mem[eip + 1]] = input
        eip += 2
    elif opcode == 4:
        output = read(mem, posdata, eip, 1)
        eip += 2
    elif opcode == 5:
        param = read(mem, posdata, eip, 1)
        val = read(mem, posdata, eip, 2)
        if param != 0:
            eip = val
        else:
            eip += 3
    elif opcode == 6:
        param = read(mem, posdata, eip, 1)
        val = read(mem, posdata, eip, 2)
        if param == 0:
            eip = val
        else:
            eip += 3
    elif opcode == 7:
        param1 = read(mem, posdata, eip, 1)
        param2 = read(mem, posdata, eip, 2)
        if param1 < param2:
            mem[mem[eip + 3]] = 1
        else:
            mem[mem[eip + 3]] = 0
        eip += 4
    elif opcode == 8:
        param1 = read(mem, posdata, eip, 1)
        param2 = read(mem, posdata, eip, 2)
        if param1 == param2:
            mem[mem[eip + 3]] = 1
        else:
            mem[mem[eip + 3]] = 0
        eip += 4
    elif opcode == 99:
        eip = None
    else:
        raise Exception("bad opcode %r" % opcode)

    return eip, output


def part1():
    mem = flatten(parse("07-easy.txt"))
    eip = 0
    phase = [4, 3, 2, 1, 0]
    i = 0
    last_output = None
    while eip is not None:
        # pp(eip, i, last_output)
        if last_output is None:
            eip, output = step(mem, eip, input=phase[i])
            if output is not None:
                print("output %r" % output)
                last_output = output
        else:
            eip, output = step(mem, eip, input=last_output)
            if output is not None:
                print("output %r" % output)
                i += 1
                last_output = None
        # elif output is not None and last_output is not None:
        #     print("output %r" % output)



def part2():
    pass


part1()
