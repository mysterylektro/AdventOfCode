"""
    -*- coding: utf-8 -*-
    Time    : 2021-11-01 9:59 a.m.
    Author  : Kevin Dunphy
    E-mail  : kevin.dunphy1989@gmail.com
    FileName: day5.py
    
    {Description}
    -------------
    
"""

from hashlib import md5, sha256


def part1(input_value):
    count = 0
    password = ''
    while len(password) < 8:
        h = md5((input_value + str(count)).encode())
        if h.hexdigest().startswith('00000'):
            password += h.hexdigest()[5]
        count += 1
    print(f'Part 1: {password}')


def part2(input_value):
    count = 0
    password = ['' for _ in range(8)]
    while '' in password:
        h = md5((input_value + str(count)).encode())
        if h.hexdigest().startswith('00000'):
            idx = h.hexdigest()[5]
            if idx.isnumeric():
                if int(idx) < 8:
                    if password[int(idx)] == '':
                        password[int(idx)] = h.hexdigest()[6]
        count += 1
    print(f"Part 2: {''.join(password)}")


if __name__ == '__main__':
    input_val = 'ojvtpuvg'
    part1(input_val)
    part2(input_val)
