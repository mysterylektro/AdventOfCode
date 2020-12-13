class Seat:
    def __init__(self, location: complex):
        self.location = location
        self.filled = False
        self.buffer = False
        self.adjacent_seats = []
        self.line_of_sight_seats = []

    def reset(self):
        self.filled = False

    def update_p1(self):
        adjacent_filled = [seat.filled for seat in self.adjacent_seats]
        if not self.filled:
            if adjacent_filled.count(True) == 0:
                self.buffer = True
            else:
                self.buffer = self.filled
        else:
            if adjacent_filled.count(True) >= 4:
                self.buffer = False
            else:
                self.buffer = self.filled

    def update_p2(self):
        los_filled = [seat.filled for seat in self.line_of_sight_seats]
        if not self.filled:
            if los_filled.count(True) == 0:
                self.buffer = True
            else:
                self.buffer = self.filled
        else:
            if los_filled.count(True) >= 5:
                self.buffer = False
            else:
                self.buffer = self.filled

    def commit(self):
        self.filled = self.buffer


def go(part2=False):
    for seat in seats:
        seat.reset()

    prev_count = 0
    for seat in seats:
        if part2:
            seat.update_p2()
        else:
            seat.update_p1()
    for seat in seats:
        seat.commit()
    new_count = [seat.filled for seat in seats].count(True)

    while prev_count != new_count:
        prev_count = new_count
        for seat in seats:
            if part2:
                seat.update_p2()
            else:
                seat.update_p1()
        for seat in seats:
            seat.commit()
        new_count = [seat.filled for seat in seats].count(True)
    return new_count


seats = [Seat(complex(i, j)) for j, line in enumerate(open('../inputs/day11.txt')) for i, char in enumerate(line) if char == 'L']
locations = [seat.location for seat in seats]
max_real = max([int(location.real) for location in locations])
max_imag = max([int(location.imag) for location in locations])
for seat in seats:
    location = seat.location
    for loc in [1j, 1+1j, 1, -1j, -1-1j, -1, 1-1j, -1+1j]:
        adj_loc = location + loc
        if any([adj_loc.real < 0, adj_loc.real > max_real, adj_loc.imag < 0, adj_loc.imag > max_imag]):
            continue
        if adj_loc in locations:
            seat.adjacent_seats.append(seats[locations.index(adj_loc)])
        for i in range(1, max([max_real, max_imag])):
            los_loc = location + loc*i
            if any([los_loc.real < 0, los_loc.real > max_real, los_loc.imag < 0, los_loc.imag > max_imag]):
                break
            if los_loc in locations:
                seat.line_of_sight_seats.append(seats[locations.index(los_loc)])
                break

print(f"Part 1 Answer: {go()}")
print(f"Part 2 Answer: {go(part2=True)}")
