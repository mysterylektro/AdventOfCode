import setup_aoc_session
from aocd.models import Puzzle
from aocd import submit
import timeit

YEAR, DAY = 2021, 19
puzzle = Puzzle(year=YEAR, day=DAY)

start = timeit.default_timer()
# ---------- SOLUTION HERE ---------- #



# ----------------------------------- #
print(f"Finished in {timeit.default_timer() - start} seconds")

submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
# submit(P2_ANSWER, part="b", year=YEAR, day=DAY)
