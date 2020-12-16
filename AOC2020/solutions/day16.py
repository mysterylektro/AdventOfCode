from collections import defaultdict
import math
import re

tickets = []
ticket_fields = dict()
ticket_positions = defaultdict(list)
invalid_values = list()

sections = open('../inputs/day16.txt').read().split('\n\n')

# Parse in first section into ticket fields dictionary.
for line in sections[0].split('\n'):
    key, s1, e1, s2, e2 = re.split(' or |-|: ', line)
    ticket_fields[key] = set.union(set(range(int(s1), int(e1) + 1)), set(range(int(s2), int(e2) + 1)))

# Parse in my ticket information
my_ticket = list(map(int, sections[1].split('\n')[1].split(',')))

# For part 1, a ticket is invalid if its number does not fit in the union of all sets of ranges.
all_valid_numbers = set.union(*ticket_fields.values())

# Parse in valid tickets, and store invalid numbers
for line in sections[2].split('\n')[1:-1]:
    ticket_numbers = list(map(int, line.split(',')))
    invalid_ticket_values = [num for num in ticket_numbers if num not in all_valid_numbers]
    if len(invalid_ticket_values) > 0:
        invalid_values.extend(invalid_ticket_values)
        continue
    tickets.append(ticket_numbers)

# Make a list of all the candidate fields each ticket position could be.
for i in range(len(my_ticket)):
    for key, val in ticket_fields.items():
        if all([ticket[i] in val for ticket in tickets]):
            ticket_positions[i].append(key)

# Find all the fields that are unique (i.e. have length of 1). These fields *must* be the correct position,
# so remove it from any other list of candidate ticket positions.
uniques = [pos[0] for pos in ticket_positions.values() if len(pos) == 1]

# Repeat this process until all ticket positions as unique.
while len(uniques) != len(ticket_positions):
    for unique in uniques:
        for val in ticket_positions.values():
            if len(val) > 1 and unique in val:
                val.remove(unique)
    uniques = [pos[0] for pos in ticket_positions.values() if len(pos) == 1]

# Get the departure value positions and pull from my ticket information
departure_values = [my_ticket[k] for k, v in ticket_positions.items() if 'departure' in v[0]]

# Part 1 is the sum of all the invalid numbers, Part 2 is the product of the departure values.
print(f"Part 1 Answer: {sum(invalid_values)}")
print(f"Part 2 Answer: {math.prod(departure_values)}")
