from collections import defaultdict

coord_mapping = {'nw': (-1, 1), 'ne': (1, 1), 'sw': (-1, -1), 'se': (1, -1), 'e': (2, 0), 'w': (-2, 0)}
tiles = defaultdict(lambda: True)
tiles[(0, 0)] = True

for line in open('../inputs/day24.txt'):
    line = list(line.strip())
    directions = []
    while len(line) > 0:
        val = line.pop(0)
        if val in ['s', 'n']:
            val += line.pop(0)
        directions.append(coord_mapping.get(val))
    x, y = 0, 0
    for direction in directions:
        x, y = x + direction[0], y + direction[1]
    tiles[(x, y)] = not tiles[(x, y)]

black_tiles = set([loc for loc, white in tiles.items() if not white])
print(len(black_tiles))

for _ in range(100):
    no_flips = set()
    white_neighbours = defaultdict(int)
    for loc in black_tiles:
        b_neighbour_count = 0
        for dir in coord_mapping.values():
            x, y = dir[0] + loc[0], dir[1] + loc[1]
            if (x, y) in black_tiles:
                b_neighbour_count += 1
            else:
                white_neighbours[(x, y)] += 1
        if 1 <= b_neighbour_count <= 2:
            no_flips.add(loc)

    white_flips = set([loc for loc, count in white_neighbours.items() if count == 2])
    black_tiles = set.union(white_flips, no_flips)

print(len(black_tiles))
