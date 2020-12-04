import string


def valid_hgt(hgt):
    if hgt[-2:] == 'cm':
        return 150 <= int(hgt[:-2]) <= 193
    elif hgt[-2:] == 'in':
        return 59 <= int(hgt[:-2]) <= 76
    else:
        return False


options = {'byr': lambda byr: 1920 <= int(byr) <= 2002,
           'iyr': lambda iyr: 2010 <= int(iyr) <= 2020,
           'eyr': lambda eyr: 2020 <= int(eyr) <= 2030,
           'hgt': valid_hgt,
           'hcl': lambda hcl: hcl[0] == '#' and len(hcl[1:]) == 6 and all([h in string.hexdigits for h in hcl[1:]]),
           'ecl': lambda ecl: ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
           'pid': lambda pid: len(pid) == 9 and all([i in string.digits for i in pid])}


def valid_pp_part1(passport):
    return all([k in passport for k in options])


def valid_pp_part2(passport):
    return all([func(passport[k]) for k, func in options.items() if k in passport])


part1, part2 = 0, 0
lines = [line.strip() for line in open('../inputs/day4.txt')]

pp = {}
for line in lines:
    if line == '':
        p1, p2 = valid_pp_part1(pp), valid_pp_part2(pp)
        part1 += 1 if p1 else 0
        part2 += 1 if p1 and p2 else 0
        pp = {}
        continue
    tokens = line.split()
    for token in tokens:
        key, value = token.split(':')
        pp[key] = value

if pp != {}:
    p1, p2 = valid_pp_part1(pp), valid_pp_part2(pp)
    part1 += 1 if p1 else 0
    part2 += 1 if p1 and p2 else 0

print(f"Part 1 Answer: {part1}")
print(f"Part 2 Answer: {part2}")
