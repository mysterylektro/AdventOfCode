total = sum(len(line.strip()) - len(eval(line.strip())) for line in open('../inputs/day8.txt'))

print(f"Part 1 Answer: {total}")

total = sum(2 + line.count('\\') + line.count('"') for line in open('../inputs/day8.txt'))

print(f"Part 2 Answer: {total}")


