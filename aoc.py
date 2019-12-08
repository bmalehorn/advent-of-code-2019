import itertools
import pprint
import re


def parse(filename, split="[^\\d]+"):
    return [
        list(map(int, re.compile(split).split(line.strip())))
        for line in open(filename).read().strip().splitlines()
        if not line.startswith("#")
    ]


def flatten(a):
    return list(itertools.chain(*a))


def pp(*args):
    ppObj = pprint.PrettyPrinter()
    if len(args) == 1:
        ppObj.pprint(args[0])
    else:
        ppObj.pprint(args)
