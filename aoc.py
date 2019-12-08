import itertools
import pprint
import re
import os
import sys


def parse(filename, split="[^-\\d]+"):
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


def uniqc(a):
    d = {}
    for e in a:
        if e not in d:
            d[e] = 0
        d[e] += 1
    return d


assert list(uniqc([])) == list({})
assert list(uniqc([5, 5, 6])) == list({5: 2, 6: 1})


def trace(f):
    def g(*args):
        sys.stdout.write("%s%r => " % (f.__name__, args))
        sys.stdout.flush()
        res = f(*args)
        sys.stdout.write("%r\n" % res)
        sys.stdout.flush()
        return res

    return g
