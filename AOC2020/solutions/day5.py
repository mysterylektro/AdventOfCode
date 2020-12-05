seat_ids = [int(line.translate(line.maketrans('FBLR', '0101')).strip(), 2) for line in open('../inputs/day5.txt')]
my_seat = [seat for seat in list(range(min(seat_ids), max(seat_ids))) if seat not in seat_ids][0]
print(f"Part 1 Answer: {max(seat_ids)}\nPart 2 Answer: {my_seat}")
