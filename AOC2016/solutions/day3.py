def is_valid(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return True
    return False


with open('../inputs/day3.txt') as f:
    lines = f.readlines()

count = 0
count2 = 0
for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
    for i in range(3):
        x, y, z = tuple(map(int, [l1.strip().split()[i], l2.strip().split()[i], l3.strip().split()[i]]))
        count2 += 1 if is_valid(x, y, z) else 0

for line in lines:
    count += 1 if is_valid(*tuple(map(int, line.strip().split()))) else 0

print(f"Part 1 Answer: {count}")
print(f"Part 2 Answer: {count2}")
