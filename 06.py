import math
from collections import defaultdict, deque
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
    siblings = defaultdict(set)
    planets = set()
    for line in open("06.txt").read().strip().splitlines():
        a, b = line.strip().split(")")
        siblings[a].add(b)
        siblings[b].add(a)
        planets |= {a, b}
    pp(siblings)
    pp(planets)
    queue = deque([("YOU", 0)])
    visited = set()
    while queue:
        node, steps = queue.popleft()
        if node == "SAN":
            pp(steps - 2)
            return
        if node in visited:
            continue
        visited.add(node)
        pp(node)
        for child in siblings[node]:
            queue.append((child, steps + 1))
    print("bad exit")


part2()
