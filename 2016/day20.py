#!/usr/bin/env python

PUZZLE_INPUT = ''
with open('day20_input') as f:
    PUZZLE_INPUT = f.readlines()

def part_one():
    ranges = []

    for line in PUZZLE_INPUT:
        start, end = (int(x) for x in (line.strip().split('-')))
        ranges.append((start, end))

    ranges.sort(key=lambda x: x[0])

    for i, rng in enumerate(ranges):
        if rng[1] < ranges[i + 1][0] - 1:
            print "The lowest allowed IP address is {}.".format(rng[1] + 1)
            break

if __name__ == '__main__':
    part_one()
