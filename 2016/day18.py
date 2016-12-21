#!/usr/bin/env python

def is_trap(left_center_right):
    left = left_center_right[0]
    center = left_center_right[1]
    right = left_center_right[2]

    if right == 1 and (left + center) == 0:
        return 0
    if left == 1 and (center + right) == 0:
        return 0
    if left == 0 and (center + right) == 2:
        return 0
    if right == 0 and (left + center) == 2:
        return 0

    return 1

def make_next_row(row):
    next_row = []

    for i, x in enumerate(row):
        if i == 0:
            left_center_right = [1] + row[:2]
        elif i == len(row) - 1:
            left_center_right = row[i-1:] + [1]
        else:
            left_center_right = row[i-1:i+2]

        next_row.append(is_trap(left_center_right))

    return next_row

def translate_row(row):
    return [1 if x == '.' else 0 for x in row]

def untranslate_row(row):
    return ''.join('.' if x == 1 else '^' for x in row)

def part_one():
    first_row = '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.'
    num_rows = 400000

    row = translate_row(first_row)
    safe_tiles = sum(row)

    for i in range(0, num_rows - 1):
        next_row = make_next_row(row)
        safe_tiles += sum(next_row)
        row = next_row

    print "There are {} safe tiles.".format(safe_tiles)


if __name__ == '__main__':
    part_one()
