from functools import reduce


def factors(n):
    return list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))


target_presents = 33100000

# Guess it starts at least 1/50 the value:
i = int(target_presents/50)
part1, part2 = None, None
while part1 is None or part2 is None:
    i += 1
    factor_list = factors(i)
    if part1 is None:
        if 10*sum(factors(i)) > target_presents:
            part1 = i

    if part2 is None:
        if 11 * sum([factor for factor in factor_list if i / factor <= 50]) >= target_presents:
            part2 = i

print(f"Part 1 Answer: {part1}")
print(f"Part 2 Answer: {part2}")

