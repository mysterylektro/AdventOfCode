import setup_aoc_session
from aocd.models import Puzzle
from aocd import submit
import timeit
import numpy as np

YEAR, DAY = 2021, 7
puzzle = Puzzle(year=YEAR, day=DAY)

start = timeit.default_timer()
# ---------- SOLUTION HERE ---------- #
positions = np.fromiter(map(int, puzzle.input_data.split(',')), dtype=int)
p1_min, p2_min = 1e20, 1e20
for i in range(np.max(positions)):
    n = np.abs(positions - i)
    p1_cost = np.sum(n)
    p2_cost = int(np.sum((n ** 2 + n) / 2))
    if p1_min > p1_cost:
        p1_min = p1_cost
    if p2_min > p2_cost:
        p2_min = p2_cost

P1_ANSWER, P2_ANSWER = p1_min, p2_min

# ----------------------------------- #
print(f"Finished in {timeit.default_timer() - start} seconds")

submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
submit(P2_ANSWER, part="b", year=YEAR, day=DAY)
