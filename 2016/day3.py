#!/usr/bin/env python

PUZZLE_INPUT = ''
with open('day3_input') as f:
    PUZZLE_INPUT = f.readlines()

def is_valid_triangle(sides):
    if sides[0] + sides[1] <= sides[2]:
        return False

    if sides[0] + sides[2] <= sides[1]:
        return False

    if sides[1] + sides[2] <= sides[0]:
        return False

    return True

def split_line_into_sides(line):
    return [int(instr) for instr in line.strip().split(' ') if instr != '']

def valid_count_for_batch(triangle_batch):
    valid_count = 0

    for sides in triangle_batch:
        valid_count += 1 if is_valid_triangle(sides) else 0

    return valid_count

def part_one():
    valid_count = 0

    for line in PUZZLE_INPUT:
        sides = split_line_into_sides(line)

        if is_valid_triangle(sides):
            valid_count += 1

    print "{} triangles are possible.".format(valid_count)

def part_two():
    valid_count = 0

    triangle_batch = [[], [], []]
    for line in PUZZLE_INPUT:
        if len(triangle_batch[0]) == 3:
            valid_count += valid_count_for_batch(triangle_batch)
            triangle_batch = [[], [], []]

        sides = split_line_into_sides(line)
        for i in range(0, len(sides)):
            triangle_batch[i].append(sides[i])

    if len(triangle_batch[0]) == 3:
        valid_count += valid_count_for_batch(triangle_batch)
        triangle_batch = [[], [], []]

    print "{} triangles are possible.".format(valid_count)

if __name__ == '__main__':
    part_one()
    part_two()
