import itertools
import numpy as np

with open('../inputs/day1.txt') as f:
    nums = list(map(int, f.readlines()))

answer = np.prod([combo for combo in itertools.combinations(nums, 2) if sum(combo) == 2020][0])
print(f"Part 1 Answer: {answer}")
answer = np.prod([combo for combo in itertools.combinations(nums, 3) if sum(combo) == 2020][0])
print(f"Part 2 Answer: {answer}")
