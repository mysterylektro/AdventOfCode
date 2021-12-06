import setup_aoc_session
from aocd.models import Puzzle
from aocd import submit
import timeit
import numpy as np


YEAR, DAY = 2021, 5
puzzle = Puzzle(year=YEAR, day=DAY)

start = timeit.default_timer()
# ---------- SOLUTION HERE ---------- #

data = puzzle.input_data.split('\n')
coords = []
max_val = 0
for line in data:
    coord1, coord2 = line.split(' -> ')
    coord1x, coord1y = tuple(map(int, coord1.split(',')))
    coord2x, coord2y = tuple(map(int, coord2.split(',')))
    coords.append(((coord1x, coord1y), (coord2x, coord2y)))
    max_val = max((max_val, coord1x, coord1y, coord2x, coord2y))

p1_count_array = np.zeros((max_val+1, max_val+1), dtype=int)
p2_count_array = np.zeros((max_val+1, max_val+1), dtype=int)
for coord1, coord2 in coords:
    min_x, max_x = min((coord1[0], coord2[0])), max((coord1[0], coord2[0]))
    min_y, max_y = min((coord1[1], coord2[1])), max((coord1[1], coord2[1]))
    if min_x == max_x or min_y == max_y:
        p1_count_array[min_x:max_x+1, min_y:max_y+1] += 1
        p2_count_array[min_x:max_x + 1, min_y:max_y + 1] += 1
    else:
        # Diagonal
        x_dir, y_dir = np.sign(coord2[0] - coord1[0]), np.sign(coord2[1] - coord1[1])
        for i in range(max_x - min_x + 1):
            p2_count_array[coord1[0] + x_dir * i, coord1[1] + y_dir * i] += 1

P1_ANSWER = len(p1_count_array[p1_count_array >= 2].flatten())
P2_ANSWER = len(p2_count_array[p2_count_array >= 2].flatten())


# ----------------------------------- #
print(f"Finished in {timeit.default_timer() - start} seconds")

submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
submit(P2_ANSWER, part="b", year=YEAR, day=DAY)
