import itertools

with open('../inputs/day17.txt') as f:
    lines = f.readlines()

containers = []
for line in lines:
    containers.append(int(line.strip()))

containers.sort()

total_litres = 150

idx = 0
min_containers = None
max_containers = None

while min_containers is None or max_containers is None:
    if sum(containers[:idx]) >= total_litres and max_containers is None:
        max_containers = idx + 1
    if sum(containers[-idx-1:]) >= total_litres and min_containers is None:
        min_containers = idx + 1

    idx += 1

total_num_combos = 0
total_min_container_combos = 0

for i in range(min_containers, max_containers):
    combos = itertools.combinations(containers, i)
    for combo in combos:
        if sum(combo) == total_litres:
            total_num_combos += 1
            if i == min_containers:
                total_min_container_combos += 1

print(f"Part 1 Answer: {total_num_combos}")
print(f"Part 2 Answer: {total_min_container_combos}")
