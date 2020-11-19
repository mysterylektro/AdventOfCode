from typing import Tuple


def calculate_presents(instructions: str, m: set) -> set:
    x = 0
    y = 0

    m.add((x, y))

    for char in instructions:
        if char == '>':
            x += 1
        elif char == '<':
            x -= 1
        elif char == '^':
            y += 1
        elif char == 'v':
            y -= 1
        else:
            continue
        m.add((x, y))

    return m


def split_instructions(instructions: str) -> Tuple[str, str]:
    s_instructions = ''.join([line[i * 2] for i in range(int(len(instructions) / 2))])
    r_instructions = ''.join([line[i * 2 + 1] for i in range(int(len(instructions) / 2))])
    # Handle odd number of instructions case
    if s_instructions[-1] != instructions[-1]:
        s_instructions += (instructions[-1])
    return s_instructions, r_instructions


with open('../inputs/day3.txt') as f:
    line = f.readline()

houses = calculate_presents(line, set())
print(f"Part 1 Answer: {len(houses)}")

santa_instructions, robot_instructions = split_instructions(line)
houses = calculate_presents(santa_instructions, set())
houses = calculate_presents(robot_instructions, houses)
print(f"Part 2 Answer: {len(houses)}")
