def bootcode(lines):
    acc, idx, seen = 0, 0, set()
    while True:
        if idx in seen:
            return False, acc
        l = lines[idx].strip().split()
        op, arg = l[0], int(l[1])
        seen.add(idx)
        acc += arg if op == 'acc' else 0
        idx += arg if op == 'jmp' else 1
        if idx >= len(lines):
            return True, acc


lines = open('../inputs/day8.txt').readlines()
print(f"Part 1 Answer: {bootcode(lines)[1]}")
for i, l in enumerate(lines):
    if 'acc' in l:
        continue
    lines[i] = 'jmp' + l[3:] if 'nop' in l else 'nop' + l[3:]
    success, val = bootcode(lines)
    if success:
        print(f"Part 2 Answer: {val}")
        break
    else:
        lines[i] = l
