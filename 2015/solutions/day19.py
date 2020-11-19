from random import shuffle


def nth_replace(string: str, old, new, n):
    f_ind = string.find(old)
    if f_ind == -1:
        return string
    # loop util we find the nth or we find no match
    num_found = 1
    while f_ind != -1 and num_found != n:
        # f_ind + 1 means we start searching from after the last match
        f_ind = string.find(old, f_ind + 1)
        num_found += 1
    # If i is equal to n we found nth match so replace
    if num_found == n:
        return string[:f_ind] + new + string[f_ind + len(old):]
    return string


with open('../inputs/day19.txt') as f:
    lines = f.readlines()

string_map = {}
med = ''
med_next = False
for line in lines:
    line = line.strip()
    if line == '':
        med_next = True
        continue
    if med_next:
        med = line
        continue

    key, value = line.split(' => ')
    val_list = string_map.get(key, [])
    val_list.append(value)
    string_map[key] = val_list

molecules = set()

for key, value_list in string_map.items():
    f_ind = med.find(key)
    while f_ind != -1:
        for val in value_list:
            molecules.add(med[:f_ind] + val + med[f_ind + len(key):])
        f_ind = med.find(key, f_ind + 1)

print(f"Part 1 Answer: {len(molecules)}")

all_maps = []
for key, val_list in string_map.items():
    for val in val_list:
        all_maps.append((key, val))

# Part 2 - Reverse Engineer.
count = 0
molecule = med
while len(molecule) > 1:
    start = molecule
    for key, val in all_maps:
        while val in molecule:
            count += molecule.count(val)
            molecule = molecule.replace(val, key)

    # Check if we found it, if not, randomize the list and try again.
    if start == molecule:
        shuffle(all_maps)
        molecule = med
        count = 0

print(f"Part 2 Answer: {count}")
