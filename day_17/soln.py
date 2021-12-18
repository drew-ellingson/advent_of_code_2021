# python soln.py  12.83s user 0.11s system 98% cpu 13.114 total

import itertools

# -------------------- Read File ----------------------

with open("input.txt") as in_file:
    txt = in_file.read().strip()
    txt = txt.replace("target area: ", "")
    x_txt, y_txt = txt.split(", ")
    x_txt = x_txt.replace("x=", "")
    y_txt = y_txt.replace("y=", "")

    x_min, x_max = (int(i) for i in x_txt.split(".."))
    y_min, y_max = (int(i) for i in y_txt.split(".."))

# -------------------- P1 -----------------------------

# did p1 with math

# -------------------- P2 -----------------------------


def _add(tup1, tup2):
    return tuple(map(sum, zip(tup1, tup2)))


def step(pos, vel):
    def sign(x):
        return (x > 0) - (x < 0)

    pos = _add(pos, vel)
    vel = (sign(vel[0]) * (abs(vel[0]) - 1), vel[1] - 1)
    return pos, vel


def get_traj(vel, step_count, y_min, x_max):
    all_pos = [(0, 0)]
    for i in range(step_count):
        pos, vel = step(all_pos[-1], vel)

        # terminate trajectory early if you've overshot
        if pos[0] > x_max or pos[1] < y_min:
            break
        all_pos.append(pos)
    return all_pos


def get_valid_vels(vel_space, target_points, step_count, y_min, x_max):
    valid_vels = []
    for i, vel in enumerate(vel_space):
        pos = get_traj(vel, step_count, y_min, x_max)
        if any(x in target_points for x in pos):
            valid_vels.append(vel)
    return valid_vels


# assuming x_min, x_max positive
# assuming y_min, y_max negative

min_x_vel = max(i for i in range(x_min) if (i ** 2 + i) / 2 < x_min)

vel_space = list(
    itertools.product(range(min_x_vel, x_max + 1), range(y_min, -1 * y_min))
)
target_points = list(
    itertools.product(range(x_min, x_max + 1), range(y_min, y_max + 1))
)

print(
    f"P2 Soln: {len(get_valid_vels(vel_space, target_points, -2 * y_min + 1, y_min, x_max))}"
)
