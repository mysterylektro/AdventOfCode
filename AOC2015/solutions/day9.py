import itertools

vertices = {}
weights = {}

input_file = '../inputs/day9.txt'

with open(input_file) as f:
    lines = f.readlines()


for line in lines:
    vertex_1, _, vertex_2, _, weight = line.split(' ')
    if vertex_1 not in vertices.keys():
        vertices[vertex_1] = len(vertices)

    if vertex_2 not in vertices.keys():
        vertices[vertex_2] = len(vertices)

    weights[(vertices[vertex_1], vertices[vertex_2])] = int(weight)
    weights[(vertices[vertex_2], vertices[vertex_1])] = int(weight)


places = vertices.values()
permutations = list(itertools.permutations(places))
min_weight = None
max_weight = None
for idx, permutation in enumerate(permutations):
    total_weight = 0
    for coord in zip(permutation[:-1], permutation[1:]):
        total_weight += weights.get(coord)
    if idx == 0:
        min_weight = total_weight
        max_weight = total_weight
    else:
        min_weight = min([min_weight, total_weight])
        max_weight = max([max_weight, total_weight])

print(f"Part 1 Answer: {min_weight}")
print(f"Part 2 Answer: {max_weight}")
