#!/usr/bin/env python

import operator

PUZZLE_INPUT = ''
with open('day6_input') as f:
    PUZZLE_INPUT = f.readlines()

def highest_frequency(occurrences_dict):
    return sorted(occurrences_dict.items(), key=operator.itemgetter(1), reverse=True)[0][0]

def part_one():
    occurrences = [{}, {}, {}, {}, {}, {}, {}, {}]

    for line in PUZZLE_INPUT:
        for index, char in enumerate(line.strip()):
            occs = occurrences[index]
            if char not in occs:
                occs[char] = 0

            occs[char] += 1

    letters = [highest_frequency(occs) for occs in occurrences]

    print "The hidden message is '{}'.".format(''.join(letters))


def part_two():
    pass

if __name__ == '__main__':
    part_one()
    part_two()
