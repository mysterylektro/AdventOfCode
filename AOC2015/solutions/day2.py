def calculate_wrapping_paper(dimensions: str) -> float:
    l, w, h = map(float, dimensions.split('x'))
    sides = (l*w, l*h, w*h)
    return 2*sum(sides) + min(sides)


def calculate_ribbon(dimensions: str) -> float:
    l, w, h = map(float, dimensions.split('x'))
    perimeters = (2*(l+w), 2*(l+h), 2*(w+h))
    return min(perimeters) + l*w*h


with open('../inputs/day2.txt') as f:
    lines = f.readlines()

wrapping_needed = sum([calculate_wrapping_paper(line) for line in lines])
print(f"Part 1 Answer: {wrapping_needed}")

ribbon_needed = sum([calculate_ribbon(line) for line in lines])
print(f"Part 2 Answer: {ribbon_needed}")
