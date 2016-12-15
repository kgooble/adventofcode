#!/usr/bin/env python

import hashlib

PUZZLE_INPUT = 'cuanljph'

def check_for_threes(h):
    char = h[0]
    count = 1
    for c in h[1:]:
        if count == 3:
            return char
        if c == char:
            count += 1
        else:
            char = c
            count = 1

    if count == 3:
        return char

    return None

def check_for_fives(h):
    fives = set()

    char = h[0]
    count = 1
    for c in h[1:]:
        if count == 5:
            fives.add(char)
        if c == char:
            count += 1
        else:
            char = c
            count = 1

    return fives

def get_hash(index):
    m = hashlib.md5()
    m.update(PUZZLE_INPUT + str(index))
    h = m.hexdigest()
    for i in range(0, 2016):
        m = hashlib.md5()
        m.update(h)
        h = m.hexdigest()

    return h

def part_one():
    index = 0
    potentials = []
    keys = []

    while True:
        print "index", index
        hex_code = get_hash(index)

        five_in_a_rows = check_for_fives(hex_code)

        if len(five_in_a_rows) > 0:
            # Filter out the ones that were found over 1000 ago
            potentials = [p for p in potentials if p[1] + 1000 > index]

            found = []
            for p in potentials:
                if p[0] in five_in_a_rows:
                    keys.append(p)
                    found.append(p)

            if len(found) > 0:
                potentials = [p for p in potentials if p not in found]
                keys.sort(key=lambda k: k[1])

        three_in_a_row = check_for_threes(hex_code)

        if three_in_a_row:
            potentials.append((three_in_a_row, index))
            potentials.sort(key=lambda p: p[1])

        if len(keys) >= 64 and keys[63][1] < potentials[0][1]:
            print "Found it: "
            for i, k in enumerate(keys):
                print i, k
            break

        index += 1

def part_two():
    pass

if __name__ == '__main__':
    part_one()
    part_two()
