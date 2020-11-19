def nice_string_p1(string: str) -> bool:

    def has_three_vowels(string: str) -> bool:
        num_vowels = sum([string.count('a'),
                          string.count('e'),
                          string.count('i'),
                          string.count('o'),
                          string.count('u')])
        if num_vowels < 3:
            return False
        else:
            return True

    def has_matching_pair(string: str) -> bool:
        str_set = set(string)
        valid = False
        for char in str_set:
            if char + char in string:
                valid = True
                break
        return valid

    def invalid(string: str) -> bool:
        return any(['ab' in string,
                    'cd' in string,
                    'pq' in string,
                    'xy' in string])

    return has_three_vowels(string) and has_matching_pair(string) and not invalid(string)


def nice_string_p2(string: str) -> bool:

    def pair_without_overlapping(string: str) -> bool:
        str_set = set(string)
        valid = False
        for char1 in str_set:
            for char2 in str_set:
                pair = char1 + char2
                if string.count(pair) < 2:
                    continue
                if char1 == char2:
                    # check overlap
                    if char1 + char1 + char1 in string:
                        valid = False
                    else:
                        valid = True
                        break
                else:
                    valid = True
                    break

        return valid

    def one_letter_separates(string: str) -> bool:
        str_set = set(string)
        valid = False
        for char in string:
            if string.count(char) < 2:
                continue
            for sub_char in str_set:
                if char + sub_char + char in string:
                    valid = True
                    break
            if valid:
                break
        return valid

    return pair_without_overlapping(string) and one_letter_separates(string)


with open('../inputs/day5.txt') as f:
    lines = f.readlines()

num_nice = [nice_string_p1(line) for line in lines].count(True)
print(f"Part 1 Answer: {num_nice}")

num_nice = [nice_string_p2(line) for line in lines].count(True)
print(f"Part 2 Answer: {num_nice}")
