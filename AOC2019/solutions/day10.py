"""
--- Day 10: Monitoring Station ---

You fly into the asteroid belt and reach the Ceres monitoring station. The Elves here have an emergency: they're
having trouble tracking all of the asteroids and can't be sure they're safe.

The Elves would like to build a new monitoring station in a nearby area of space; they hand you a map of all of the
asteroids in that region (your puzzle input).

The map indicates whether each position is empty (.) or contains an asteroid (#). The asteroids are much smaller than
they appear on the map, and every asteroid is exactly in the center of its marked position. The asteroids can be
described with X,Y coordinates where X is the distance from the left edge and Y is the distance from the top edge (so
the top-left corner is 0,0 and the position immediately to its right is 1,0).

Your job is to figure out which asteroid would be the best place to build a new monitoring station. A monitoring
station can detect any asteroid to which it has direct line of sight - that is, there cannot be another asteroid
exactly between them. This line of sight can be at any angle, not just lines aligned to the grid or diagonally. The
best location is the asteroid that can detect the largest number of other asteroids.

For example, consider the following map:

.#..#
.....
#####
....#
...##

The best location for a new monitoring station on this map is the highlighted asteroid at 3,4 because it can detect 8
asteroids, more than any other location. (The only asteroid it cannot detect is the one at 1,0; its view of this
asteroid is blocked by the asteroid at 2,2.) All other asteroids are worse locations; they can detect 7 or fewer
other asteroids. Here is the number of other asteroids a monitoring station on each asteroid could detect:

.7..7
.....
67775
....7
...87

Here is an asteroid (#) and some examples of the ways its line of sight might be blocked. If there were another
asteroid at the location of a capital letter, the locations marked with the corresponding lowercase letter would be
blocked and could not be detected:

#.........
...A......
...B..a...
.EDCG....a
..F.c.b...
.....c....
..efd.c.gb
.......c..
....f...c.
...e..d..c

Here are some larger examples:

Best is 5,8 with 33 other asteroids detected:

......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####

Best is 1,2 with 35 other asteroids detected:

#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.

Best is 6,3 with 41 other asteroids detected:

.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..

Best is 11,13 with 210 other asteroids detected:

.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##

Find the best location for a new monitoring station. How many other asteroids can be detected from that location?

--- Part Two ---

Once you give them the coordinates, the Elves quickly deploy an Instant Monitoring Station to the location and
discover the worst: there are simply too many asteroids.

The only solution is complete vaporization by giant laser.

Fortunately, in addition to an asteroid scanner, the new monitoring station also comes equipped with a giant rotating
laser perfect for vaporizing asteroids. The laser starts by pointing up and always rotates clockwise, vaporizing any
asteroid it hits.

If multiple asteroids are exactly in line with the station, the laser only has enough power to vaporize one of them
before continuing its rotation. In other words, the same asteroids that can be detected can be vaporized,
but if vaporizing one asteroid makes another one detectable, the newly-detected asteroid won't be vaporized until the
laser has returned to the same position by rotating a full 360 degrees.

For example, consider the following map, where the asteroid with the new monitoring station (and laser) is marked X:

.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##

The first nine asteroids to get vaporized, in order, would be:

.#....###24...#..
##...##.13#67..9#
##...#...5.8####.
..#.....X...###..
..#.#.....#....##

Note that some asteroids (the ones behind the asteroids marked 1, 5, and 7) won't have a chance to be vaporized until
the next full rotation. The laser continues rotating; the next nine to be vaporized are:

.#....###.....#..
##...##...#.....#
##...#......1234.
..#.....X...5##..
..#.9.....8....76

The next nine to be vaporized are then:

.8....###.....#..
56...9#...#.....#
34...7...........
..2.....X....##..
..1..............

Finally, the laser completes its first full rotation (1 through 3), a second rotation (4 through 8), and vaporizes
the last asteroid (9) partway through its third rotation:

......234.....6..
......1...5.....7
.................
........X....89..
.................

In the large example above (the one with the best monitoring station location at 11,13):

The 1st asteroid to be vaporized is at 11,12.
The 2nd asteroid to be vaporized is at 12,1.
The 3rd asteroid to be vaporized is at 12,2.
The 10th asteroid to be vaporized is at 12,8.
The 20th asteroid to be vaporized is at 16,0.
The 50th asteroid to be vaporized is at 16,9.
The 100th asteroid to be vaporized is at 10,16.
The 199th asteroid to be vaporized is at 9,6.
The 200th asteroid to be vaporized is at 8,2.
The 201st asteroid to be vaporized is at 10,9.
The 299th and final asteroid to be vaporized is at 11,1.

The Elves are placing bets on which will be the 200th asteroid to be vaporized. Win the bet by determining which
asteroid that will be; what do you get if you multiply its X coordinate by 100 and then add its Y coordinate? (For
example, 8,2 becomes 802.)

"""

