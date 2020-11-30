d = 'NESW'
direction_key = {'N': (0, 1),
              'E': (1, 0),
              'S': (0, -1),
              'W': (-1, 0)}

x, y = 0, 0
current_d = 'N'
locations = [(x, y)]
first_duplicate = None

with open('../inputs/day1.txt') as f:
    line = f.readline()

for command in line.strip().split(', '):
    rotate, steps = command[0], int(command[1:])
    index = d.index(current_d) + (1 if rotate == 'R' else -1)
    index -= len(d) if index >= len(d) else 0
    index += len(d) if index < 0 else 0
    current_d = d[index]
    x_dir, y_dir = direction_key.get(current_d)
    for _ in range(steps):
        x += x_dir
        y += y_dir
        if first_duplicate is None:
            if (x, y) not in locations:
                locations.append((x, y))
            else:
                first_duplicate = (x, y)


print(f"Part 1 Answer: {abs(x) + abs(y)}")
print(f"Part 2 Answer: {abs(first_duplicate[0]) + abs(first_duplicate[1])}")
