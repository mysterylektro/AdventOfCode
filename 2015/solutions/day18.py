class Light:
    def __init__(self, status: bool, stuck=False):
        self.status = status
        self.neighbours = []
        self.buffer = False
        self.stuck = stuck

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def update(self):
        if self.stuck:
            self.status = True
        else:
            self.status = self.buffer

    def check_neighbours(self):
        count = 0
        for neighbour in self.neighbours:
            if neighbour.status:
                count += 1

        if self.status:
            if count == 2 or count == 3:
                self.buffer = True
            else:
                self.buffer = False
        else:
            if count == 3:
                self.buffer = True


def emulate(stuck=False):

    with open('../inputs/day18.txt') as f:
        lines = f.readlines()

    light_array = []
    for row, line in enumerate(lines):
        line.strip()
        light_row = []
        for column, char in enumerate(line):
            if char == '#':
                light_row.append(Light(True))
            elif char == '.':
                light_row.append(Light(False))
            else:
                continue
        light_array.append(light_row)

    for y in range(0, len(light_array)):
        for x in range(0, len(light_array[0])):
            light = light_array[y][x]
            for x_val in [x - 1, x, x + 1]:
                if x_val < 0 or x_val == len(light_array[0]):
                    continue
                for y_val in [y - 1, y, y + 1]:
                    if y_val < 0 or y_val == len(light_array):
                        continue
                    if x_val == x and y_val == y:
                        continue
                    light.add_neighbour(light_array[y_val][x_val])

    if stuck:
        light_array[0][0].stuck = True
        light_array[0][99].stuck = True
        light_array[99][0].stuck = True
        light_array[99][99].stuck = True

    for i in range(0, 100):
        for light_row in light_array:
            for light in light_row:
                light.check_neighbours()

        for light_row in light_array:
            for light in light_row:
                light.update()

    count = 0
    for light_row in light_array:
        for light in light_row:
            if light.status:
                count += 1

    return count


print(f"Part 1 Answer: {emulate()}")
print(f"Part 2 Answer: {emulate(stuck=True)}")