# Compute coordinates for each asteroid.
# For each asteroid, calculate the other asteroids that are visible.
#   To do this, first calculate all relative coordinates and distances for all other asteroids.
#   Start with the closest asteroid, add it to a list of observable asteroids, and remove from list of test asteroids.
#   Calculate the greatest common denominator and use that to calculate a base vector.
#   Calculate coordinates that will block view. If any asteroids in those coordinates, skip, otherwise add as visible.
#   Return the number of visible for each asteroid.

import numpy as np
import math


def calculate_distances(coordinates):
    return [np.sqrt(x**2 + y**2) for x, y in coordinates]


def normalize_coordinates(coordinates, center_coordinate):
    normalized_coordinates = []
    for coordinate in coordinates:
        normalized_coordinates.append((coordinate[0] - center_coordinate[0],
                                       coordinate[1] - center_coordinate[1]))
    return normalized_coordinates


def check_1d_block_view(val1, val2):
    tf = False
    if val1 == 0:
        if val2 == 0:
            tf = True
    else:
        if np.sign(val1) == np.sign(val2):
            if val1 % val2 == 0 and val1 != val2:
                tf = True
    return tf


def normalize_vector(x, y):
    gcd = math.gcd(x, y)
    return x // gcd, y // gcd


def is_blocked(test_asteroid, asteroids):
    normal_vector = normalize_vector(*test_asteroid)
    if normal_vector[0] == 0:
        points_between = test_asteroid[1] / normal_vector[1]
    else:
        points_between = test_asteroid[0] / normal_vector[0]

    points_between = int(points_between)

    if points_between > 1:
        for j in range(1, points_between):
            blocking_coord = normal_vector[0] * j, normal_vector[1] * j
            if blocking_coord in asteroids:
                return True

    return False


def get_num_observable_asteroids(index, asteroids):
    num_observable = 0
    test_coordinates = normalize_coordinates(asteroids, asteroids[index])
    # Remove itself
    test_coordinates.remove((0, 0))
    distances = calculate_distances(test_coordinates)
    test_coordinates = [x for _, x in sorted(zip(distances, test_coordinates))]

    while len(test_coordinates) > 0:
        current_asteroid = test_coordinates.pop()
        if not is_blocked(current_asteroid, test_coordinates):
            num_observable += 1

    return num_observable


def get_next_vaporized_asteroid(asteroids, current_angle_index):
    # Asteroids are assumed to be ordered by angle
    asteroid_is_blocked = True
    vaporized_asteroid = None
    next_angle_index = current_angle_index
    while asteroid_is_blocked:
        test_asteroid = asteroids[next_angle_index]
        asteroid_is_blocked = is_blocked(test_asteroid, asteroids)
        if not asteroid_is_blocked:
            vaporized_asteroid = test_asteroid
            break
        next_angle_index += 1
        if next_angle_index >= len(asteroids):
            next_angle_index = 0

    return vaporized_asteroid, next_angle_index


def nth_vaporized_asteroid(stationed_asteroid, asteroids, n=200):
    normalized_coords = normalize_coordinates(asteroids, stationed_asteroid)
    angles = [np.rad2deg(np.arctan2(-1*coord[1], -1*coord[0])) - 90. for coord in normalized_coords]
    for idx, angle in enumerate(angles):
        if angle < 0:
            angle += 360.
        angles[idx] = angle

    # Sort asteroids and angles
    normalized_coords = [x for _, x in sorted(zip(angles, normalized_coords))]
    angles = sorted(angles)

    current_angle_index = 0
    input_list = normalized_coords.copy()
    vaporized_asteroid = (None, None)
    num_vaporized = 0
    while num_vaporized != n:
        vaporized_asteroid, idx = get_next_vaporized_asteroid(input_list, current_angle_index)
        num_vaporized += 1
        index = input_list.index(vaporized_asteroid)
        last_angle = angles.pop(index)
        input_list.pop(index)
        vaporized_asteroid = (vaporized_asteroid[0] + stationed_asteroid[0],
                              vaporized_asteroid[1] + stationed_asteroid[1])
        while last_angle == angles[idx]:
            idx += 1
            if idx >= len(angles):
                idx = 0
        current_angle_index = idx

    return vaporized_asteroid


if __name__ == '__main__':
    input_file = '../inputs/day10.txt'
    asteroid_coordinates = []
    row = -1
    column = -1
    count = 1
    with open(input_file) as f:
        for line in f:
            row += 1
            for char in line:
                column += 1
                if char == '#':
                    asteroid_coordinates.append((column, row))
                    count += 1
            column = -1

    num_observable_asteroids = []

    for i, asteroid in enumerate(asteroid_coordinates):
        num_observable_asteroids.append(get_num_observable_asteroids(i, asteroid_coordinates))

    print("Answer to Part 1: " + str(max(num_observable_asteroids)))

    best_asteroid = asteroid_coordinates[num_observable_asteroids.index(max(num_observable_asteroids))]

    x, y = nth_vaporized_asteroid(best_asteroid, asteroid_coordinates, n=200)

    print("Answer to Part 2: " + str(x*100 + y))
