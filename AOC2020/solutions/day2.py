def parse_line(line: str):
    tokens = line.split()
    arg1, arg2 = tuple(map(int, tokens[0].split('-')))
    arg3, arg4 = tokens[1][0], tokens[2]
    return arg1, arg2, arg3, arg4


def valid_part_one(lower_bound, upper_bound, letter, password):
    return lower_bound <= password.count(letter) <= upper_bound


def valid_part_two(pos1, pos2, letter, password):
    return (password[pos1-1] == letter) != (password[pos2-1] == letter)


count1, count2 = 0, 0
with open('../inputs/day2.txt') as f:
    for line in f:
        args = parse_line(line)
        count1 += 1 if valid_part_one(*args) else 0
        count2 += 1 if valid_part_two(*args) else 0

print(f"Part 1 Answer: {count1}")
print(f"Part 2 Answer: {count2}")
