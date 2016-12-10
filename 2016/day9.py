#!/usr/bin/env python

PUZZLE_INPUT = ''
with open('day9_input') as f:
    PUZZLE_INPUT = f.read().strip()

def part_one():
    the_string = []

    reading_marker = False
    marker_holder = ''
    num_chars_to_copy = 0
    num_copies = 0

    to_copy = ''

    for char in PUZZLE_INPUT:
        if char.isspace():
            continue

        if reading_marker:
            marker_holder += char
            if char == ')':
                reading_marker = False
                num_chars_to_copy, num_copies = [int(piece) for piece in marker_holder[1:-1].split('x')]
        else:
            if num_chars_to_copy > 0:
                to_copy += char
                num_chars_to_copy -= 1

                if num_chars_to_copy == 0:
                    the_string.append(to_copy * num_copies)
                    num_copies = 0
                    to_copy = ''
            elif char == '(':
                reading_marker = True
                marker_holder = '('
            else:
                the_string.append(char)

    print "The decompressed length of the file is {}.".format(sum(len(s) for s in the_string))

class Multiplier:
    def __init__(self, chars_to_copy, num_copies):
        self.chars_to_copy = chars_to_copy
        self.num_copies = num_copies

    def decrement(self):
        self.chars_to_copy -= 1

    def done(self):
        return self.chars_to_copy == 0

def part_two():
    count = 0
    reading_marker = False
    marker_holder = ''
    multipliers = []

    for char in PUZZLE_INPUT:
        if char.isspace():
            continue

        if reading_marker:
            marker_holder += char
            if char == ')':
                reading_marker = False
                num_chars_to_copy, num_copies = [int(piece)
                                                 for piece in marker_holder[1:-1].split('x')]

                # We add one here to account for the fact that all multipliers will be
                # decremented at the end of this iteration; however, this one does not
                # take effect until the next iteration
                multipliers.append(Multiplier(num_chars_to_copy + 1, num_copies))
        else:
            if char == '(':
                reading_marker = True
                marker_holder = '('
            else:
                total_multiplier = reduce(lambda x, y: x * y, [m.num_copies for m in multipliers], 1)
                count += total_multiplier

        for multiplier in multipliers:
            multiplier.decrement()

        multipliers = [m for m in multipliers if not m.done()]

    print "The decompressed length of the file was {}.".format(count)

if __name__ == '__main__':
    part_one()
    part_two()
