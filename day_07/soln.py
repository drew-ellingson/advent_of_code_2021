# python soln.py  0.81s user 0.02s system 98% cpu 0.835 total

# -------------------- Read File ----------------------

with open("input.txt") as in_file:
    crabs = [int(x) for x in in_file.read().split(",")]

# -------------------- P1 -----------------------------


def fuel_cost(crabs, align_pos, weighted=False):
    if weighted:
        return sum(triangle_nums(abs(c - align_pos)) for c in crabs)
    return sum(abs(c - align_pos) for c in crabs)


def min_fuel_cost(crabs, weighted=False):
    min_pos, max_pos = min(crabs), max(crabs)
    return min(
        fuel_cost(crabs, i, weighted=weighted) for i in range(min_pos, max_pos + 1)
    )


print(f"P1 Soln: {min_fuel_cost(crabs)}")

# -------------------- P2 -----------------------------

costs = {}


def triangle_nums(pos_diff):
    """memoized triangle numbers"""
    if pos_diff not in costs.keys():
        costs[pos_diff] = sum(i for i in range(1, pos_diff + 1))
    return costs[pos_diff]


print(f"P2 Soln: {min_fuel_cost(crabs, weighted=True)}")
