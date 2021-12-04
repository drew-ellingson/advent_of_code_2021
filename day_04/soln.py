# python soln.py  0.38s user 0.02s system 98% cpu 0.399 total

import re

# -------- Class Setup and Reading File --------------------


class BingoSquare:
    def __init__(self, coord, value, marked=False):
        self.coord = coord
        self.value = value
        self.marked = marked


class BingoBoard:
    def __init__(self, board):
        """board at this point is a string with spaces and newlines as in the input file"""

        ws_pattern = re.compile("\s{1,}")
        board = [re.split(ws_pattern, row.strip()) for row in board.split("\n")]
        self.board = [
            BingoSquare((i, j), int(board[i][j]))
            for i in range(len(board))
            for j in range(len(board[0]))
        ]
        self.winning_index = None

    def is_winning(self):
        max_row = max(s.coord[0] for s in self.board) + 1
        max_col = max(s.coord[1] for s in self.board) + 1

        row_win = any(
            [
                all([s.marked for s in self.board if s.coord[0] == i])
                for i in range(max_row)
            ]
        )
        col_win = any(
            [
                all([s.marked for s in self.board if s.coord[1] == i])
                for i in range(max_col)
            ]
        )

        return row_win or col_win


class BingoGame:
    def __init__(self, in_fp):
        self.instructions, self.boards = self.parse_input(in_fp)
        self.curr_instr_indx = 0
        self.score = None

    def parse_input(self, in_fp):
        with open(in_fp) as in_file:
            instructions = [int(x) for x in in_file.readline().strip().split(",")]
            in_file.readline()  # getting rid of extra blank row.
            boards = [BingoBoard(board) for board in in_file.read().split("\n\n")]
        return instructions, boards

    def play_round(self):
        curr_val = self.instructions[self.curr_instr_indx]
        for board in self.boards:
            if curr_val not in [s.value for s in board.board]:
                continue
            else:
                match_square = [s for s in board.board if s.value == curr_val][0]
                match_square.marked = True
            if board.is_winning() and not board.winning_index:
                board.winning_index = self.curr_instr_indx
        self.curr_instr_indx += 1

    def score_game(self, scoring_board):
        unmarked_sum = sum([s.value for s in scoring_board.board if not s.marked])
        return unmarked_sum * self.instructions[self.curr_instr_indx - 1]

    def play_game(self, win_condition="first"):
        over = False
        while not over:
            self.play_round()
            winners = [b for b in self.boards if b.is_winning()]
            if win_condition == "first" and len(winners) > 0:
                self.score = self.score_game(winners[0])
                over = True
            elif win_condition == "last" and len(winners) == len(self.boards):
                winning_board = max([b for b in winners], key=lambda x: x.winning_index)
                self.score = self.score_game(winning_board)
                over = True


# -------------------- P1 -----------------------------

in_fp = "input.txt"
game = BingoGame(in_fp)
game.play_game(win_condition="first")

print(f"P1 Soln: {game.score}")

# -------------------- P2 -----------------------------

game = BingoGame(in_fp)
game.play_game(win_condition="last")

print(f"P2 Soln: {game.score}")
