import setup_aoc_session
from aocd.models import Puzzle
from aocd import submit
import timeit
import numpy as np

YEAR, DAY = 2021, 3
puzzle = Puzzle(year=YEAR, day=DAY)

start = timeit.default_timer()
# ---------- SOLUTION HERE ---------- #

data = np.array([[int(i) for i in d] for d in puzzle.input_data.split('\n')])
gamma_rate = [1 if np.sum(data[:, i]) >= data.shape[0] // 2 else 0 for i in range(data.shape[1])]
gamma_rate_num = np.sum([2**i for i in range(data.shape[1]) if gamma_rate[::-1][i]])
epsilon_rate_num = np.sum([2**i for i in range(data.shape[1]) if not gamma_rate[::-1][i]])

P1_ANSWER = gamma_rate_num * epsilon_rate_num

oxy_rating = co2_rating = data

for i in range(data.shape[1]):
    if oxy_rating.shape[0] != 1:
        mask = oxy_rating[:, i] == 1
        oxy_rating = oxy_rating[mask] if oxy_rating[mask].shape[0] >= oxy_rating[~mask].shape[0] else oxy_rating[~mask]

    if co2_rating.shape[0] != 1:
        mask = co2_rating[:, i] == 0
        co2_rating = co2_rating[mask] if co2_rating[mask].shape[0] <= co2_rating[~mask].shape[0] else co2_rating[~mask]

oxy_rate_num = np.sum([2**i for i in range(12) if oxy_rating.flatten()[::-1][i]])
co2_rate_num = np.sum([2**i for i in range(12) if co2_rating.flatten()[::-1][i]])

P2_ANSWER = oxy_rate_num * co2_rate_num

# ----------------------------------- #
print(f"Finished in {timeit.default_timer() - start} seconds")

submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
submit(P2_ANSWER, part="b", year=YEAR, day=DAY)
