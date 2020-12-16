from collections import defaultdict, deque


def memory_game(end_num):
    spoken = defaultdict(deque)

    for i, j in enumerate(list(map(int, open('../inputs/day15.txt').readline().split(',')))):
        spoken[j].append(i+1)

    last_turn, last_spoken = i+1, j
    for turn in range(last_turn+1, end_num+1):
        last_spoken = 0 if len(spoken[last_spoken]) <= 1 else spoken[last_spoken][1] - spoken[last_spoken][0]
        spoken[last_spoken].append(turn)
        if len(spoken[last_spoken]) > 2:
            spoken[last_spoken].popleft()

    return last_spoken


print(f"Part 1 Answer: {memory_game(2020)}")
print(f"Part 2 Answer: {memory_game(30000000)}")

