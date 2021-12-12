# python soln.py  787.04s user 7.78s system 99% cpu 13:20.38 total

from collections import Counter

# -------------------- Read File ----------------------

with open("input.txt") as in_file:
    edges = [x.strip().split("-") for x in in_file.readlines()]

# -------------------- P1 -----------------------------


def get_adjs(label):
    second_label = [edge[1] for edge in edges if edge[0] == label]
    first_label = [edge[0] for edge in edges if edge[1] == label]
    return second_label + first_label


def build_one_step_one_path(path, dupe_visit=0):
    label = path[-1]

    # already done
    if label == "end":
        return [path]

    adjs = [x for x in get_adjs(label) if not x in path or x.isupper()]

    # allow one small cave to be visited twice in p2, as long as not start or end
    if dupe_visit == 1:
        counts = Counter(path)
        if not any(v >= 2 for k, v in counts.items() if k.islower()):
            adjs = adjs + [
                x
                for x in get_adjs(label)
                if x.islower() and x in path and x not in ["start", "end"]
            ]

    # dead end path
    if adjs == []:
        return []

    return [path + [adj] for adj in adjs]


def build_one_step_many_paths(paths, dupe_visit=0):
    output_paths = []
    new_paths = [build_one_step_one_path(path, dupe_visit=dupe_visit) for path in paths]
    for path_col in new_paths:
        output_paths = output_paths + path_col

    output_paths = [x for x in output_paths if x != []]
    return output_paths


def build_all_step_many_paths(paths, dupe_visit=0):
    while not all(path[-1] == "end" for path in paths):
        paths = build_one_step_many_paths(paths, dupe_visit=dupe_visit)
    return paths


paths = [["start"]]
paths = build_all_step_many_paths(paths)
print(f"P1 Soln: {len(paths)}")

# -------------------- P2 -----------------------------

paths = [["start"]]
paths = build_all_step_many_paths(paths, dupe_visit=1)
print(f"P2 Soln: {len(paths)}")
