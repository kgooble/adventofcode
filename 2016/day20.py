#!/usr/bin/env python

PUZZLE_INPUT = ''
with open('day20_input') as f:
    PUZZLE_INPUT = f.readlines()

def get_sorted_ranges():
    ranges = []

    for line in PUZZLE_INPUT:
        start, end = (int(x) for x in (line.strip().split('-')))
        ranges.append((start, end))

    ranges.sort(key=lambda x: x[0])

    return ranges

def part_one():
    ranges = get_sorted_ranges()

    for i, rng in enumerate(ranges):
        if rng[1] < ranges[i + 1][0] - 1:
            print "The lowest allowed IP address is {}.".format(rng[1] + 1)
            break

def find_enclosing_ranges(rng, visited):
    containers = []

    for r in visited:
        if r[0] <= rng[0] and r[1] >= rng[1]:
            containers.append(r)

    return containers

def part_two():
    ranges = get_sorted_ranges()

    visited_ranges = []

    num_ips_allowed = min(0, ranges[0][0])

    for i, rng in enumerate(ranges):
        if i == len(ranges) - 1:
            break

        next_start = ranges[i + 1][0]
        if rng[1] < next_start - 1:
            containers = find_enclosing_ranges(rng, visited_ranges)
            containers.sort(key=lambda x: x[1])

            if len(containers) == 0:
                num_ips_allowed += next_start - 1 - rng[1]
            elif containers[-1][1] < next_start - 1:
                num_ips_allowed += next_start - 1 - containers[-1][1]

        visited_ranges.append(rng)

    print "The number of IPs allowed is {}.".format(num_ips_allowed)


if __name__ == '__main__':
    part_two()
