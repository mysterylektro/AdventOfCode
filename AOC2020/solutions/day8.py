def bootcode(lines):
    acc, idx, seen = 0, 0, set()
    while True:
        if idx in seen:
            return False, acc
        l = lines[idx].strip().split()
        instruction, value = l[0], int(l[1])
        seen.add(idx)
        acc += value if instruction == 'acc' else 0
        idx += value if instruction == 'jmp' else 1
        if idx >= len(lines):
            return True, acc


lines = open('../inputs/day8.txt').readlines()
print(f"Part 1 Answer: {bootcode(lines)[1]}")
for i, l in enumerate(lines):
    if 'acc' in l:
        continue
    lines[i] = l.replace('nop', 'jmp') if 'nop' in l else l.replace('jmp', 'nop')
    success, val = bootcode(lines)
    if success:
        print(f"Part 2 Answer: {val}")
        break
    else:
        lines[i] = l
