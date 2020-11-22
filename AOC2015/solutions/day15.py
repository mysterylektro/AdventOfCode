import numpy

with open('../inputs/day15.txt') as f:
    lines = f.readlines()

ingredients = {}
for line in lines:
    ingredient, params = line.split(': ')
    parameters = params.split(', ')
    param_dict = {}
    for p in parameters:
        parameter, amount = p.split(' ')
        param_dict[parameter] = int(amount)
    ingredients[ingredient] = param_dict

max_range = 100

ingredient_list = ingredients.keys()
param_list = list(list(ingredients.values())[0].keys())

best_score = 0
best_calorie_score = 0

for w in range(0, max_range + 1):
    for x in range(0, max_range + 1 - w):
        for y in range(0, max_range + 1 - w - x):
            z = max_range - w - x - y
            totals = {}
            for ingredient, amount in zip(ingredient_list, [w, x, y, z]):
                for param in param_list:
                    totals[param] = totals.get(param, 0) + amount * ingredients[ingredient][param]

            scores = [totals[key] for key in totals if key != 'calories']
            scores = [score if score > 0 else 0 for score in scores]
            score = numpy.prod(scores)
            if totals['calories'] == 500:
                best_calorie_score = max([best_calorie_score, score])
            best_score = max([best_score, score])


print(f"Part 1 Answer: {best_score}")
print(f"Part 2 Answer: {best_calorie_score}")
