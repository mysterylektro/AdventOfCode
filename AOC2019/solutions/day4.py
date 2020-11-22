"""
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password.
The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 402328-864247.

--- Part Two ---

An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of
matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

"""


def valid_password(val):
    digits = str(val)
    has_double = False
    current_digit = digits[0]
    for digit in digits[1:]:
        if int(digit) < int(current_digit):
            return False
        if int(digit) == int(current_digit) and has_double is False:
            has_double = True
        current_digit = digit

    return has_double


def valid_password2(val):
    digits = str(val)
    valid = False
    current_digit = digits[0]
    digit_count = 1
    previous_valid = False
    for digit in digits[1:]:
        if int(digit) < int(current_digit):
            return False
        if int(digit) == int(current_digit):
            digit_count += 1
            if digit_count == 2:
                valid = True
            else:
                valid = previous_valid
        else:
            digit_count = 1
            previous_valid = valid
        current_digit = digit

    return valid


if __name__ == '__main__':
    input_file = '../inputs/day4.txt'
    with open(input_file) as f:
        start, end = f.readline().split('-')

    start = int(start)
    end = int(end)

    count = 0
    for value in range(start, end+1):
        if valid_password(value):
            count += 1

    print("Answer for Part 1: " + str(count))

    count = 0
    for value in range(start, end + 1):
        if valid_password2(value):
            count += 1

    print("Answer for Part 2: " + str(count))
