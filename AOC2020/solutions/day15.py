from collections import defaultdict
spoken = defaultdict(list)
last_turn = 0
last_spoken = 0
for i, j in enumerate(list(map(int, open('../inputs/day15.txt').readline().split(',')))):
    last_spoken, last_turn = j, i+1
    spoken[last_spoken].append(last_turn)

for turn in range(last_turn+1, 30000001):
    if len(spoken[last_spoken]) <= 1:
        to_speak = 0
    else:
        to_speak = spoken[last_spoken][-1] - spoken[last_spoken][-2]
    last_spoken = to_speak
    spoken[last_spoken].append(turn)

print(f"Turn: {turn}: {last_spoken}")





