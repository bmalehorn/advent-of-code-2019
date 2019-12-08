#!/usr/bin/env python

# nodemon 03.py -e py,txt

import sys

SKELETON = """
import math
from collections import defaultdict
from aoc import parse, flatten, pp, uniqc
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
