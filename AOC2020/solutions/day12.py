from collections import deque

facing = deque('ESWN')
steps = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
p1, p2 = 0, 0
waypoint = 10+1j

for line in open('../inputs/day12.txt'):
    op, arg = line[0], int(line[1:].strip())
    val = arg // 90
    if op == 'L':
        facing.rotate(val)
        for _ in range(val):
            waypoint = complex(-waypoint.imag, waypoint.real)
    elif op == 'R':
        facing.rotate(-val)
        for _ in range(val):
            waypoint = complex(waypoint.imag, -waypoint.real)
    elif op == 'F':
        step = steps.get(facing[0])
        p1 += step * arg
        p2 += waypoint * arg
    elif op in facing:
        step = steps.get(op)
        p1 += step * arg
        waypoint += step * arg
    else:
        continue

print(f"Part 1 Answer: {int(abs(p1.real) + abs(p1.imag))}")
print(f"Part 2 Answer: {int(abs(p2.real) + abs(p2.imag))}")
