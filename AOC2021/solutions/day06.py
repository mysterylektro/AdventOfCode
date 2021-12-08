import setup_aoc_session
from aocd.models import Puzzle
from aocd import submit
import timeit

YEAR, DAY = 2021, 6
puzzle = Puzzle(year=YEAR, day=DAY)

start = timeit.default_timer()
# ---------- SOLUTION HERE ---------- #


def simulate(num_days, offset_list):
    t = [1] * num_days
    for i in range(num_days):
        t[i] = t[i - 9] + t[i - 7]
    return sum(t[num_days-i] for i in offset_list)


data = list(map(int, puzzle.input_data.split(',')))
P1_ANSWER = simulate(79, data)
P2_ANSWER = simulate(255, data)


# ----------------------------------- #
print(f"Finished in {timeit.default_timer() - start} seconds")

submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
submit(P2_ANSWER, part="b", year=YEAR, day=DAY)
