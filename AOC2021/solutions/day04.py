import setup_aoc_session
from aocd.models import Puzzle
from aocd import submit
import timeit
import numpy as np

YEAR, DAY = 2021, 4
puzzle = Puzzle(year=YEAR, day=DAY)

start = timeit.default_timer()
# ---------- SOLUTION HERE ---------- #

data = puzzle.input_data.split('\n\n')
numbers = np.fromiter(map(int, data[0].split(',')), dtype=int)
boards = np.array([[list(map(int, row.split())) for row in board.split('\n')] for board in data[1:]])
winners = np.full_like(boards, fill_value=0, dtype=int)

P1_ANSWER = P2_ANSWER = None
for num in numbers:
    winners[boards == num] = 1
    winning_boards = np.append(np.argwhere(np.sum(winners, axis=1) == boards.shape[1]),
                               np.argwhere(np.sum(winners, axis=2) == boards.shape[2]), axis=0)
    if len(winning_boards) > 0:
        if P1_ANSWER is None:
            winning_board, marked = boards[winning_boards[0, 0]], winners[winning_boards[0, 0]]
            P1_ANSWER = np.sum(winning_board[marked == 0]) * num

        if boards.shape[0] == 1:
            P2_ANSWER = np.sum(boards[0][winners[0] == 0]) * num
            break

        boards = np.delete(boards, winning_boards[:, 0], 0)
        winners = np.delete(winners, winning_boards[:, 0], 0)

# ----------------------------------- #
print(f"Finished in {timeit.default_timer() - start} seconds")

submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
submit(P2_ANSWER, part="b", year=YEAR, day=DAY)
