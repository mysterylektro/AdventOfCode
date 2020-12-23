def move(current_cup):
    pickups = [cups[current_cup]]
    for _ in range(2):
        pickups.append(cups[pickups[-1]])
    destination = current_cup - 1 if current_cup > min_val else max_val
    while destination in pickups:
        destination = destination - 1 if destination > min_val else max_val
    cups[current_cup] = cups[pickups[-1]]
    cups[pickups[-1]] = cups[destination]
    cups[destination] = pickups[0]


def game(current_cup, rounds):
    for _ in range(rounds):
        move(current_cup)
        current_cup = cups[current_cup]


puzzle_input = open('../inputs/day23.txt').read().strip()

nums = list(map(int, list(puzzle_input)))
min_val, max_val = min(nums), max(nums)
cups = {key: val for key, val in zip(nums, nums[1:] + nums[:1])}
game(nums[0], 100)
cup, part1 = 1, ''
for _ in range(len(nums)-1):
    cup = cups[cup]
    part1 += str(cup)
print(f"Part 1 Answer: {part1}")

nums = list(map(int, list(puzzle_input))) + list(range(10, 1000001))
min_val, max_val = min(nums), max(nums)
cups = {key: val for key, val in zip(nums, nums[1:] + nums[:1])}
game(nums[0], 10000000)
print(f"Part 2 Answer: {cups[1] * cups[cups[1]]}")
