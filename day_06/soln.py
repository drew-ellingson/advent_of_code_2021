import math
import copy
from collections import Counter, defaultdict

# -------------------- Read File ----------------------

with open("input.txt") as in_file:
    fishes = [int(x) for x in in_file.read().split(",")]
    fishes2 = copy.deepcopy(fishes)

# -------------------- P1 -----------------------------


def one_day(fishes):
    new_fishes = [6 if x == 0 else x - 1 for x in fishes] + [8] * fishes.count(0)
    return new_fishes


def mult_days(fishes, day_count):
    i = 0
    while i < day_count:
        fishes = one_day(fishes)
        i += 1
    return fishes


fishes = mult_days(fishes, 80)

print(f"P1 Soln: {len(fishes)}")

# -------------------- P2 -----------------------------

# this was too slow but i like it so i'm keeping it in the solution file.


def fish_sum(fish, days):
    """recursively find # of fish added by a single `fish` and it's descendants over `days`."""
    if days <= fish:
        return 1
    else:
        spawn_days = days - fish
        new_fish = math.ceil(spawn_days / 7)
        return 1 + sum(fish_sum(8, spawn_days - i * 7 - 1) for i in range(new_fish))


def fish_counts(days):
    return {k: fish_sum(k, days) for k in range(6)}


def all_fish_sum(fishes, days):
    all_fish_counts = fish_counts(days)
    return sum(all_fish_counts[fish] for fish in fishes)


# print(all_fish_sum(fishes2, 256))

# ------------ New Approach -----------------------------

fish_counts = Counter(fishes2)


def p2_one_day(fish_counts):
    new_fish_counts = defaultdict(lambda: 0)
    for k, v in fish_counts.items():
        if k < 1:
            continue
        new_fish_counts[k - 1] += v
    new_fish_counts[6] += fish_counts[0]
    new_fish_counts[8] += fish_counts[0]
    return new_fish_counts


def p2_mult_days(fish_counts, days):
    i = 0
    while i < days:
        fish_counts = p2_one_day(fish_counts)
        i += 1
    return sum(fish_counts.values())


print(f"P2 Soln: {p2_mult_days(fish_counts, 256)}")
