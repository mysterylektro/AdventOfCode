"""
    -*- coding: utf-8 -*-
    Time    : 2021-11-01 1:00 p.m.
    Author  : Kevin Dunphy
    E-mail  : kevin.dunphy1989@gmail.com
    FileName: day6.py
    
    {Description}
    -------------
    
"""

from collections import Counter


if __name__ == '__main__':
    with open('../inputs/day6.txt') as f:
        lines = f.readlines()

    p1 = ''
    p2 = ''
    for line in [''.join(s) for s in zip(*[ln.strip() for ln in lines])]:
        count = Counter(line)
        max_val = max(count.values())
        min_val = min(count.values())
        for k, v in count.items():
            if v == max_val:
                p1 += k
                break

        for k, v in count.items():
            if v == min_val:
                p2 += k
                break

    print(f'Part 1: {p1}')
    print(f'Part 2: {p2}')
