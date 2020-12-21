import re

allergen_list = dict()
food_set = set()
food_list = []

for line in [line.strip() for line in open('../inputs/day21.txt')]:
    ingredients, allergens = line.split(' (contains ')
    foods = ingredients.split()
    food_set = set.union(food_set, set(foods))
    food_list.extend(foods)
    allergens = re.split(r', | |\)', allergens)[:-1]
    for allergen in allergens:
        allergen_list[allergen] = set.intersection(allergen_list[allergen], set(foods)) if allergen in allergen_list else set(foods)

while sum([len(c) for c in allergen_list.values()]) != len(allergen_list):
    # find sets that contain only a single value, and remove that value from other sets:
    single_val_sets = [s for s in allergen_list.values() if len(s) == 1]
    for s in single_val_sets:
        val = list(s)[0]
        for allergen, candidates in allergen_list.items():
            if val in candidates and len(candidates) != 1:
                candidates.remove(val)

safe_foods = set.union(*allergen_list.values()) ^ food_set
count = sum([food_list.count(food) for food in safe_foods])
print(f'Part 1 Answer: {count}')

allergen_foods = ','.join([list(allergen_list[key])[0] for key in sorted(allergen_list)])
print(f"Part 2 Answer: {allergen_foods}")
