import math
from collections import defaultdict
from aoc import parse, flatten, pp
import aoc


def step(mem, eip):
    a = mem[eip]
    if a == 99:
        return None
    a, b, c, d = mem[eip : eip + 4]
    assert a in [1, 2]
    if a == 1:
        mem[d] = mem[b] + mem[c]
        return eip + 4
    elif a == 2:
        mem[d] = mem[b] * mem[c]
        return eip + 4


# 3716250
def part1():
    mem = flatten(parse("02.txt"))
    mem[1] = 12
    mem[2] = 2
    # pp(mem)
    eip = 0
    while eip is not None:
        eip = step(mem, eip)
        # pp(eip, mem)
    pp(mem[0])


def get_output(mem, noun, verb):
    mem = mem[:]
    mem[1] = noun
    mem[2] = verb
    eip = 0
    while eip is not None:
        eip = step(mem, eip)
        # pp(eip, mem)
    return mem[0]


def part2():
    mem = flatten(parse("02.txt"))
    for noun in range(0, 99):
        for verb in range(0, 99):
            output = get_output(mem, noun, verb)
            if output == 19690720:
                pp(noun, verb, output)
                pp(100 * noun + verb)


part2()
