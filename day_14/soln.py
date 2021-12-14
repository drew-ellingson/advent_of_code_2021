# python soln.py  0.05s user 0.01s system 90% cpu 0.073 total

from collections import Counter, defaultdict
import copy

# -------------------- Read File ----------------------

with open("input.txt") as in_file:
    start = in_file.readline().strip()
    in_file.readline()
    rules = [x.strip().split(" -> ") for x in in_file.readlines()]
    reps = {k: k[0] + v + k[1] for k, v in rules}

# -------------------- P1 -----------------------------


def one_step(poly, reps):
    trans = [reps.get(poly[i : i + 2], poly[i : i + 2]) for i in range(len(poly) - 1)]
    return "".join(x if i == 0 else x[1:] for i, x in enumerate(trans))


def many_step(poly, reps, steps):
    for i in range(steps):
        poly = one_step(poly, reps)
    return poly


def get_answer(poly):
    hist = Counter(poly)
    return max(hist.values()) - min(hist.values())


print(f"P1 Answer: {get_answer(many_step(start, reps, 10))}")

# -------------------- P2 -----------------------------


def fancy_step(pair_hist, reps):
    """track tuple counts across polymer insertions"""

    new_pair_hist = copy.deepcopy(pair_hist)
    for k, v in pair_hist.items():
        new_pair_hist[k] -= v
        new_pair_hist[reps[k][:2]] += v
        new_pair_hist[reps[k][1:]] += v
    return new_pair_hist


def many_fancy_step(pair_hist, reps, steps):
    for i in range(steps):
        pair_hist = fancy_step(pair_hist, reps)
    return pair_hist


def count_occ(pair_hist, char, bound_chars):
    """translate from tuple counts to total character counts, accounting for end chars"""

    # 'CC' gets counted differently than 'CB'
    total_occ = sum(k.count(char) * v for k, v in pair_hist.items() if char in k)

    # first and last characters don't get doublecounted - the rest do.
    total_occ += bound_chars.count(char)
    return int(total_occ / 2)


def fancy_get_answer(pair_hist, bound_chars):
    chars = list(set("".join(pair_hist.keys())))
    max_count = max(count_occ(pair_hist, char, bound_chars) for char in chars)
    min_count = min(count_occ(pair_hist, char, bound_chars) for char in chars)
    return max_count - min_count


pair_hist = defaultdict(lambda: 0)

for i in range(len(start) - 1):
    pair_hist[start[i : i + 2]] += 1

pair_hist = many_fancy_step(pair_hist, reps, 40)

print(fancy_get_answer(pair_hist, start[0] + start[-1]))
