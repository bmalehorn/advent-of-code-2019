import itertools
import pprint


def parse(filename):
    return [
        list(map(int, line.strip().split()))
        for line in open(filename).read().strip().splitlines()
    ]


def flatten(a):
    return list(itertools.chain(*a))


def pp(*args):
    ppObj = pprint.PrettyPrinter()
    if len(args) == 1:
        ppObj.pprint(args[0])
    else:
        ppObj.pprint(args)
