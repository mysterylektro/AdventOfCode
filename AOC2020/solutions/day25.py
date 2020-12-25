val, key, subject_number = 1, 1, 7
card_public, door_public = list(map(int, [line.strip() for line in open('../inputs/day25.txt')]))
while val != card_public:
    val, key = (val * subject_number) % 20201227, (key * door_public) % 20201227
print(f"Part 1 Answer: {key}")
