#!/usr/bin/env python

import operator

PUZZLE_INPUT = ''
with open('day4_input') as f:
    PUZZLE_INPUT = f.readlines()

def calculate_sector_id(room):
    encrypted_name = room[:-11]
    sector_id = room[-10:-7]
    checksum = room[-6:-1]

    letter_frequencies = {}

    for letter in encrypted_name:
        if letter == '-':
            continue

        if letter not in letter_frequencies:
            letter_frequencies[letter] = 0

        letter_frequencies[letter] += 1

    sorted_frequencies = letter_frequencies.items()[:]
    sorted_frequencies.sort(cmp_items)
    first_letters = [item[0] for item in sorted_frequencies][:5]

    real_room = True

    for c in checksum:
        if c not in first_letters:
            real_room = False
            break

    if real_room:
        print room, "was a real room."
        return int(sector_id)
    else:
        print room, "was NOT a real room."
        return 0

def cmp_items(a, b):
    if a[1] > b[1]:
        return -1
    if a[1] < b[1]:
        return 1
    if a[0] < b[0]:
        return -1
    return 1

def part_one():
    sector_id_sum = 0

    for line in PUZZLE_INPUT:
        sector_id_sum += calculate_sector_id(line.strip())

    print "The sum of the sector IDs of the real rooms is {}.".format(sector_id_sum)

def part_two():
    pass

if __name__ == '__main__':
    assert calculate_sector_id("aaaaa-bbb-z-y-x-123[abxyz]") > 0
    assert calculate_sector_id("a-b-c-d-e-f-g-h-987[abcde]") > 0
    assert calculate_sector_id("not-a-real-room-404[oarel]") > 0
    assert calculate_sector_id("totally-real-room-200[decoy]") == 0
    part_one()
    part_two()
