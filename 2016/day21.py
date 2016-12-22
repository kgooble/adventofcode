#!/usr/bin/env python

PUZZLE_INPUT = ''
with open('day21_input') as f:
    PUZZLE_INPUT = f.readlines()

#PUZZLE_INPUT = """
#swap position 4 with position 0
#swap letter d with letter b
#reverse positions 0 through 4
#rotate left 1 step
#move position 1 to position 4
#move position 3 to position 0
#rotate based on position of letter b
#rotate based on position of letter d
#""".strip().split("\n")

def swap_position(string, i, j):
    tmp = string[j]
    string[j] = string[i]
    string[i] = tmp
    return string

def swap_letter(string, a, b):
    for i, c in enumerate(string):
        if c == a:
            string[i] = b
        elif c == b:
            string[i] = a

    return string

def rotate_left(string, n):
    copy = string[:]
    length = len(string)

    for i in range(0, length):
        copy[i] = string[(length + n + i) % length]

    return copy

def rotate_right(string, n):
    copy = string[:]
    length = len(string)

    for i in range(0, length):
        copy[i] = string[(length - n + i) % length]

    return copy

def rotate_based_on_letter(string, c):
    i = string.index(c)
    rotations = 1 + i

    if i > 3:
        rotations += 1

    return rotate_right(string, rotations)

def reverse(string, start, end):
    original = string[:]

    for i in range(start, end + 1):
        string[i] = original[end - (i - start)]

    return string

def move(string, start, end):
    c = string[start]
    removed = string[:start] + string[start + 1:]
    removed.insert(end, c)
    return removed

def reverse_swap_position(string, i, j):
    return swap_position(string, i, j)

def reverse_swap_letter(string, a, b):
    return swap_letter(string, a, b)

def reverse_rotate_left(string, n):
    return rotate_right(string, n)

def reverse_rotate_right(string, n):
    return rotate_left(string, n)

def reverse_rotate_based_on_letter(string, c):
    for i in range(1, len(string) + 1):
        left_rotated = rotate_left(string[:], i)
        result = rotate_based_on_letter(left_rotated[:], c)
        if result == string:
            return left_rotated

    raise Exception("Couldn't find the correct rotation")

def reverse_reverse(string, start, end):
    original = string[:]

    for i in range(start, end + 1):
        string[i] = original[end - (i - start)]

    return string

def reverse_move(string, end, start):
    c = string[start]
    removed = string[:start] + string[start + 1:]
    removed.insert(end, c)
    return removed

def part_one():
    to_scramble = list('abcdefgh')

    scrambled = to_scramble
    for line in PUZZLE_INPUT:
        parts = line.strip().split(' ')

        if parts[0] == 'swap' and parts[1] == 'position':
            scrambled = swap_position(scrambled, int(parts[2]), int(parts[-1]))
        elif parts[0] == 'swap' and parts[1] == 'letter':
            scrambled = swap_letter(scrambled, parts[2], parts[-1])
        elif parts[0] == 'rotate' and parts[1] == 'left':
            scrambled = rotate_left(scrambled, int(parts[2]))
        elif parts[0] == 'rotate' and parts[1] == 'right':
            scrambled = rotate_right(scrambled, int(parts[2]))
        elif parts[0] == 'rotate' and parts[1] == 'based':
            scrambled = rotate_based_on_letter(scrambled, parts[-1])
        elif parts[0] == 'reverse':
            scrambled = reverse(scrambled, int(parts[2]), int(parts[-1]))
        elif parts[0] == 'move':
            scrambled = move(scrambled, int(parts[2]), int(parts[-1]))
        else:
            raise Exception("Unexpected instruction: " + line.strip())

    print "The resulting scrambled password is {}.".format(''.join(scrambled))

def part_two():
    to_scramble = list('fbgdceah')
    scrambled = to_scramble
    PUZZLE_INPUT.reverse()

    for line in PUZZLE_INPUT:
        parts = line.strip().split(' ')

        if parts[0] == 'swap' and parts[1] == 'position':
            scrambled = reverse_swap_position(scrambled, int(parts[2]), int(parts[-1]))
        elif parts[0] == 'swap' and parts[1] == 'letter':
            scrambled = reverse_swap_letter(scrambled, parts[2], parts[-1])
        elif parts[0] == 'rotate' and parts[1] == 'left':
            scrambled = reverse_rotate_left(scrambled, int(parts[2]))
        elif parts[0] == 'rotate' and parts[1] == 'right':
            scrambled = reverse_rotate_right(scrambled, int(parts[2]))
        elif parts[0] == 'rotate' and parts[1] == 'based':
            scrambled = reverse_rotate_based_on_letter(scrambled, parts[-1])
        elif parts[0] == 'reverse':
            scrambled = reverse_reverse(scrambled, int(parts[2]), int(parts[-1]))
        elif parts[0] == 'move':
            scrambled = reverse_move(scrambled, int(parts[2]), int(parts[-1]))
        else:
            raise Exception("Unexpected instruction: " + line.strip())

    print "The resulting unscrambled password is {}.".format(''.join(scrambled))

if __name__ == '__main__':
    part_one()
    part_two()
