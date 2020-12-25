def loop(val, subject_number):
    return (val * subject_number) % 20201227


val, subject_number = 1, 7
card_public, door_public = list(map(int, [line.strip() for line in open('../inputs/day25.txt')]))

card_loop = 0
while val != card_public:
    card_loop += 1
    val = loop(val, subject_number)

encryption_key = 1
for _ in range(card_loop):
    encryption_key = loop(encryption_key, door_public)

print(f"Part 1 Answer: {encryption_key}")
