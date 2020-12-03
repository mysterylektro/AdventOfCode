import numpy as np
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def tree_slope(right, down):
    lines = [line.strip() for line in open('../inputs/day3.txt')]
    tree_count, idx = 0, 0
    for line in lines[down::down]:
        idx += right
        idx -= len(line) if idx >= len(line) else 0
        tree_count += 1 if line[idx] == '#' else 0
    return tree_count


print(f"Part 1 Answer: {tree_slope(3, 1)}")
print(f"Part 2 Answer: {np.prod([tree_slope(*args) for args in slopes])}")
