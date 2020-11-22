with open('../inputs/day1.txt') as f:
    line = f.readline()
answer = line.count('(') - line.count(')')
print(f"Part 1 Answer: {answer}")

floor = 0
idx = 0
for idx, char in enumerate(line):
    floor += (1 if char == '(' else -1)
    if floor == -1:
        break

print(f"Part 2 Answer: {idx+1}")
