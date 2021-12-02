import setup_aoc_session
from aocd.models import Puzzle
from aocd import submit
import timeit

YEAR, DAY = 2021, 2
puzzle = Puzzle(year=YEAR, day=DAY)

start = timeit.default_timer()
# ---------- SOLUTION HERE ---------- #

depth1 = depth2 = pos = aim = 0

for line in puzzle.input_data.split('\n'):
    tokens = line.split(' ')
    op, val = tokens[0], int(tokens[1])
    if op == 'forward':
        pos += val
        depth2 += aim * val
    if op == 'up':
        depth1 -= val
        aim -= val
    if op == 'down':
        depth1 += val
        aim += val

P1_ANSWER = depth1 * pos
P2_ANSWER = depth2 * pos

# ----------------------------------- #
print(f"Finished in {timeit.default_timer() - start} seconds")

submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
submit(P2_ANSWER, part="b", year=YEAR, day=DAY)
