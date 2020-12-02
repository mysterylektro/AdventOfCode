count1, count2 = 0, 0
with open('../inputs/day2.txt') as f:
    for line in f:
        args = *tuple(map(int, line.split()[0].split('-'))), line.split()[1][0], line.split()[2]
        count1 += 1 if args[0] <= args[3].count(args[2]) <= args[1] else 0
        count2 += 1 if (args[3][args[0]-1] == args[2]) != (args[3][args[1]-1] == args[2]) else 0
print(f"Part 1 Answer: {count1}\nPart 2 Answer: {count2}")
