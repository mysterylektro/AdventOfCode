import itertools

lines = list(map(int, open('../inputs/day9.txt')))

part1, part2 = 0, 0
for idx, num in enumerate(lines):
    if idx < 25:
        continue
    sums = [sum(combo) for combo in itertools.combinations(lines[idx-25:idx], 2)]
    if num in sums:
        continue
    else:
        part1 = num
        break

print(f"Part 1 Answer: {part1}")

for i in range(2, len(lines)):
    combos = [lines[k:k+i] for k in range(0, len(lines))]
    if part1 in [sum(combo) for combo in combos]:
        sequence = combos[[sum(combo) for combo in combos].index(part1)]
        part2 = min(sequence) + max(sequence)
        break

print(f"Part 2 Answer: {part2}")
