from collections import defaultdict
import math

valid_ranges = dict()
all_valid_numbers = set()
tickets = []
my_ticket = []
with open('../inputs/day16.txt') as f:
    line = f.readline().strip()
    while line != '':
        valid_numbers = set()
        key, tokens = line.split(': ')
        tokens = tokens.split(' or ')
        start, end = tuple(map(int, tokens[0].split('-')))
        valid_numbers = valid_numbers.union(set(range(start, end+1)))
        start, end = tuple(map(int, tokens[1].split('-')))
        valid_numbers = valid_numbers.union(set(range(start, end + 1)))
        valid_ranges[key] = valid_numbers
        all_valid_numbers = all_valid_numbers.union(valid_numbers)
        line = f.readline().strip()

    # Read next lines
    while line != 'your ticket:':
        line = f.readline().strip()
    line = f.readline().strip()
    my_ticket = list(map(int, line.split(',')))
    while line != 'nearby tickets:':
        line = f.readline().strip()

    line = f.readline().strip()
    invalid_values = list()
    while line != '':
        ticket_numbers = list(map(int, line.split(',')))
        invalid = False
        for num in ticket_numbers:
            if num not in all_valid_numbers:
                invalid_values.append(num)
                invalid = True
        if not invalid:
            tickets.append(ticket_numbers)
        line = f.readline().strip()

print(f"Part 1 Answer: {sum(invalid_values)}")

positions = defaultdict(list)
for i, j in enumerate(my_ticket):
    for key, val in valid_ranges.items():
        if all([ticket[i] in val for ticket in tickets]):
            positions[i].append(key)

# find all that have len(1) and remove from other lists:
uniques = [pos[0] for pos in positions.values() if len(pos) == 1]
while len(uniques) != len(positions):
    for unique in uniques:
        for val in positions.values():
            if len(val) > 1 and unique in val:
                val.remove(unique)
    uniques = [pos[0] for pos in positions.values() if len(pos) == 1]

my_ticket_values = [my_ticket[k] for k, v in positions.items() if 'departure' in v[0]]

print(f"Part 2 Answer: {math.prod(my_ticket_values)}")
