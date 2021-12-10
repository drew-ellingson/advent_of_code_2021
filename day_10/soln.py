# python soln.py  0.04s user 0.01s system 83% cpu 0.060 total

# -------------------- Read File ----------------------

with open("input.txt") as in_file:
    lines = [line.strip() for line in in_file.readlines()]

# -------------------- P1 -----------------------------

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}


def score(line):
    stack = []
    for i, c in enumerate(line):
        if c in pairs.keys():
            stack.append(c)
        else:
            if c == pairs[stack[-1]]:
                stack.pop()
            else:
                return scores[c], stack
    return 0, stack


print(f"P1 Soln: {sum(score(line)[0] for line in lines)}")

# -------------------- P2 -----------------------------

incompletes = [line for line in lines if score(line)[0] == 0]
ac_scores = {")": 1, "]": 2, "}": 3, ">": 4}


def score_autocomplete(line):
    stack = score(line)[1]
    ac_score = 0
    for c in reversed(stack):
        ac_score *= 5
        ac_score += ac_scores[pairs[c]]
    return ac_score


line_ac_scores = sorted([score_autocomplete(line) for line in incompletes])

print(f"P1 Soln: {line_ac_scores[int((len(line_ac_scores) - 1) / 2)]}")
