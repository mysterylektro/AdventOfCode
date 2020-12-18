from collections import defaultdict
import itertools
from functools import lru_cache


@lru_cache()
def calc_neighbours(loc):
    neighbours = list(itertools.product(*[[loc[dim] - 1, loc[dim], loc[dim] + 1] for dim in range(len(loc))]))
    neighbours.remove(loc)
    return neighbours


def get_active_cubes(active_cubes):
    ret_cubes, all_neighbours = set(), defaultdict(int)
    for active_cube in active_cubes:
        neighbours = calc_neighbours(active_cube)
        count = len([c for c in neighbours if c in active_cubes])
        _ = ret_cubes.add(active_cube) if count in [2, 3] else None
        for neighbour in neighbours:
            if neighbour not in active_cubes:
                all_neighbours[neighbour] += 1

    _ = [ret_cubes.add(neighbour) for neighbour, active_count in all_neighbours.items() if active_count == 3]
    return ret_cubes


def go(dims=3):
    active_cubes = set()
    _ = [active_cubes.add(tuple([x, y] + [0] * (dims - 2))) for x, line in enumerate(open('../inputs/day17.txt')) for y, char in enumerate(line[:-1]) if char == '#']
    for _ in range(6):
        active_cubes = get_active_cubes(active_cubes)
    return len(active_cubes)


print(f"Part 1 Answer: {go()}")
print(f"Part 2 Answer: {go(dims=4)}")
