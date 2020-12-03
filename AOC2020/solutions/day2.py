import re


def valid_one(lower, upper, letter, password):
    return int(lower) <= password.count(letter) <= int(upper)


def valid_two(p1, p2, letter, password):
    return (password[int(p1) - 1] == letter) != (password[int(p2) - 1] == letter)


count1, count2 = 0, 0
with open('../inputs/day2.txt') as f:
    for line in f:
        args = re.split('-|: | ', line.strip())
        count1 += 1 if valid_one(*args) else 0
        count2 += 1 if valid_two(*args) else 0
print(f"Part 1 Answer: {count1}\nPart 2 Answer: {count2}")
