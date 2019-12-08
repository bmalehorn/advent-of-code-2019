#!/usr/bin/env python

import sys

SKELETON = """
import math
from aoc import parse, flatten, pp
import aoc


def part1():
    numbers = parse("%s-easy.txt")
    pp(numbers)

def part2():
    pass

part1()
"""


def main():
    assert len(sys.argv) == 2
    number_str = "%02d" % int(sys.argv[1])
    with open("%s.txt" % number_str, "w"):
        pass
    with open("%s-easy.txt" % number_str, "w"):
        pass
    with open("%s.py" % number_str, "w") as f:
        f.write((SKELETON % number_str).strip())


main()
