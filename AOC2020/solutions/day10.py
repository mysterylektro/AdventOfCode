from functools import lru_cache


@lru_cache()
def count_paths_to_end(val):
    return 1 if val == max(j) else 0 if val not in j else count_paths_to_end(val + 1) + count_paths_to_end(val + 2) + count_paths_to_end(val + 3)


lines = list(map(int, open('../inputs/day10.txt')))
j = list(lines) + [0, max(lines) + 3]
j.sort()
diffs = [b - a for a, b in zip(j, j[1:])]
print(f"Part 1 Answer: {diffs.count(1) * (diffs.count(3))}")
print(f"Part 2 Answer: {count_paths_to_end(0)}")
