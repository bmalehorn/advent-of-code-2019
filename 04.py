import math
from collections import defaultdict
from aoc import parse, flatten, pp, uniqc
import aoc


def has_double(password):
    digits = list(map(int, str(password)))
    for i in range(len(digits) - 1):
        a, b = digits[i], digits[i + 1]
        if a == b:
            return True
    return False


def never_decreasing(password):
    digits = list(map(int, str(password)))
    for i in range(len(digits) - 1):
        a, b = digits[i], digits[i + 1]
        if a > b:
            return False
    return True


def valid(password):
    return (
        len(str(password)) == 6 and has_double(password) and never_decreasing(password)
    )

assert valid(111111)
assert not valid(223450)
assert not valid(123789)


# 1694
def part1():
    # low = 156218
    # high = 652527
    count = 0
    for password in range(156218, 652527 + 1):
        if valid(password):
            # pp(password)
            count += 1
    print("count = %r" % count)


def has_double2(password):
    digits = list(map(int, str(password)))
    return 2 in uniqc(digits).values()


def valid2(password):
    return (
        len(str(password)) == 6 and has_double2(password) and never_decreasing(password)
    )


assert valid2(112233)
assert not valid2(123444)
assert valid2(111122)

# 1148
def part2():
    count = 0
    for password in range(156218, 652527 + 1):
        if valid2(password):
            # pp(password)
            count += 1
    print("count = %r" % count)

    pass


part2()
