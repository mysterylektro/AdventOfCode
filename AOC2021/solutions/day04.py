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
boards = np.array([[list(map(int, row.split())) for row in board.split('\n')] for board in data[1:-1]])
winners = np.full_like(boards, fill_value=False, dtype=bool)

winning_board = None
P1_ANSWER = None
for num in numbers:
    winners[boards == num] = True
    # Check if winner exists
    row_winners = np.array([[all(winners[i, j, :]) for j in range(winners.shape[1])] for i in range(winners.shape[0])])
    col_winners = np.array([[all(winners[i, :, j]) for j in range(winners.shape[2])] for i in range(winners.shape[0])])
    if any(row_winners.flatten()) or any(col_winners.flatten()):
        # Find winning board
        idx = np.argwhere(row_winners == True) if any(row_winners.flatten()) else np.argwhere(col_winners == True)
        if P1_ANSWER is None:
            winning_board, marked = boards[idx[0, 0]], winners[idx[0, 0]]
            unmarked_numbers = winning_board[~marked]
            P1_ANSWER = np.sum(unmarked_numbers) * num

        if boards.shape[0] == 1:
            marked = winners[0]
            unmarked_numbers = boards[0][~marked]
            P2_ANSWER = np.sum(unmarked_numbers) * num
            break

        # Remove this board from consideration
        boards = np.delete(boards, idx[:, 0], 0)
        winners = np.delete(winners, idx[:, 0], 0)

# ----------------------------------- #
print(f"Finished in {timeit.default_timer() - start} seconds")

submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
submit(P2_ANSWER, part="b", year=YEAR, day=DAY)
