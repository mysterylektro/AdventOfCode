def nop(v, a, i):
    i += 1
    return a, i


def jmp(v, a, i):
    i += v
    return a, i


def acc(v, a, i):
    a += v
    i += 1
    return a, i

def replace_nop_jmp(line_list, i):
    indices = [i for i, l in enumerate(line_list) if 'nop' in l or 'jmp' in l]
    l = line_list[indices[i]]
    if 'nop' in l:
        l = l.replace('nop', 'jmp')
    else:
        l = l.replace('jmp', 'nop')
    line_list[indices[i]] = l
    return line_list


funcs = {'nop': nop,
         'jmp': jmp,
         'acc': acc}

lines = open('../inputs/day8.txt').readlines()

part1, part2, replace_index, first_run = 0, 0, 0, True
check, accumulator, idx, visited = lines.copy(), 0, 0, set()

while idx != len(check):
    while idx != len(check):
        if idx in visited:
            if first_run:
                part1 = accumulator
                first_run = False
            break
        visited.add(idx)
        op, val = check[idx].strip().split()
        f = funcs.get(op)
        accumulator, idx = f(int(val), accumulator, idx)
    if idx != len(check):
        check, accumulator, idx, visited = lines.copy(), 0, 0, set()
        check = replace_nop_jmp(check, replace_index)
        replace_index += 1
    else:
        part2 = accumulator
        break

print(f"Part 1 Answer: {part1}")
print(f"Part 2 Answer: {part2}")
