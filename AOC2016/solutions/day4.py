"""
    -*- coding: utf-8 -*-
    Time    : 2021-11-01 9:26 a.m.
    Author  : Kevin Dunphy
    E-mail  : kevin.dunphy1989@gmail.com
    FileName: day4.py
    
    {Description}
    -------------
    
"""

from collections import Counter
from string import ascii_lowercase


def decrypt(line, id):
    trans_table = ''.maketrans(ascii_lowercase, ''.join([ascii_lowercase[idx] for idx in [(i + id) % 26 for i in range(26)]]))
    return ' '.join([t.translate(trans_table) for t in line.strip().split('-')[:-1]])


def parse_line(line):
    tokens = line.strip().split('-')
    counter = Counter(''.join(tokens[:-1]))
    id, key = tokens[-1].split('[')
    id, key = int(id), key[:-1]

    values = set(counter.values())

    valid = True
    for k in key:
        v = counter[k]
        if v == max(values):
            max_keys = [i for i in counter if counter[i] == v]
            if k != min(max_keys):
                valid = False
                break
            else:
                counter.pop(k)
                values = set(counter.values())
        else:
            valid = False
            break

    if valid:
        message = decrypt(line, id)
    else:
        id, message = 0, ''

    return id, message


if __name__ == '__main__':
    with open('../inputs/day4.txt') as f:
        lines = f.readlines()

    part1 = 0
    part2 = 0
    for line in lines:
        id, message = parse_line(line)
        part1 += id
        if id != 0:
            if 'north' in message:
                part2 = id

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
