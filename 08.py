import math
from collections import defaultdict, deque
from aoc import parse, flatten, pp, uniqc, trace
import aoc


def part1():
    numbers = list(map(int, open("08.txt").read().strip()))
    width = 25
    height = 6
    size = width * height
    assert len(numbers) % size == 0
    best_count = float("inf")
    for i in range(len(numbers) // size):
        layer = numbers[i * size : (i + 1) * size]
        d = uniqc(layer)
        if d[0] < best_count:
            best_count = d[0]
            score = d.get(1, 0) * d.get(2, 0)
            print(best_count, score)


def to_str(num):
    if num == 0:
        return " "
    return str(num)

def pgrid(grid, width, height):
    out = ""
    for row in range(height):
        out += "".join(map(to_str, grid[row * width : (row + 1) * width]))
        out += "\n"
    print(out)


def part2():
    numbers = list(map(int, open("08.txt").read().strip()))
    width = 25
    height = 6
    size = width * height
    assert len(numbers) % size == 0
    image = [2] * width * height
    for i in range(len(numbers) // size):
        layer = numbers[i * size : (i + 1) * size]
        pp(layer)
        for j in range(size):
            if image[j] == 2:
                image[j] = layer[j]

    pgrid(image, width, height)


part2()
