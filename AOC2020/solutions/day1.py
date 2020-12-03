import itertools
import numpy as np

nums = [int(line.strip()) for line in open('../inputs/day1.txt')]
print(f"Part 1 Answer: {np.prod([combo for combo in itertools.combinations(nums, 2) if sum(combo) == 2020][0])}\nPart 2 Answer: {np.prod([combo for combo in itertools.combinations(nums, 3) if sum(combo) == 2020][0])}")
