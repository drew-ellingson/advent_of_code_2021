# python soln.py  0.43s user 0.04s system 91% cpu 0.514 total

import math
from collections import Counter

# ------- Class Setup and Input Parsing ---------------


def _add(tup1, tup2):
    """tuple addition helper"""
    return tuple(map(sum, zip(tup1, tup2)))


def _mult(scalar, tup):
    """tuple multiplication helper - assumes integer points only"""
    return tuple(int(round(scalar * a)) for a in tup)


class Line:
    def __init__(self, line_str):
        self.start, self.end = self.parse(line_str)
        self.integer_points = self.get_integer_points()

    def parse(self, line):
        start, end = line.split(" -> ")
        start = tuple(int(x) for x in start.split(","))
        end = tuple(int(x) for x in end.split(","))
        return start, end

    def get_integer_points(self):
        delta = _add(self.end, _mult(-1, self.start))
        intervals = math.gcd(*delta)
        incr = _mult(1 / intervals, delta)
        int_points = [_add(self.start, _mult(i, incr)) for i in range(intervals + 1)]
        return int_points

    def is_hor_or_ver(self):
        return self.start[0] == self.end[0] or self.start[1] == self.end[1]


with open("input.txt") as in_file:
    lines = [Line(x) for x in in_file.readlines()]

# -------------------- P1 -----------------------------

hor_or_ver_lines = [l for l in lines if l.is_hor_or_ver()]
int_points = [pt for l in hor_or_ver_lines for pt in l.integer_points]
hist = Counter(int_points)
mults = {k: v for k, v in hist.items() if v >= 2}

print(f"P1 Soln: {len(mults)}")

# -------------------- P2 -----------------------------

int_points = [pt for l in lines for pt in l.integer_points]
hist = Counter(int_points)
mults = {k: v for k, v in hist.items() if v >= 2}

print(f"P2 Soln: {len(mults)}")
