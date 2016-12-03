#!/usr/bin/env python

PUZZLE_INPUT = ''
with open('day3_input') as f:
    PUZZLE_INPUT = f.readlines()

def part_one():
    valid_count = 0

    for line in PUZZLE_INPUT:
        sides = [int(instr) for instr in line.strip().split(' ') if instr != '']

        if sides[0] + sides[1] <= sides[2]:
            continue

        if sides[0] + sides[2] <= sides[1]:
            continue

        if sides[1] + sides[2] <= sides[0]:
            continue

        valid_count += 1

    print "{} triangles are possible.".format(valid_count)

if __name__ == '__main__':
    part_one()
