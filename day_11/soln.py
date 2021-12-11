import itertools

# ---------------- Class Setup ----------------------


class Octopus:
    def __init__(self, level):
        self.level = level
        self.flashed_this_step = False

    def __repr__(self):
        return f"{str(self.level):>2}"


class OctoGrid:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.addresses = [(i, j) for i in range(self.height) for j in range(self.width)]
        self.flash_count = 0
        self.step_num = 0

    def __repr__(self):
        msg = f"Step Count: {self.step_num}\nFlash Count: {self.flash_count}\nGrid:\n"
        for i in self.grid:
            msg = msg + str(i) + "\n"
        return msg

    def get_adjs(self, coord):
        adjs = [
            x for x in list(itertools.product([1, 0, -1], [1, 0, -1])) if x != (0, 0)
        ]
        return [
            (coord[0] + adj[0], coord[1] + adj[1])
            for adj in adjs
            if 0 <= coord[0] + adj[0] < self.height
            and 0 <= coord[1] + adj[1] < self.width
        ]

    def get_flash_octs(self):
        return [
            (i, j)
            for (i, j) in self.addresses
            if self.grid[i][j].level > 9 and not self.grid[i][j].flashed_this_step
        ]

    def get_flashed_octs(self):
        return [
            (i, j) for (i, j) in self.addresses if self.grid[i][j].flashed_this_step
        ]

    def flash(self, coord):
        adjs = self.get_adjs(coord)
        for i, j in adjs:
            self.grid[i][j].level += 1

        self.grid[coord[0]][coord[1]].flashed_this_step = True
        self.flash_count += 1

    def step(self):
        # increment each octopus
        for i, j in self.addresses:
            grid[i][j].level += 1

        # flash all octopuses > 9 that haven't flashed - keep doing this
        flash_oct_addrs = self.get_flash_octs()
        while len(flash_oct_addrs) > 0:
            for i, j in flash_oct_addrs:
                self.flash((i, j))
            flash_oct_addrs = self.get_flash_octs()

        # reset flashed octs to 0 and reset all flash indicators
        flashed_octs = self.get_flashed_octs()
        for i, j in flashed_octs:
            self.grid[i][j].level = 0
            self.grid[i][j].flashed_this_step = False
        self.step_num += 1

    def multi_step(self, step_count):
        for i in range(step_count):
            self.step()

    def all_octs_just_flashed(self):
        return all(self.grid[i][j].level == 0 for (i, j) in self.addresses)


# -------------------- P1 -----------------------------

with open("input.txt") as in_file:
    grid = [[Octopus(int(o)) for o in line.strip()] for line in in_file.readlines()]

octo_grid = OctoGrid(grid)
octo_grid.multi_step(100)

print(f"P1 Soln: {octo_grid.flash_count}")


# -------------------- P2 -----------------------------

while not octo_grid.all_octs_just_flashed():
    octo_grid.step()

print(f"P2 Soln: {octo_grid.step_num}")
