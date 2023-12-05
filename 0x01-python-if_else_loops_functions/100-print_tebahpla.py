#!/usr/bin/python3
from itertools import chain

for i in chain(range(122, 96, -1), range(64, 90, -1)):
    if i % 2:
        i = i - 32
    print("{:c}".format(i), end="")
