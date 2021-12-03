# python soln.py  0.03s user 0.01s system 86% cpu 0.056 total

from collections import Counter

# -------------------- Read File ----------------------

with open("input.txt") as in_file:
    nums = [x.strip() for x in in_file.readlines()]

# -------------------- P1 -----------------------------


def filter_val(nums, pos, criteria="max"):
    """return most or least common value of bit in `nums` for given position `pos`"""

    vals = [num[pos] for num in nums]
    hist = Counter(vals)

    func = max if criteria == "max" else min
    default = "1" if criteria == "max" else "0"
    common = [i for i, x in hist.items() if x == func(hist.values())]

    return default if len(common) > 1 else common[0]


gamma = "".join([filter_val(nums, i) for i in range(len(nums[0]))])
epsilon = "".join(["1" if a == "0" else "0" for a in gamma])

power_rating = int(gamma, 2) * int(epsilon, 2)

print(f"P1 Soln: {power_rating}")

# -------------------- P2 -----------------------------


def bit_filter(nums, criteria="max", pos=0):
    """recursively filter `nums` according to majority next-bit rules"""
    if len(nums) == 1:
        return nums[0]
    else:
        common = filter_val(nums, pos, criteria=criteria)
        nums = list(filter(lambda x: x[pos] == common, nums))
        return bit_filter(nums, criteria=criteria, pos=pos + 1)


oxy_rating = bit_filter(nums, criteria="max")
co2_rating = bit_filter(nums, criteria="min")

life_support_rating = int(oxy_rating, 2) * int(co2_rating, 2)

print(f"P2 Soln: {life_support_rating}")
