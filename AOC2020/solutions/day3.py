import numpy as np
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def tree_slope(right, down):
    lines, tree_count, idx = [line.strip() for line in open('../inputs/day3.txt')], 0, 0
    for line in lines[down::down]:
        idx += right if idx < len(line)-right else right-len(line)
        tree_count += 1 if line[idx] == '#' else 0
    return tree_count


print(f"Part 1 Answer: {tree_slope(*slopes[1])}\nPart 2 Answer: {np.prod([tree_slope(*args) for args in slopes])}")
