def inc(r):
    return int(r+1)


def halve(r):
    return int(r/2)


def triple(r):
    return int(r*3)


def jump(i, amount):
    return i + amount


def jump_if_even(i, register, amount):
    return i + amount if register % 2 == 0 else i + 1


def jump_if_one(i, register, amount):
    return i + amount if register == 1 else i + 1


funcs = {'hlf': halve,
         'tpl': triple,
         'inc': inc,
         'jmp': jump,
         'jie': jump_if_even,
         'jio': jump_if_one}


def run_computer(a, b):

    with open('../inputs/day23.txt') as f:
        lines = f.readlines()

    index = 0
    while True:
        try:
            line = lines[index]
        except IndexError:
            break

        register = line[4:5]
        f = funcs.get(line[:3], None)

        if f is None:
            raise ValueError()
        if f in [jump_if_even, jump_if_one]:
            amount = int(line[6:].strip())
            if register == 'a':
                index = f(index, a, amount)
            else:
                index = f(index, b, amount)
        elif f is jump:
            amount = int(line[3:].strip())
            index = f(index, amount)
        else:
            if register == 'a':
                a = f(a)
            else:
                b = f(b)
            index += 1

    return b


reg_b = run_computer(0, 0)
print(f"Part 1 Answer: {reg_b}")

reg_b = run_computer(1, 0)
print(f"Part 2 Answer: {reg_b}")
