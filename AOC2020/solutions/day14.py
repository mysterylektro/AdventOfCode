import itertools


def apply_mask(mask: str, integer: int):
    int_list = list(bin(integer)[2:].zfill(36))
    for i, j in enumerate(int_list):
        if mask[i] != 'X':
            int_list[i] = mask[i]
    return int(''.join(int_list), 2)


def get_address_list(mask: str, address: int):
    address = bin(address)[2:].zfill(36)
    address_list = []
    floaters = []
    base = dict()
    for i, bit in enumerate(mask):
        if bit == 'X':
            floaters.append(i)
        elif bit == '1':
            base[i] = '1'
        else:
            base[i] = address[i]
    floating_vals = itertools.product([0, 1], repeat=len(floaters))
    for floating_val in floating_vals:
        iter_address = base.copy()
        for i, k in enumerate(floaters):
            iter_address[k] = str(floating_val[i])
        string = ''.join([j for i, j in sorted(zip(iter_address.keys(), iter_address.values()))])
        address_list.append(int(string, 2))

    return address_list


mem1 = dict()
mem2 = dict()
mask = ''
for line in open('../inputs/day14.txt'):
    op, arg = line.strip().split(' = ')
    if op == 'mask':
        mask = arg
        continue
    address, arg = int(op[4:-1]), int(arg)
    mem1[address] = apply_mask(mask, arg)
    for address in get_address_list(mask, address):
        mem2[address] = arg

print(f"Part 1 Answer: {sum(mem1.values())}")
print(f"Part 2 Answer: {sum(mem2.values())}")
