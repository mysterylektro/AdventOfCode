"""
    -*- coding: utf-8 -*-
    Time    : 2021-12-01 11:42 a.m.
    Author  : Kevin Dunphy
    E-mail  : kevin.dunphy1989@gmail.com
    FileName: setup_solutions.py
    
    {Description}
    -------------
    
"""
import os
OUTPUT_DIR = './solutions/'

for i in range(1, 26):
    filename = OUTPUT_DIR + f'day{i:02d}.py'
    if not os.path.exists(filename):
        with open(filename, 'w+') as f:
            f.write('import setup_aoc_session\n')
            f.write('from aocd.models import Puzzle\n')
            f.write('from aocd import submit\n\n')
            f.write(f'YEAR, DAY = 2021, {i}\n')
            f.write(f'puzzle = Puzzle(year=YEAR, day=DAY)\n\n# ---------- SOLUTION HERE ---------- #\n\n\n\n'
                    f'# ----------------------------------- #\n\n')
            f.write(f'submit(P1_ANSWER, part="a", year=YEAR, day=DAY)\n')
            f.write(f'# submit(P2_ANSWER, part="b", year=YEAR, day=DAY)\n')
