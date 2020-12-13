class Seat:
    def __init__(self):
        self.filled = False
        self.buffer = False
        self.adjacent_seats = set()
        self.line_of_sight_seats = set()

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
        if self.filled != self.buffer:
            self.filled = self.buffer


def go(part2=False):
    def update(part2=False):
        for s in seats.values():
            if part2:
                s.update_p2()
            else:
                s.update_p1()
        for s in seats.values():
            s.commit()

    for seat in seats.values():
        seat.reset()

    prev_count = [seat.filled for seat in seats.values()].count(True)
    update(part2=part2)
    new_count = [seat.filled for seat in seats.values()].count(True)
    while prev_count != new_count:
        prev_count = new_count
        update(part2=part2)
        new_count = [seat.filled for seat in seats.values()].count(True)
    return prev_count


seats = {}
for j, line in enumerate(open('../inputs/day11.txt')):
    for i, char in enumerate(line):
        if char == 'L':
            seats[complex(i, j)] = Seat()

max_real = max([int(location.real) for location in seats.keys()])
max_imag = max([int(location.imag) for location in seats.keys()])
handled_locations = set()
for location, seat in seats.items():
    for loc in [1j, 1+1j, 1, -1j, -1-1j, -1, 1-1j, -1+1j]:
        adj_loc = location + loc
        if adj_loc in handled_locations:
            continue
        if any([adj_loc.real < 0, adj_loc.real > max_real, adj_loc.imag < 0, adj_loc.imag > max_imag]):
            continue
        if adj_loc in seats.keys():
            seats[adj_loc].adjacent_seats.add(seat)
            seat.adjacent_seats.add(seats[adj_loc])
        for i in range(1, max([max_real, max_imag])):
            los_loc = location + loc*i
            if any([los_loc.real < 0, los_loc.real > max_real, los_loc.imag < 0, los_loc.imag > max_imag]):
                break
            if los_loc in seats.keys():
                seat.line_of_sight_seats.add(seats[los_loc])
                seats[los_loc].line_of_sight_seats.add(seat)
                break
    handled_locations.add(location)

print(f"Part 1 Answer: {go()}")
print(f"Part 2 Answer: {go(part2=True)}")
