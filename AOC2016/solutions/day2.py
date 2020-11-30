direction_key = {'U': (0, -1),
                 'D': (0, 1),
                 'L': (-1, 0),
                 'R': (1, 0)}

numpad1 = {(0, 0): 1,
           (1, 0): 2,
           (2, 0): 3,
           (0, 1): 4,
           (1, 1): 5,
           (2, 1): 6,
           (0, 2): 7,
           (1, 2): 8,
           (2, 2): 9}

numpad2 = {(2, 0): 1,
           (1, 1): 2,
           (2, 1): 3,
           (3, 1): 4,
           (0, 2): 5,
           (1, 2): 6,
           (2, 2): 7,
           (3, 2): 8,
           (4, 2): 9,
           (1, 3): 'A',
           (2, 3): 'B',
           (3, 3): 'C',
           (2, 4): 'D'}


def move(current_position, direction, numpad):
    x, y = current_position
    x_add, y_add = direction_key.get(direction)
    x += x_add
    y += y_add

    if (x, y) in numpad.keys():
        return x, y
    return current_position


pos1 = (1, 1)
pos2 = (0, 2)
code1 = []
code2 = []

with open('../inputs/day2.txt') as f:
    lines = f.readlines()

for line in lines:
    for command in line.strip():
        pos1 = move(pos1, command, numpad1)
        pos2 = move(pos2, command, numpad2)
    code1.append(numpad1.get(pos1))
    code2.append(numpad2.get(pos2))

print(f"Part 1 Answer: {''.join(list(map(str, code1)))}")
print(f"Part 2 Answer: {''.join(list(map(str, code2)))}")
