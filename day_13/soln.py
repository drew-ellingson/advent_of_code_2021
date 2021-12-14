# python soln.py  0.04s user 0.01s system 88% cpu 0.062 total

# -------------------- Read File ----------------------

with open("input.txt") as in_file:
    points, instrs = in_file.read().strip().split("\n\n")
    points = [tuple(int(x) for x in pt.strip().split(",")) for pt in points.split("\n")]
    instrs = [
        instr.replace("fold along ", "").split("=") for instr in instrs.split("\n")
    ]
    instrs = [(x[0], int(x[1])) for x in instrs]

# -------------------- P1 -----------------------------


def map_pt(pt, fold):
    if fold[0] == "x":
        return (2 * fold[1] - pt[0], pt[1]) if pt[0] > fold[1] else pt
    return (pt[0], 2 * fold[1] - pt[1]) if pt[1] > fold[1] else pt


fold1_pts = list(set(map_pt(pt, instrs[0]) for pt in points))

print(f"P1 Soln: {len(fold1_pts)}")

# -------------------- P2 -----------------------------


def disp(points):
    max_x = max(pt[0] for pt in points)
    max_y = max(pt[1] for pt in points)

    for y in range(max_y + 1):
        outputs = list("#" if (x, y) in points else "." for x in range(max_x + 1))
        print("".join(outputs))


for fold in instrs:
    points = [map_pt(pt, fold) for pt in points]

disp(points)
