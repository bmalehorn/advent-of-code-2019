import math
from collections import defaultdict
from aoc import parse, flatten, pp
import aoc


def write(grid, wire, id):
    x = 0
    y = 0
    for e in wire:
        direction = e[0]
        dist = int(e[1:])

        if direction == "R":
            dx = 1
            dy = 0
        elif direction == "L":
            dx = -1
            dy = 0
        elif direction == "D":
            dx = 0
            dy = 1
        elif direction == "U":
            dx = 0
            dy = -1
        else:
            raise Exception("bad direction: %r", direction)

        for _ in range(dist):
            grid[(x, y)].add(id)
            x += dx
            y += dy


def part1():
    wire1, wire2 = [
        line.split(",") for line in open("03.txt").read().strip().splitlines()
    ][:2]
    grid = defaultdict(lambda: set())
    write(grid, wire1, 1)
    write(grid, wire2, 2)
    closest = float('inf')
    for x, y in grid:
        if len(grid[(x, y)]) > 1 and (x, y) != (0, 0):
            pp(x, y, grid[(x, y)])
            pp(abs(x) + abs(y))
            closest = min(closest, abs(x) + abs(y))

    print(closest)

def part2():
    pass


part1()
