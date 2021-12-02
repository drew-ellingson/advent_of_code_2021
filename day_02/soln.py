# python soln.py  0.04s user 0.01s system 85% cpu 0.058 total

# -------------------- Read File ----------------------


def parse(line):
    dirc, mag = line.split(" ")
    mag = int(mag)
    return dirc, mag


with open("input.txt") as in_file:
    steps = list(map(parse, in_file.readlines()))

# -------------------- P1 -----------------------------

hor_pos, ver_pos = 0, 0

for dirc, mag in steps:
    if dirc == "forward":
        hor_pos += mag
    elif dirc == "down":
        ver_pos += mag
    elif dirc == "up":
        ver_pos -= mag
    else:
        raise ValueError(f"Unexpected direction: {dirc}")

print(f"P1 Answer: {hor_pos * ver_pos}")

# -------------------- P2 -----------------------------

hor_pos, ver_pos, aim = 0, 0, 0

for dirc, mag in steps:
    if dirc == "forward":
        hor_pos += mag
        ver_pos += aim * mag
    elif dirc == "down":
        aim += mag
    elif dirc == "up":
        aim -= mag
    else:
        raise ValueError(f"Unexpected direction {dirc}")

print(f"P2 Answer: {hor_pos * ver_pos}")
