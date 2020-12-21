from collections import defaultdict
import re

allergen_list = defaultdict(list)
food_list = set()
appearances = []

for line in [line.strip() for line in open('../inputs/day21.txt')]:
    tokens = line.split(' (contains ')
    foods = tokens[0].split()
    allergens = re.split(r', | |\)', tokens[1])
    allergens[-1] = allergens[-1][:-1]
    food_list = food_list.union(set(foods))
    appearances.extend(foods)
    for allergen in allergens:
        if allergen == '':
            continue
        allergen_list[allergen].append(set(foods))


for allergen, candidates in allergen_list.items():
    allergen_list[allergen] = set.intersection(*candidates)

while sum([len(c) for c in allergen_list.values()]) != len(allergen_list):
    # find sets that contain only a single value, and remove that value from other sets:
    single_val_sets = [s for s in allergen_list.values() if len(s) == 1]
    for s in single_val_sets:
        val = list(s)[0]
        for allergen, candidates in allergen_list.items():
            if val in candidates and len(candidates) != 1:
                candidates.remove(val)

allergen_foods = set.union(*allergen_list.values())
safe_foods = allergen_foods ^ food_list
count = 0
for food in safe_foods:
    count += appearances.count(food)

print(f'Part 1 Answer: {count}')

allergens = [list(allergen_list[key])[0] for key in sorted(allergen_list)]
print(f"Part 2 Answer: {','.join(allergens)}")
