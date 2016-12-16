#!/usr/bin/env python

DISK_SIZE = 35651584
PUZZLE_INPUT = '10111011111001111'

def flip_value(value):
    return ''.join('0' if v == '1' else '1' for v in reversed(value))

def part_one():
    value = PUZZLE_INPUT

    while len(value) < DISK_SIZE:
        value = value + '0' + flip_value(value)

    print "Result of dragon curving:", len(value)

    value = value[:DISK_SIZE]
    checksum = value

    while len(checksum) % 2 == 0:
        new_checksum = []
        for i in range(0, len(checksum) - 1, 2):
            pair = checksum[i:i + 2]
            if pair[0] == pair[1]:
                new_checksum.append('1')
            else:
                new_checksum.append('0')

        checksum = new_checksum

    print 'The correct checksum is', ''.join(checksum)

def part_two():
    pass

if __name__ == '__main__':
    part_one()
    part_two()
