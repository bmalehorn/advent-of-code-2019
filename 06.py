import math
from collections import defaultdict
from aoc import parse, flatten, pp, uniqc, trace
import aoc


def part1():
    orbits = {}
    planets = set()
    for line in open("06.txt").read().strip().splitlines():
        a, b = line.strip().split(")")
        orbits[b] = a
        planets |= {a, b}
    pp(orbits)
    pp(planets)
    total_count = 0
    for planet in planets:
        count = 0
        current_planet = planet
        while current_planet in orbits:
            current_planet = orbits[current_planet]
            count += 1
        print("%s %s" % (planet, count))
        total_count += count
    print(total_count)


def part2():
    pass


part1()
