import itertools


class Cube:
    def __init__(self):
        self.active = False
        self.neighbours = set()
        self.buffer = False

    def buffer_update(self):
        count = [cube.active for cube in self.neighbours].count(True)
        self.buffer = count in [2, 3] if self.active else count == 3

    def commit(self):
        self.active = self.buffer


def calc_neighbours(location):
    dims = []
    for dim in range(len(location)):
        dims.append([location[dim]-1, location[dim], location[dim]+1])
    neighbours = list(itertools.product(*dims))
    neighbours.remove(location)
    return neighbours


def update_neighbours(cubes, active_cubes):
    for loc, cube in active_cubes:
        neighbours = calc_neighbours(loc)
        for neighbour in neighbours:
            if neighbour not in cubes:
                cubes[neighbour] = Cube()
            cube.neighbours.add(cubes[neighbour])
            cubes[neighbour].neighbours.add(cube)


def buffer_cubes(cubes):
    for cube in cubes.values():
        cube.buffer_update()


def commit_cubes(cubes):
    for cube in cubes.values():
        cube.commit()


def go(dims=3):
    cubes = dict()
    for x, line in enumerate([line.strip() for line in open('../inputs/day17.txt')]):
        for y, char in enumerate(line):
            if char == '#':
                loc = tuple([x, y] + [0] * (dims - 2))
                cubes[loc] = Cube()
                cubes[loc].active = True

    update_neighbours(cubes, list(cubes.items()))
    for _ in range(6):
        buffer_cubes(cubes)
        commit_cubes(cubes)
        update_neighbours(cubes, [i for i in cubes.items() if i[1].active])

    return [cube.active for cube in cubes.values()].count(True)


print(f"Part 1 Answer: {go()}")
print(f"Part 2 Answer: {go(dims=4)}")
