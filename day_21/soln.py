# python day_21/soln.py  0.24s user 0.01s system 96% cpu 0.267 total

import itertools
from collections import defaultdict, Counter

# -------------------- Class Setup ----------------------


class Player:
    def __init__(self, pos, score=0):
        self.pos = pos
        self.score = score

    def move(self):
        pass


class Dice:
    def __init__(self):
        self.state = 1
        self.roll_count = 0

    def roll(self):
        output = self.state
        self.state = 1 if self.state == 100 else self.state + 1
        self.roll_count += 1
        return output


class DiracGame:
    def __init__(self, p1, p2, die):
        self.p1 = p1
        self.p2 = p2
        self.die = die
        self.round_num = 0
        self.active_player = self.p1
        self.game_over = False

    def __repr__(self):
        msg = ""
        msg = msg + f"Active Player: {self.active_player}\n"
        msg = msg + f"P1 pos: {self.p1.pos}, P1 Score: {self.p1.score}\n"
        msg = msg + f"P2 pos: {self.p2.pos}, P2 Score: {self.p2.score}\n"
        return msg

    def round(self):
        val = 0
        for i in range(3):
            val += self.die.roll()

        self.active_player.pos = (self.active_player.pos + val - 1) % 10 + 1
        self.active_player.score += self.active_player.pos

        if self.active_player.score >= 1000:
            self.game_over = True

        self.round_num += 1
        self.active_player = p2 if self.active_player == p1 else p1

    def full_game(self):
        while not self.game_over:
            self.round()

    def score(self):
        return self.active_player.score * self.die.roll_count


class QuantumGame:
    def __init__(self, p1_pos, p2_pos):
        self.status = {(p1_pos, 0, p2_pos, 0): 1}
        self.active_player = 1
        self.round_num = 0
        self.p1_wins = 0
        self.p2_wins = 0

    def __repr__(self):
        msg = f"Active Player: {self.active_player}\n"
        msg = f"Round: {self.round_num}\n"
        for x, y in self.status.items():
            msg = msg + f"Status: {x}, mult: {y}\n"
        return msg

    def round(self):
        new_status = defaultdict(lambda: 0)
        for (p1_pos, p1_score, p2_pos, p2_score), mult in self.status.items():
            if self.active_player == 1:
                change_pos, change_score = p1_pos, p1_score
            else:
                change_pos, change_score = p2_pos, p2_score

            for add_val, add_mult in possible_adds.items():
                new_pos = (change_pos + add_val - 1) % 10 + 1
                new_score = change_score + new_pos

                if self.active_player == 1:
                    new_status[new_pos, new_score, p2_pos, p2_score] += add_mult * mult
                else:
                    new_status[p1_pos, p1_score, new_pos, new_score] += add_mult * mult

        self.status = new_status
        self.round_num += 1
        self.active_player = 2 if self.active_player == 1 else 1

    def full_game(self):
        while len(self.status) > 0:
            self.round()

            wins = {k: v for k, v in self.status.items() if k[1] >= 21 or k[3] >= 21}

            for k, v in wins.items():
                if k[1] >= 21:
                    self.p1_wins += v
                elif k[3] >= 21:
                    self.p2_wins += v

            self.status = {
                k: v for k, v in self.status.items() if k[1] < 21 and k[3] < 21
            }

        return self.p1_wins, self.p2_wins


# -------------------- P1 -----------------------------

with open("day_21/input.txt") as in_file:
    p1_pos = int(in_file.readline().strip()[-1])
    p2_pos = int(in_file.readline().strip()[-1])

    p1 = Player(p1_pos)
    p2 = Player(p2_pos)
    die = Dice()

    game = DiracGame(p1, p2, die)

    game.full_game()
    print(game.score())

# -------------------- P2 -----------------------------

roll_vals = [1, 2, 3]
possible_triples = list(itertools.product(roll_vals, roll_vals, roll_vals))
possible_adds = Counter(sum(x) for x in possible_triples)

game = QuantumGame(p1_pos, p2_pos)

print(f"P2 Soln: {max(game.full_game())}")
