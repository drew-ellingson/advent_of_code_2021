import math

# ------------ Read File and Class Setup ----------------------

with open("input.txt") as in_file:
    heights = [[int(col) for col in row.strip()] for row in in_file.readlines()]


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.low_points = self.get_low_addresses()
        self.risk_level = self.get_risk_level()
        self.basins = [self.get_basin(pt) for pt in self.low_points]

    def get_neighbor_adds(self, point):
        i, j = point
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neighbors = [
            (i + z, j + w)
            for (z, w) in deltas
            if not (
                i + z < 0
                or i + z >= len(self.grid)
                or j + w < 0
                or j + w >= len(self.grid[i])
            )
        ]

        return neighbors

    def get_neighbor_vals(self, point):
        neighbors = self.get_neighbor_adds(point)
        return [self.grid[i][j] for (i, j) in neighbors]

    def get_low_addresses(self):
        low_points = []
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                neighbors = self.get_neighbor_vals((i, j))
                if all(col < neighbor for neighbor in neighbors):
                    low_points.append((i, j))
        return low_points

    def get_risk_level(self):
        return sum(self.grid[i][j] + 1 for (i, j) in self.low_points)

    def get_basin(self, low_point):
        i, j = low_point
        new_points = [(i, j)]
        basin = []
        while len(new_points) > 0:
            basin = list(set(basin + new_points))
            next_new_points = []
            for k, l in new_points:
                neighbors = self.get_neighbor_adds((k, l))
                next_new_points = next_new_points + [
                    (a, b)
                    for (a, b) in neighbors
                    if self.grid[a][b] > self.grid[k][l] and self.grid[a][b] < 9
                ]
            new_points = next_new_points
        return basin


# -------------------- P1 -----------------------------

grid = Grid(heights)

print(f"P1 Soln: {grid.risk_level}")

# -------------------- P2 -----------------------------

biggest_basins = sorted(grid.basins, reverse=True, key=lambda x: len(x))[:3]

print(f"P2 Soln: {math.prod(len(basin) for basin in biggest_basins)}")
