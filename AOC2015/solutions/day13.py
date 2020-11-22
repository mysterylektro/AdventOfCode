from itertools import permutations


def calculate_max_happiness(people, weights):

    perms = list(permutations(people))
    happiness_list = []
    for idx, permutation in enumerate(perms):
        permutation = list(permutation)
        permutation.append(permutation[0])
        happiness = []
        for pair in zip(permutation[:-1], permutation[1:]):
            happiness.append(weights.get(pair) + weights.get(pair[::-1]))
        happiness_list.append(tuple(happiness))

    max_happiness = max([sum(item) for item in happiness_list])
    return max_happiness


people = set()
weights = {}

input_file = '../inputs/day13.txt'

with open(input_file) as f:
    lines = f.readlines()


for line in lines:
    line = line[:-2]
    person_1, _, direction, amount, _, _, _, _, _, _, person_2 = line.strip().split(' ')
    people.add(person_1)
    people.add(person_2)

    multiplier = -1 if direction == 'lose' else 1
    weight = int(amount) * multiplier

    weights[(person_1, person_2)] = int(weight)

max_happiness = calculate_max_happiness(people, weights)
print(f"Part 1 Answer: {max_happiness}")

people.add('Me')
for person in people:
    if person == 'Me':
        continue
    weights[('Me', person)] = int(0)
    weights[(person, 'Me')] = int(0)

max_happiness = calculate_max_happiness(people, weights)
print(f"Part 2 Answer: {max_happiness}")
