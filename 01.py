import math
from aoc import parse, flatten, pp
import aoc


def part1():
    numbers = flatten(parse("01.txt"))
    total = 0
    for number in numbers:
        fuel = number // 3 - 2
        pp(number, fuel)
        total += fuel
    print(total)


def part2():
    print("hello")
    numbers = flatten(parse("01.txt"))
    total = 0
    for number in numbers:
        subtotal = 0
        fuel = number
        fuel = fuel // 3 - 2
        while fuel > 0:
            subtotal += fuel
            fuel = fuel // 3 - 2

        pp(number, subtotal)
        total += subtotal
    print(total)


part2()
