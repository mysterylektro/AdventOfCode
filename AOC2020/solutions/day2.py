import re


lines, count1, count2 = [line.strip() for line in open('../inputs/day2.txt')], 0, 0
for line in lines:
    args = re.split('-|: | ', line)
    count1 += 1 if int(args[0]) <= args[3].count(args[2]) <= int(args[1]) else 0
    count2 += 1 if (args[3][int(args[0]) - 1] == args[2]) != (args[3][int(args[1]) - 1] == args[2]) else 0
print(f"Part 1 Answer: {count1}\nPart 2 Answer: {count2}")
