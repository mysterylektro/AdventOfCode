groups, group = [], []
for line in [line.strip() for line in open('../inputs/day6.txt')] + ['']:
    groups, group = (groups + [group], []) if line == '' else (groups, group + [{*line}])
print(f"Part 1 Answer: {sum([len(set.union(*g)) for g in groups])}\nPart 2 Answer: {sum([len(set.intersection(*g)) for g in groups])}")