#!/usr/bin/env python

PUZZLE_INPUT = ''
with open('day8_input') as f:
    PUZZLE_INPUT = f.readlines()

def turn_on_rectangle(display, width, height):
    for y in range(0, height):
        for x in range(0, width):
            display[y][x] = 1

def rotate(col_or_row, shift):
    original = col_or_row[:]
    length = len(col_or_row)
    for i in range(0, length):
        col_or_row[i] = original[(length - shift + i) % length]

def rotate_row(display, row_index, shift):
    row = display[row_index]
    rotate(row, shift)

def rotate_column(display, column_index, shift):
    column = [row[column_index] for row in display]
    rotate(column, shift)
    for index, row in enumerate(display):
        row[column_index] = column[index]

def show(display):
    for row in display:
        print ''.join(['.' if c == 1 else ' ' for c in row])

WIDTH = 50
HEIGHT = 6

def part_one():
    display = [[0] * WIDTH for i in range(0, HEIGHT)]

    for line in PUZZLE_INPUT:
        instruction = line.strip()
        instruction_parts = instruction.split(' ')

        if len(instruction_parts) == 2:
            width, height = [int(dim) for dim in instruction_parts[1].split('x')]

            turn_on_rectangle(display, width, height)

            print 'executed instruction: ', instruction
            show(display)
            continue

        shift_position = int(instruction_parts[2].split('=')[1])
        shift_amount = int(instruction_parts[-1])

        if instruction_parts[1] == 'row':
            rotate_row(display, shift_position, shift_amount)
        else:
            rotate_column(display, shift_position, shift_amount)

        print 'executed instruction: ', instruction
        show(display)

    num_pixels = sum(sum(row) for row in display)
    print "{} pixels should be lit.".format(num_pixels)

def part_two():
    # Just look at print of part one
    pass

if __name__ == '__main__':
    part_one()
    part_two()
