alphabet = 'abcdefghijklmnopqrstuvwxyz'


def increment_letter(char: str):
    index = alphabet.index(char) + 1
    if index == len(alphabet):
        index = 0
    if index in [alphabet.index('i'), alphabet.index('o'), alphabet.index('l')]:
        index += 1
    return alphabet[index]


def increment_password(password: str):
    idx = 7
    password = password[:idx] + increment_letter(password[idx]) + password[idx+1:]
    while password[idx] == 'a':
        idx -= 1
        if idx == -1:
            idx = 7
        password = password[:idx] + increment_letter(password[idx]) + password[idx+1:]
    return password


def check_password(password):

    def invalid(password: str) -> bool:
        if any(['i' in password,
                'o' in password,
                'l' in password]):
            return True
        else:
            return False

    def contains_two_pairs(password: str) -> bool:
        count = 0
        for char in alphabet:
            if char + char in password:
                count += 1
            if count == 2:
                return True

        return False

    def increasing_straight(password: str) -> bool:
        for i in range(len(alphabet)-2):
            if alphabet[i:i+3] in password:
                return True

        return False

    return not invalid(password) and increasing_straight(password) and contains_two_pairs(password)


input_val = 'hxbxwxba'

while not check_password(input_val):
    input_val = increment_password(input_val)

print(f"Part 1 Answer: {input_val}")

input_val = increment_password(input_val)
while not check_password(input_val):
    input_val = increment_password(input_val)

print(f"Part 2 Answer: {input_val}")