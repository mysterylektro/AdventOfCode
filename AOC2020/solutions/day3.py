import numpy as np


def tree_slope(right, down):
    with open('../inputs/day3.txt') as f:
        lines = f.readlines()

    tree_count = 0
    idx = 0

    for line in lines[down::down]:
        idx += right
        if idx >= len(line.strip()):
            idx -= len(line.strip())
        if line[idx] == '#':
            tree_count += 1

    return tree_count


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(f"Part 1 Answer: {tree_slope(3, 1)}")
print(f"Part 2 Answer: {np.prod([tree_slope(*args) for args in slopes])}")
