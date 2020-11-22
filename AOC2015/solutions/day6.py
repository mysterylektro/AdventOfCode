import numpy as np
from typing import Tuple


def switch(array,
           coord1: Tuple[int, int],
           coord2: Tuple[int, int],
           status: bool):
    array[coord1[0]:coord2[0]+1, coord1[1]:coord2[1]+1] = status


def toggle(array,
           coord1: Tuple[int, int],
           coord2: Tuple[int, int]):
    array[coord1[0]:coord2[0]+1, coord1[1]:coord2[1]+1] = np.invert(array[coord1[0]:coord2[0]+1, coord1[1]:coord2[1]+1])


def change_brightness(array,
                      coord1: Tuple[int, int],
                      coord2: Tuple[int, int],
                      n: int):
    array[coord1[0]:coord2[0] + 1, coord1[1]:coord2[1] + 1] += n
    array[array < 0] = 0


def get_coord(string: str) -> Tuple[int, int]:
    x, y = map(int, string.split(','))
    return x, y


with open('../inputs/day6.txt') as f:
    lines = f.readlines()

array = np.full((1000, 1000), False, dtype=bool)

for line in lines:
    tokens = line.split(' ')
    if tokens[0] == 'turn':
        status = (True if tokens[1] == 'on' else False)
        coord1 = get_coord(tokens[2])
        coord2 = get_coord(tokens[4])
        switch(array, coord1, coord2, status)

    elif tokens[0] == 'toggle':
        coord1 = get_coord(tokens[1])
        coord2 = get_coord(tokens[3])
        toggle(array, coord1, coord2)
    else:
        continue

print(f"Part 1 Answer: {np.count_nonzero(array)}")

array = np.full((1000, 1000), 0)

for line in lines:
    tokens = line.split(' ')
    if tokens[0] == 'turn':
        n = (1 if tokens[1] == 'on' else -1)
        coord1 = get_coord(tokens[2])
        coord2 = get_coord(tokens[4])
    elif tokens[0] == 'toggle':
        n = 2
        coord1 = get_coord(tokens[1])
        coord2 = get_coord(tokens[3])
    else:
        continue
    change_brightness(array, coord1, coord2, n)

print(f"Part 1 Answer: {np.sum(array)}")
