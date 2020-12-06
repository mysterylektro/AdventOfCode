def get_count(lines, part1=True):
    groups, group = [], None
    for line in lines:
        if line == '\n':
            groups.append(group)
            group = None
            continue
        if group is None:
            group = set([char for char in line.strip()])
            continue
        if part1:
            group = group.union(set([char for char in line.strip()]))
        else:
            group = group.intersection(set([char for char in line.strip()]))

    return sum([len(g) for g in groups])


lines = [line for line in open('../inputs/day6.txt')] + ['\n']
print(f"Part 1 Answer: {get_count(lines)}")
print(f"Part 2 Answer: {get_count(lines, part1=False)}")
