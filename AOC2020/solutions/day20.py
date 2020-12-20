import numpy as np
import math


class Tile:
    def __init__(self, tile_id, data):
        self.tile_id = tile_id
        self.data = data
        self.edges = [self.top_edge(), self.bottom_edge(), self.left_edge(), self.right_edge()]

    def top_edge(self):
        return self.data[0, :]

    def bottom_edge(self):
        return self.data[-1, :]

    def left_edge(self):
        return self.data[:, 0]

    def right_edge(self):
        return self.data[:, -1]

    def mirror_x(self):
        return Tile(self.tile_id, np.flip(self.data, axis=1))

    def mirror_y(self):
        return Tile(self.tile_id, np.flip(self.data, axis=0))

    def rotate(self):
        return Tile(self.tile_id, np.rot90(self.data))

    def no_border(self):
        return self.data[1:-1, 1:-1]

    def print_tile(self):
        for row in range(self.data.shape[0]):
            print(self.data[row, :])

    def find_common_edge(self, tile_list):
        common_edges = []
        reversed_edges = []
        for i, edge in enumerate(self.edges):
            for t in tile_list:
                if t == self:
                    continue
                if list(edge) in list(map(list, t.edges)):
                    common_edges.append(edge)
                if list(edge)[::-1] in list(map(list, t.edges)):
                    reversed_edges.append(edge)
        return common_edges, reversed_edges

    def generate_orientations(self):
        return [self, self.mirror_x(), self.mirror_y(), self.mirror_x().mirror_y(), self.rotate(),
                self.rotate().mirror_x(), self.rotate().mirror_y(), self.rotate().mirror_x().mirror_y()]


def place_tiles(all_combinations, grid, seen, pos = (0, 0)):
    x, y = pos
    if y == len(grid):
        return grid

    for tile in all_combinations:
        if tile.tile_id in seen:
            continue

        if x > 0 and any(grid[y][x - 1].right_edge() != tile.left_edge()):
            continue

        if y > 0 and any(grid[y - 1][x].bottom_edge() != tile.top_edge()):
            continue

        grid[y][x] = tile

        result = place_tiles(all_combinations, grid, seen | {tile.tile_id}, (x + 1, y) if x < len(grid[0]) - 1 else (0, y + 1))
        if result is not None:
            grid = result
            break

        grid[y][x] = None

    else:
        grid = None

    return grid


def stitch_tiles(tile_placements):
    rows = []
    for row in tile_placements:
        r = None
        for tile in row:
            if r is None:
                r = tile.no_border()
            else:
                r = np.concatenate((r, tile.no_border()), axis=1)
        rows.append(r)
    output = None
    for row in rows:
        if output is None:
            output = row
        else:
            output = np.concatenate((output, row))
    return output


def sea_monster_template():
    definition = """                  # \n#    ##    ##    ###\n #  #  #  #  #  #   """.split('\n')
    template = []
    for y, line in enumerate(definition):
        for x, char in enumerate(line):
            if char == '#':
                template.append((x, y))
    return template


def find_sea_monsters(image, template):
    count = 0
    positions = set()
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            found = True
            sea_monster_coords = set()
            for x_offset, y_offset in template:
                pos_x, pos_y = x + x_offset, y + y_offset
                if pos_x >= image.shape[0] or pos_y >= image.shape[1]:
                    found = False
                    break
                if image[pos_y, pos_x] != 1:
                    found = False
                    break
                sea_monster_coords.add((pos_x, pos_y))
            if found:
                count += 1
                positions = positions | sea_monster_coords
            else:
                continue
    return count, positions


tiles = []
for string in open('../inputs/day20.txt').read().split('\n\n')[:-1]:
    tile_id = int(string.split('\n')[0][5:-1])
    data = [list(map(int, x.replace('#', '1').replace('.', '0'))) for x in string.split('\n')[1:]]
    data = np.array([np.array(x) for x in data])
    tiles.append(Tile(tile_id, data))

grid_size = int(np.sqrt(len(tiles)))

corners = []
for tile in tiles:
    num_common = sum(map(len, tile.find_common_edge(tiles)))
    if num_common == 2:
        corners.append(tile)

print(f"Part 1 Answer: {math.prod([t.tile_id for t in corners])}")

all_combos = []
for tile in tiles:
    all_combos.extend(tile.generate_orientations())
tile_placement = place_tiles(all_combos, [[None for _ in range(grid_size)] for _ in range(grid_size)], set())
image = stitch_tiles(tile_placement)
template = sea_monster_template()
image_orientations = [image,
                      np.flip(image, axis=0),
                      np.flip(image, axis=1),
                      np.flip(np.flip(image, axis=0), axis=1),
                      np.rot90(image),
                      np.flip(np.rot90(image), axis=0),
                      np.flip(np.rot90(image), axis=1),
                      np.flip(np.flip(np.rot90(image), axis=0), axis=1)]

for image_orientation in image_orientations:

    num, positions = find_sea_monsters(image_orientation, template)
    if num > 0:
        roughness = 0
        for x in range(image_orientation.shape[0]):
            for y in range(image_orientation.shape[1]):
                if (x, y) not in positions and image_orientation[y, x] == 1:
                    roughness += 1
        print(f'Part 2 Answer: {roughness}')
        break