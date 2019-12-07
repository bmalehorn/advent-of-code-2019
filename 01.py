import math
from aoc import parse, flatten, pp
import aoc


def main():
    numbers = flatten(parse("01.txt"))
    total = 0
    for number in numbers:
        fuel = number // 3 - 2
        pp(number, fuel)
        total += fuel
    print(total)


main()
