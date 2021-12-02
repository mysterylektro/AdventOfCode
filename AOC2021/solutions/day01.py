import setup_aoc_session
from aocd.models import Puzzle
from aocd import submit
import timeit
import numpy as np

YEAR, DAY = 2021, 1
puzzle = Puzzle(year=YEAR, day=DAY)

start = timeit.default_timer()
# ---------- SOLUTION HERE ---------- #

data = tuple(map(int, puzzle.input_data.split('\n')))
P1_ANSWER = sum(1 for i in range(1, len(data)) if data[i-1] < data[i])
sliding_sum = np.convolve([1, 1, 1], data)
P2_ANSWER = sum(1 for i in range(3, len(sliding_sum)) if sliding_sum[i-1] < sliding_sum[i])

# ----------------------------------- #
print(f"Finished in {timeit.default_timer() - start} seconds")
submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
submit(P2_ANSWER, part="b", year=YEAR, day=DAY)
