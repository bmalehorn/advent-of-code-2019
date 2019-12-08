import itertools
from collections import defaultdict, deque
import pprint
import re
import os
import sys


def parse(filename, split="[^-\\d\\w]+"):
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
    d = defaultdict(lambda: 0)
    for e in a:
        if e not in d:
            d[e] = 0
        d[e] += 1
    return d


assert list(uniqc([])) == list({})
assert list(uniqc([5, 5, 6])) == list({5: 2, 6: 1})


def trace(f):
    def g(*args, **kwargs):
        sys.stdout.write("%s%r => " % (f.__name__, args))
        sys.stdout.flush()
        res = f(*args, **kwargs)
        sys.stdout.write("%r\n" % res)
        sys.stdout.flush()
        return res

    return g


# https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
# Python function to print permutations of a given list
def permutations(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    a = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1 :]

        # Generating all permutations where m is first
        # element
        for p in permutations(remLst):
            a.append([m] + p)
    return a
