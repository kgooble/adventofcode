#!/usr/bin/env python

PUZZLE_INPUT = """
L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2
""".strip()


NORTH = 0
SOUTH = 180
EAST = 90
WEST = 270

LEFT = 'L'
RIGHT = 'R'

def get_new_direction(old_direction, turn):
    direction = old_direction

    if turn == LEFT:
        direction -= 90
    else:
        direction += 90

    direction = direction % 360

    return direction

def get_x_y(direction, distance, x, y):
    if direction == NORTH:
        y = y + distance
    elif direction == SOUTH:
        y = y - distance
    elif direction == WEST:
        x = x - distance
    elif direction == EAST:
        x = x + distance

    return x, y


def part_one():
    print "Calculating Day 1 part 1..."
    direction = NORTH
    instructions = PUZZLE_INPUT.split(', ')

    x = 0
    y = 0

    for instr in instructions:
        turn = instr[0]
        distance = int(instr[1:])

        direction = get_new_direction(direction, turn)
        x, y = get_x_y(direction, distance, x, y)

    print "The final location is ({}, {}).".format(x, y)
    print "The total distance from the start is {}.".format(abs(x) + abs(y))

def sign(a):
    if a > 0:
        return 1
    else:
        return -1

def part_two():
    print "Calculating Day 1 part 2..."
    direction = NORTH
    instructions = PUZZLE_INPUT.split(', ')

    old_positions = {}
    x = 0
    y = 0

    for instr in instructions:
        old_x = x
        old_y = y

        turn = instr[0]
        distance = int(instr[1:])

        direction = get_new_direction(direction, turn)
        x, y = get_x_y(direction, distance, x, y)

        found = False
        for ix in range(old_x, x, sign(x - old_x)):
            pos = (ix, y)

            if pos in old_positions:
                x = ix
                found = True
                break

            old_positions[pos] = 1

        for iy in range(old_y, y, sign(y - old_y)):
            pos = (x, iy)

            if pos in old_positions:
                y = iy
                found = True
                break

            old_positions[pos] = 1

        if found:
            break

    print "The first position visited twice is ({}, {}).".format(x, y)
    print "The total distance from the start is {}.".format(abs(x) + abs(y))

if __name__ == '__main__':
    part_one()
    print "----"
    part_two()
