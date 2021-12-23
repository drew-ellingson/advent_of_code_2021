# python day_20/soln.py  2155.36s user 6.63s system 97% cpu 36:55.52 total

import itertools

# -------------------- Class Setup ----------------------


def _add(tup1, tup2):
    return tuple(map(sum, zip(tup1, tup2)))


class EnhanceImage:
    def __init__(self, alg, ons):
        self.alg = alg
        self.ons = ons

        self._set_min_max()

        self.step = 0

        # track history of image enhancement
        self.ons_hist = [self.ons]

    def __repr__(self):
        msg = f"Enhance Alg: {self.alg}\n"
        msg = msg + "On Coords:\n"
        for on in self.ons:
            msg = msg + str(on) + "\n"
        return msg

    def _im_rep(self):

        msg = ""
        for y in range(self.min_y, self.max_y + 1):
            msg = (
                msg
                + "".join(
                    [
                        " #" if (y, x) in self.ons else " ."
                        for x in range(self.min_x, self.max_x + 1)
                    ]
                )
                + "\n"
            )
        return msg

    def _set_min_max(self):
        self.min_x = min(x[0] for x in self.ons)
        self.max_x = max(x[0] for x in self.ons)

        self.min_y = min(x[1] for x in self.ons)
        self.max_y = max(x[1] for x in self.ons)

    def enhance_pix(self, y, x):
        dirs = (-1, 0, 1)
        deltas = list(itertools.product(dirs, dirs))

        border_val = "1" if self.step % 2 == 1 and self.alg[0] == "#" else "0"

        mask = sorted([_add((y, x), d) for d in deltas])

        pixel_raw = "".join(
            [
                border_val
                if (
                    x > self.max_x or x < self.min_x or y > self.max_y or y < self.min_y
                )
                else "1"
                if (y, x) in self.ons
                else "0"
                for (y, x) in mask
            ]
        )

        output_val = self.alg[int(pixel_raw, 2)]

        return output_val

    def enhance(self):
        new_ons = []
        for y in range(self.min_y - 1, self.max_y + 2):
            for x in range(self.min_x - 1, self.max_x + 2):
                if self.enhance_pix(y, x) == "#":
                    new_ons.append((y, x))

        self.ons = new_ons
        self.ons_hist.append(self.ons)
        self._set_min_max()
        self.step += 1

    def enhance_many(self, count, disp=False):
        for i in range(count):
            self.enhance()
            print(f"Finished rep {i + 1} of {count}")
            if disp:
                print(self._im_rep())


# -------------------- P1 -----------------------------

with open("day_20/input.txt") as in_file:
    alg = in_file.readline()
    in_file.readline()
    lines = in_file.readlines()
    ons = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                ons.append((i, j))

enhance_image = EnhanceImage(alg, ons)

enhance_image.enhance_many(2)

print(f'P1 Soln: {len(enhance_image.ons)}')

# -------------------- P2 -----------------------------

enhance_image.enhance_many(48)

print(f'P2 Soln: {len(enhance_image.ons)}')
