import numpy
from itertools import combinations
with open('../inputs/day24.txt') as f:
    lines = f.readlines()

weights = [float(line) for line in lines]


def min_qe(num_groups):
    target_weight = float(sum(weights)/num_groups)
    combos = []
    for i in range(len(weights)):
        combos.extend([combo for combo in combinations(weights, i) if sum(combo) == target_weight])
        if len(combos) > 0:
            break

    qes = [numpy.prod(combo) for combo in combos]
    return int(min(qes))


qe = min_qe(3)
print(f"Part 1 Answer: {qe}")
qe = min_qe(4)
print(f"Part 1 Answer: {qe}")
