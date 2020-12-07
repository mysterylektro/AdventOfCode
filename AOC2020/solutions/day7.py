import re
bags = {}


def can_contain_shiny_gold(bag, bag_dict):
    contain_list = bag_dict[bag]
    if len(contain_list) == 0:
        return False
    if 'shiny gold' in [b for b, c in contain_list]:
        return True

    return any([can_contain_shiny_gold(b, bag_dict) for b, c in contain_list])


def bag_sum(bag, bag_dict):
    contain_list = bag_dict[bag]
    if len(contain_list) == 0:
        return 0
    else:
        return sum([int(c) + int(c)*bag_sum(b, bag_dict) for b, c in contain_list])


for line in open('../inputs/day7.txt'):
    line = line.replace('.', ' ').strip()
    tokens = line.split(' bags contain ')
    bag_color = tokens[0]
    contains = []
    if 'no other bags' in tokens[1]:
        bags[bag_color] = []
        continue
    for other_bags in re.split(' bag, | bags, | bag| bags', tokens[1])[:-1]:
        count, colour = other_bags.split(' ')[0], ' '.join(other_bags.split(' ')[1:])
        contains.append((colour, count))

    bags[bag_color] = contains

count = 0
for bag in bags:
    count += 1 if can_contain_shiny_gold(bag, bags) else 0

print(f"Part 1 Answer: {count}")
print(f"Part 2 Answer: {bag_sum('shiny gold', bags)}")
