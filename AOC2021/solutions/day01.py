import setup_aoc_session
from aocd.models import Puzzle
from aocd import submit

YEAR, DAY = 2021, 1
puzzle = Puzzle(year=YEAR, day=DAY)

# ---------- SOLUTION HERE ---------- #

data = tuple(map(int, puzzle.input_data.split('\n')))
P1_ANSWER = sum(1 for i in range(1, len(data)) if data[i-1] < data[i])
P2_ANSWER = sum(1 for i in range(1, len(data)) if data[i-3] < data[i])

# ----------------------------------- #

submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
submit(P2_ANSWER, part="b", year=YEAR, day=DAY)
