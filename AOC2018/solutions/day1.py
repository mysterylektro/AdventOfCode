a, p2, f, nums = 0, None, set(), list(map(int, [line.strip() for line in open('../inputs/day1.txt')]))
p1 = sum(nums)
while p2 is None:
    for num in nums:
        a += num
        if a in f:
            p2 = a
            break
        f.add(a)

print(f"Part 1: {p1}\nPart 2: {p2}")

