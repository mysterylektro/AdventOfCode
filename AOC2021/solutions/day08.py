import setup_aoc_session
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict
import timeit

YEAR, DAY = 2021, 8
puzzle = Puzzle(year=YEAR, day=DAY)

start = timeit.default_timer()
# ---------- SOLUTION HERE ---------- #

mapping = {'abcefg': '0',
           'cf': '1',
           'acdeg': '2',
           'acdfg': '3',
           'bcdf': '4',
           'abdfg': '5',
           'abdefg': '6',
           'acf': '7',
           'abcdefg': '8',
           'abcdfg': '9'}


def decode(input_segments):
    values = list(set(''.join(sorted(i)) for i in input_segments))
    counts = {letter: sum(1 for string in values if letter in string) for letter in 'abcdefg'}
    translation = defaultdict(str)
    one, four, seven, eight = None, None, None, None
    for i in input_segments:
        if len(i) == 2:
            one = i
        if len(i) == 3:
            seven = i
        if len(i) == 4:
            four = i
        if len(i) == 7:
            eight = i
        if None not in [one, four, seven, eight]:
            break

    translation['a'] = ''.join(list(set(one) ^ set(seven)))
    translation['b'] = ''.join(list(set(one) ^ set(four)))
    translation['c'] = ''.join(list(set(one)))
    translation['d'] = ''.join(list(set(one) ^ set(four)))
    translation['e'] = ''.join(list(set(eight) ^ set(four) ^ set(seven)))
    translation['f'] = ''.join(list(set(one)))
    translation['g'] = ''.join(list(set(eight) ^ set(four) ^ set(seven)))

    a, b = (0, 1) if counts.get(translation['b'][0]) == 7 else (1, 0)
    translation['d'] = translation['b'][a]
    translation['b'] = translation['b'][b]
    for i in ['e', 'g']:
        for j in ['d', 'b']:
            translation[i].replace(translation[j], '')

    a, b = (1, 0) if counts.get(translation['c'][0]) == 8 else (0, 1)
    translation['f'] = translation['c'][a]
    translation['c'] = translation['c'][b]

    for i in ['e', 'g']:
        for j in ['a', 'b', 'c', 'd', 'f']:
            translation[i] = translation[i].replace(translation[j], '')

    a, b = (1, 0) if counts.get(translation['e'][0]) == 4 else (0, 1)
    translation['g'] = translation['e'][a]
    translation['e'] = translation['e'][b]

    return 'abcdefg'.maketrans({x: y for y, x in translation.items()})


displays = puzzle.input_data.split('\n')
P1_ANSWER, P2_ANSWER = 0, 0
unique_lengths = [2, 3, 4, 7]
for display in displays:
    inputs, output = tuple(display.split(' | '))
    P1_ANSWER += sum([1 for digit in output.split() if len(digit) in unique_lengths])
    segments = list(map(sorted, [o.translate(decode((inputs + ' ' + output).split())) for o in output.split()]))
    P2_ANSWER += int(''.join([mapping.get(''.join(d)) for d in segments]))

# ----------------------------------- #
print(f"Finished in {timeit.default_timer() - start} seconds")

submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
submit(P2_ANSWER, part="b", year=YEAR, day=DAY)
