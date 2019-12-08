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


def main():
    mem = flatten(parse("02.txt"))
    mem[1] = 12
    mem[2] = 2
    pp(mem)
    eip = 0
    while eip is not None:
        eip = step(mem, eip)
        pp(eip, mem)
    pp(mem[0])

# That's not the right answer; your answer is too low. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 29848.) [Return to Day 2]

main()
