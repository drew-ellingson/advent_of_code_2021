import json
import math
import itertools

# -------------------- Class Definitions ----------------------


class SnailNum:
    def __init__(self, str_rep):
        self.str_rep = str_rep
        self.num = json.loads(str_rep)

    def __repr__(self):
        msg = ""
        for key, val in self.__dict__.items():
            msg = msg + f"{key}: {val}\n"
        return msg

    def reduce_step(self):
        old_val = self.str_rep
        self.explode()
        if self.str_rep == old_val:
            self.split()
        return self.str_rep

    def reduce(self):
        old_val = self.str_rep
        step = 0
        while (new_val := self.reduce_step()) != old_val:  # sloppyaf
            step += 1
            old_val = new_val
            continue
        return self.str_rep

    def add(self, snail_num):
        self.str_rep = f"[{self.str_rep},{snail_num.str_rep}]"
        self.num = json.loads(self.str_rep)
        self.reduce()
        return self

    def explode(self):
        nums = "0123456789"
        depth = 0
        explode = False
        for i, c in enumerate(self.str_rep):
            if c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
            elif depth > 4:
                explode = True
                explode_idx = i
                if self.str_rep[i + 1] in nums:  # account for 2 digit nums
                    left = int(self.str_rep[i : i + 2])
                    left_dd = True
                    right_idx = i + 3
                else:
                    left = int(self.str_rep[i])
                    left_dd = False
                    right_idx = i + 2
                if self.str_rep[right_idx + 1] in nums:  # account for 2 digit nums
                    right = int(self.str_rep[right_idx : right_idx + 2])
                    right_dd = True
                else:
                    right = int(self.str_rep[right_idx])
                    right_dd = False
                try:
                    next_left_idx = max(j for j in range(i) if self.str_rep[j] in nums)
                except ValueError:
                    next_left_idx = None
                try:
                    next_right_idx = min(
                        j
                        for j in range(right_idx + 2, len(self.str_rep))
                        if self.str_rep[j] in nums
                    )
                except ValueError:
                    next_right_idx = None
                break
        if explode:
            if next_right_idx:
                if self.str_rep[next_right_idx + 1] in nums:
                    right_rep_val = int(
                        self.str_rep[next_right_idx : next_right_idx + 2]
                    )
                    new_str_1 = (
                        self.str_rep[:next_right_idx]
                        + str(right + right_rep_val)
                        + self.str_rep[next_right_idx + 2 :]
                    )
                else:
                    right_rep_val = int(self.str_rep[next_right_idx])
                    new_str_1 = (
                        self.str_rep[:next_right_idx]
                        + str(right + right_rep_val)
                        + self.str_rep[next_right_idx + 1 :]
                    )
            else:
                new_str_1 = self.str_rep

            tail_index = i + 4 + (1 if left_dd else 0) + (1 if right_dd else 0)
            new_str_2 = new_str_1[: i - 1] + "0" + new_str_1[tail_index:]

            if next_left_idx:
                if self.str_rep[next_left_idx - 1] in nums:
                    left_rep_val = int(
                        self.str_rep[next_left_idx - 1 : next_left_idx + 1]
                    )
                    new_str_3 = (
                        new_str_2[: next_left_idx - 1]
                        + str(left + left_rep_val)
                        + new_str_2[next_left_idx + 1 :]
                    )
                else:
                    left_rep_val = int(self.str_rep[next_left_idx])
                    new_str_3 = (
                        new_str_2[:next_left_idx]
                        + str(left + left_rep_val)
                        + new_str_2[next_left_idx + 1 :]
                    )
            else:
                new_str_3 = new_str_2

            self.str_rep = new_str_3
            self.num = json.loads(self.str_rep)

            return self.str_rep

    # assuming vals < 100
    def split(self):
        nums = "0123456789"
        for i, c in enumerate(self.str_rep[:-2]):
            if c in nums and self.str_rep[i + 1] in nums:
                split_num = int(self.str_rep[i : i + 2])
                split_left = math.floor(int(split_num) / 2)
                split_right = math.ceil(int(split_num) / 2)
                self.str_rep = (
                    self.str_rep[:i]
                    + f"[{split_left},{split_right}]"
                    + self.str_rep[i + 2 :]
                )
                self.num = json.loads(self.str_rep)
                break
        return self.str_rep

    def mag(self):
        if type(self.num) == int:
            return self.num
        else:
            return (
                3 * SnailNum(str(self.num[0])).mag()
                + 2 * SnailNum(str(self.num[1])).mag()
            )


# -------------------- P1 -----------------------------

with open("day_18/input.txt") as in_file:
    str_nums = [x.strip() for x in in_file.readlines()]
    snail_nums = [SnailNum(x) for x in str_nums]

init = snail_nums[0]
for x in snail_nums[1:]:
    init.add(x)

print(f"P1 Soln: {init.mag()}")


# -------------------- P2 -----------------------------

# need to reinstantiate every time cause i modified in place
max_sum = max(
    SnailNum(x).add(SnailNum(y)).mag() for x in str_nums for y in str_nums if x != y
)

print(f"P2 Soln: {max_sum}")
