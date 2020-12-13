class Seat:
    def __init__(self, row, col):
        self.location = (row, col)
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


seats = [Seat(j, i) for j, line in enumerate(open('../inputs/day11.txt')) for i, char in enumerate(line) if char == 'L']
locations = [seat.location for seat in seats]
max_row = max([loc[0] for loc in locations])
max_col = max([loc[1] for loc in locations])
for seat in seats:
    for loc in [(0, 1), (1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (1, -1), (-1, 1)]:
        adj_loc = seat.location[0] + loc[0], seat.location[1] + loc[1]
        if 0 <= adj_loc[0] <= max_row and 0 <= adj_loc[1] <= max_col:
            if adj_loc in locations:
                seat.adjacent_seats.append(seats[locations.index(adj_loc)])
        for i in range(1, max(max_row, max_col)):
            los_loc = seat.location[0] + loc[0]*i, seat.location[1] + loc[1]*i
            if 0 <= los_loc[0] <= max_row and 0 <= los_loc[1] <= max_col:
                if los_loc in locations:
                    seat.line_of_sight_seats.append(seats[locations.index(los_loc)])
                    break
            else:
                break

print(f"Part 1 Answer: {go()}")
print(f"Part 2 Answer: {go(part2=True)}")
