lines = [line.strip() for line in open('../inputs/day5.txt')]
seat_ids = [int(line[:7].replace('F', '0').replace('B', '1'), 2) * 8 + int(line[7:].replace('L', '0').replace('R', '1'), 2) for line in lines]
my_seat = [seat for seat in list(range(min(seat_ids), max(seat_ids))) if seat not in seat_ids][0]
print(f"Part 1 Answer: {max(seat_ids)}\nPart 2 Answer: {my_seat}")
