from collections import deque

facing = deque('ESWN')

steps = {'N': (0, 1),
         'E': (1, 0),
         'S': (0, -1),
         'W': (-1, 0)}

ccw_rotate = {90: lambda x, y: (-y, x),
              180: lambda x, y: (-x, -y),
              270: lambda x, y: (y, -x)}

cw_rotate = {90: lambda x, y: (y, -x),
             180: lambda x, y: (-x, -y),
             270: lambda x, y: (-y, x)}

x1, y1, x2, y2 = 0, 0, 0, 0
waypoint = [10, 1]

for line in open('../inputs/day12.txt'):
    op, arg = line[0], int(line[1:].strip())
    if op == 'L':
        facing.rotate(int(arg / 90))
        waypoint[0], waypoint[1] = ccw_rotate.get(arg)(waypoint[0], waypoint[1])
    if op == 'R':
        facing.rotate(-int(arg / 90))
        waypoint[0], waypoint[1] = cw_rotate.get(arg)(waypoint[0], waypoint[1])
    if op == 'F':
        dir = steps.get(facing[0])
        x1, y1 = x1 + dir[0] * arg, y1 + dir[1] * arg
        x2, y2 = x2 + waypoint[0] * arg, y2 + waypoint[1] * arg
    if op in facing:
        dir = steps.get(op)
        x1, y1 = x1 + dir[0] * arg, y1 + dir[1] * arg
        waypoint[0], waypoint[1] = waypoint[0] + dir[0] * arg, waypoint[1] + dir[1] * arg

print(abs(x1) + abs(y1))
print(abs(x2) + abs(y2))
