# python soln.py  7.91s user 0.03s system 99% cpu 8.017 total

import itertools

# -------------------- Read File ----------------------


def parse(line):
    signal, output = [x.strip().split(" ") for x in line.split(" | ")]
    return signal, output


with open("input.txt") as in_file:
    input_lines = [parse(line) for line in in_file.readlines()]

# -------------------- P1 -----------------------------


def get_uniques(output_signal):
    return list([x for x in output_signal if len(x) in (2, 3, 4, 7)])


all_uniques = sum(len(get_uniques(l[1])) for l in input_lines)

print(f"P1 Soln: {all_uniques}")

# -------------------- P2 -----------------------------

valids = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

valids_rev_lookup = {v: k for k, v in valids.items()}

seg_maps = ["".join(x) for x in itertools.permutations("abcdefg", 7)]


def transform(digit, seg_map):
    """apply `abcdefg -> segmap` transformation to `digit`"""

    base = "abcdefg"
    return "".join(sorted([seg_map[base.index(c)] for c in digit]))


def transform_all(digits, seg_map):
    return [transform(digit, seg_map) for digit in digits]


def is_valid_map(digits, seg_map):
    trans_digits = transform_all(digits, seg_map)
    return all(d in valids.values() for d in trans_digits)


def get_valid_map(signal):
    for seg_map in seg_maps:
        if is_valid_map(signal, seg_map):
            return seg_map


def score(line):
    signal, output = line
    valid_map = get_valid_map(signal)
    resolved_output = transform_all(output, valid_map)
    return int("".join([str(valids_rev_lookup[i]) for i in resolved_output]))


overall_score = sum(score(line) for line in input_lines)

print(f"P2 Soln: {overall_score}")
