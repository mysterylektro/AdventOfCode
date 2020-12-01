import itertools
import numpy as np

with open('../inputs/day1.txt') as f:
    lines = f.readlines()

nums = list(map(int, lines))

combos = itertools.combinations(nums, 2)
answer = None
for combo in combos:
    if sum(combo) == 2020:
        answer = np.prod(combo)
        break

print(f"Part 1 Answer: {answer}")

combos = itertools.combinations(nums, 3)
answer = None
for combo in combos:
    if sum(combo) == 2020:
        answer = np.prod(combo)
        break

print(f"Part 2 Answer: {answer}")