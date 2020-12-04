import string


def valid_byr(byr):
    return True if 1920 <= int(byr) <= 2002 else False


def valid_iyr(iyr):
    return True if 2010 <= int(iyr) <= 2020 else False


def valid_eyr(eyr):
    return True if 2020 <= int(eyr) <= 2030 else False


def valid_hgt(hgt):
    units = hgt[-2:]
    if units == 'cm':
        return True if 150 <= int(hgt[:-2]) <= 193 else False
    elif units == 'in':
        return True if 59 <= int(hgt[:-2]) <= 76 else False
    else:
        return False


def valid_hcl(hcl):
    if hcl[0] == '#':
        return True if len(hcl[1:]) == 6 and all([h in string.hexdigits for h in hcl[1:]]) else False
    else:
        return False


def valid_ecl(ecl):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in colors


def valid_pid(pid):
    return len(pid) == 9 and all([i in string.digits for i in pid])


options = {'byr': valid_byr,
           'iyr': valid_iyr,
           'eyr': valid_eyr,
           'hgt': valid_hgt,
           'hcl': valid_hcl,
           'ecl': valid_ecl,
           'pid': valid_pid}


def valid_pp_part1(passport):
    for k in options:
        if k not in passport:
            return False
    return True


def valid_pp_part2(passport):

    valid = valid_pp_part1(passport)
    for k in options:
        func = options.get(k)
        valid = valid and func(passport[k])
        if not valid:
            return False
    return valid


def parse_passports(input_file):
    lines = [line.strip() for line in open(input_file)]

    passports = []
    pp = {}
    for line in lines:
        if line == '':
            passports.append(pp)
            pp = {}
            continue
        tokens = line.split()
        for token in tokens:
            key, value = token.split(':')
            pp[key] = value
    if pp != {}:
        passports.append(pp)
    return passports


all_passports = parse_passports('../inputs/day4.txt')
p1_valid_passports = [pp for pp in all_passports if valid_pp_part1(pp)]
print(f"Part 1 Answer: {len(p1_valid_passports)}")
p2_valid_passports = [pp for pp in p1_valid_passports if valid_pp_part2(pp)]
print(f"Part 2 Answer: {len(p2_valid_passports)}")
