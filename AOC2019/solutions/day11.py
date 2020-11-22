"""
--- Day 11: Space Police ---

On the way to Jupiter, you're pulled over by the Space Police.

"Attention, unmarked spacecraft! You are in violation of Space Law! All spacecraft must have a clearly visible
registration identifier! You have 24 hours to comply or be sent to Space Jail!"

Not wanting to be sent to Space Jail, you radio back to the Elves on Earth for help. Although it takes almost three
hours for their reply signal to reach you, they send instructions for how to power up the emergency hull painting
robot and even provide a small Intcode program (your puzzle input) that will cause it to paint your ship appropriately.

There's just one problem: you don't have an emergency hull painting robot.

You'll need to build a new emergency hull painting robot. The robot needs to be able to move around on the grid of
square panels on the side of your ship, detect the color of its current panel, and paint its current panel black or
white. (All of the panels are currently black.)

The Intcode program will serve as the brain of the robot. The program uses input instructions to access the robot's
camera: provide 0 if the robot is over a black panel or 1 if the robot is over a white panel. Then, the program will
output two values:

First, it will output a value indicating the color to paint the panel the robot is over: 0 means to paint the panel
black, and 1 means to paint the panel white.

Second, it will output a value indicating the direction the robot should turn: 0 means it should turn left 90
degrees, and 1 means it should turn right 90 degrees.

After the robot turns, it should always move forward exactly one panel. The robot starts facing up.

The robot will continue running for a while like this and halt when it is finished drawing. Do not restart the
Intcode computer inside the robot during this process.

For example, suppose the robot is about to start running. Drawing black panels as ., white panels as #, and the robot
pointing the direction it is facing (< ^ > v), the initial state and region near the robot looks like this:

.....
.....
..^..
.....
.....

The panel under the robot (not visible here because a ^ is shown instead) is also black, and so any input
instructions at this point should be provided 0. Suppose the robot eventually outputs 1 (paint white) and then 0 (
turn left). After taking these actions and moving forward one panel, the region now looks like this:

.....
.....
.<#..
.....
.....

Input instructions should still be provided 0. Next, the robot might output 0 (paint black) and then 0 (turn left):

.....
.....
..#..
.v...
.....

After more outputs (1,0, 1,0):

.....
.....
..^..
.##..
.....

The robot is now back where it started, but because it is now on a white panel, input instructions should be provided
1. After several more outputs (0,1, 1,0, 1,0), the area looks like this:

.....
..<#.
...#.
.##..
.....

Before you deploy the robot, you should probably have an estimate of the area it will cover: specifically,
you need to know the number of panels it paints at least once, regardless of color. In the example above,
the robot painted 6 panels at least once. (It painted its starting panel twice, but that panel is still only counted
once; it also never painted the panel it ended on.)

Build a new emergency hull painting robot and run the Intcode program on it. How many panels does it paint at least
once?

--- Part Two ---

You're not sure what it's trying to paint, but it's definitely not a registration identifier. The Space Police are
getting impatient.

Checking your external ship cameras again, you notice a white panel marked "emergency hull painting robot starting
panel". The rest of the panels are still black, but it looks like the robot was expecting to start on a white panel,
not a black one.

Based on the Space Law Space Brochure that the Space Police attached to one of your windows, a valid registration
identifier is always eight capital letters. After starting the robot on a single white panel instead,
what registration identifier does it paint on your hull?

"""

from matplotlib import pyplot as plt
import numpy as np

from AOC2019.solutions.day9 import RelativeIntComputer


class PaintRobot:
    def __init__(self, code):
        self.computer = RelativeIntComputer(code)
        self.position = (0, 0)
        self.painted_panels = {}
        self.direction = (0, 1)

    def reset(self, code):
        self.position = (0, 0)
        self.painted_panels = {}
        self.direction = (0, 1)
        self.computer.reset(code)

    def change_direction(self, val, verbose=False):
        x = self.direction[0]
        y = self.direction[1]

        multiplier = -1 if val == 0 else 1
        new_x = multiplier * y if x == 0 else 0
        new_y = -1 * multiplier * x if y == 0 else 0

        if verbose:
            turn = 'left' if val == 0 else 'right'
            print("Turning %s from direction %s,%s to new direction %s,%s" % (turn,
                                                                               x,
                                                                               y,
                                                                               new_x,
                                                                               new_y))

        self.direction = (new_x, new_y)

    def paint_panel(self, val, verbose=False):
        if verbose:
            color = 'white' if val else 'black'
            print("Painting position %s,%s color %s" % (self.position[0],
                                                        self.position[1],
                                                        color))
        self.painted_panels[self.position] = val

    def num_painted_panels(self):
        return len(self.painted_panels)

    def get_panel_color(self, verbose=False):
        if self.position in self.painted_panels:
            return_val = self.painted_panels[self.position]
            if verbose:
                print("Painted position %s,%s before, last paint color was %s" % (self.position[0],
                                                                                  self.position[1],
                                                                                  return_val))
        else:
            return_val = 0
            if verbose:
                print("Never painted position %s,%s before, returning paint color black (%s)" % (self.position[0],
                                                                                                 self.position[1],
                                                                                                 return_val))

        return return_val

    def step_forward(self, verbose=False):
        new_x, new_y = self.position[0] + self.direction[0], self.position[1] + self.direction[1]
        if verbose:
            axis = 'x' if self.direction[0] != 0 else 'y'
            if axis == 'x':
                if self.direction[0] == -1:
                    axis = '-x'
            if axis == 'y':
                if self.direction[1] == -1:
                    axis = '-y'
            print("Stepping forward in the %s direction from position %s,%s to position %s,%s" % (axis,
                                                                                                  self.position[0],
                                                                                                  self.position[1],
                                                                                                  new_x,
                                                                                                  new_y))
        self.position = (new_x, new_y)

    def run(self, verbose=False):
        while not self.computer.halted:
            self.computer.run(input_val=self.get_panel_color(verbose=verbose))
            self.paint_panel(self.computer.output[-2], verbose=verbose)
            self.change_direction(self.computer.output[-1], verbose=verbose)
            self.step_forward(verbose=verbose)
            if verbose:
                print("--------------")


def show_paint_output(robot):

    max_x = max([x for x, y in robot.painted_panels.keys()])
    min_x = min([x for x, y in robot.painted_panels.keys()])
    max_y = max([y for x, y in robot.painted_panels.keys()])
    min_y = min([y for x, y in robot.painted_panels.keys()])

    canvas = np.zeros((max_x - min_x + 1, max_y - min_y + 1))
    for coord, paint_color in robot.painted_panels.items():
        canvas[coord[0], coord[1]] = paint_color
    canvas = np.roll(canvas, -1, axis=1)
    canvas = np.flip(canvas, axis=1)
    plt.imshow(np.transpose(canvas))
    plt.show()


if __name__ == '__main__':
    input_file = '../inputs/day11.txt'
    with open(input_file) as f:
        instructions = [int(i) for i in f.readline().split(',')]

    robot = PaintRobot(instructions)
    robot.run()
    print("Answer to Part 1: " + str(robot.num_painted_panels()))

    # show_paint_output(robot)

    robot = PaintRobot(instructions)
    robot.paint_panel(1)
    robot.run()

    show_paint_output(robot)



