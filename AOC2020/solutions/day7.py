import re
bags = {}


def can_contain_shiny_gold(bag, bag_dict):
    return False if len(bag_dict[bag]) == 0 else True if 'shiny gold' in [b for b, c in bag_dict[bag]] else any([can_contain_shiny_gold(b, bag_dict) for b, c in bag_dict[bag]])


def bag_sum(bag, bag_dict):
    return 0 if len(bag_dict[bag]) == 0 else sum([c + c*bag_sum(b, bag_dict) for b, c in bag_dict[bag]])


for line in open('../inputs/day7.txt'):
    bag_color, contains = line.replace('.', ' ').strip().split(' bags contain ')[0], [] if 'no' in line.replace('.', ' ').strip().split(' bags contain ')[1] else [(' '.join(other_bags.split(' ')[1:]), int(other_bags.split(' ')[0])) for other_bags in re.split(' bag, | bags, | bag| bags', line.replace('.', ' ').strip().split(' bags contain ')[1])[:-1]]
    bags[bag_color] = contains

print(f"Part 1 Answer: {sum([1 if can_contain_shiny_gold(bag, bags) else 0 for bag in bags])}")
print(f"Part 2 Answer: {bag_sum('shiny gold', bags)}")
