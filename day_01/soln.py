# time python soln.py
# real    0m0.015s
# user    0m0.015s
# sys     0m0.000s

# Read in input

with open("input.txt") as in_file:
    depths = list(map(int, in_file.readlines()))

# -------------------- P1 -----------------------------

# skipping first reading so indexing is weird
increases = [x > depths[i] for i, x in enumerate(depths[1:])]

print(f"P1 Answer: {sum(increases)}")

# -------------------- P2 -----------------------------


def window_sum(in_list, win_len):
    return [sum(in_list[i : i + win_len]) for i in range(len(in_list) - win_len + 1)]


depth_win_sums = window_sum(depths, 3)
increases = [x > depth_win_sums[i] for i, x in enumerate(depth_win_sums[1:])]

print(f"P2 Answer: {sum(increases)}")
