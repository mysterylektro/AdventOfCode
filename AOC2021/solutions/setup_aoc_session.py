import os
from pathlib import Path

# Modify the filename to point to whatever file stores your AOC session ID.
filename = Path(__file__).parents[2].joinpath('aoc_session.txt')
with open(str(filename), 'r') as f:
    session = f.readline()

os.environ["AOC_SESSION"] = session
