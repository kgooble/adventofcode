#!/usr/bin/env python

PUZZLE_INPUT = ''
with open('day21_input') as f:
    PUZZLE_INPUT = f.readlines()

PUZZLE_INPUT = """
swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
""".strip().split('\n')

def swap_position(string, i, j):
    return string

def swap_letter(string, a, b):
    return string

def rotate_left(string, n):
    return string

def rotate_right(string, n):
    return string

def rotate_based_on_letter(string, c):
    return string

def reverse(string, start, end):
    return string

def move(string, start, end):
    return string

def part_one():
    to_scramble = 'abcde'

    scrambled = to_scramble
    for line in PUZZLE_INPUT:
        parts = line.strip().split(' ')

        if parts[0] == 'swap' and parts[1] == 'position':
            scrambled = swap_position(scrambled, int(parts[2]), int(parts[-1]))
        elif parts[0] == 'swap' and parts[1] == 'letter':
            scrambled = swap_letter(scrambled, parts[2], parts[-1])
        elif parts[0] == 'rotate' and parts[1] == 'left':
            scrambled = rotate_left(scrambled, int(parts[2]))
        elif parts[0] == 'rotate' and parts[1] == 'based':
            scrambled = rotate_based_on_letter(scrambled, parts[-1])
        elif parts[0] == 'reverse':
            scrambled = reverse(scrambled, int(parts[2]), int(parts[-1]))
        elif parts[0] == 'move':
            scrambled = move(scrambled, int(parts[2]), int(parts[-1]))
        else:
            raise Exception("Unexpected instruction: " + line.strip())

    print "The resulting scrambled password is {}.".format(scrambled)

if __name__ == '__main__':
    part_one()
