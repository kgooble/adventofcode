#!/usr/bin/env python
PUZZLE_INPUT = ''
with open('day7_input') as f:
    PUZZLE_INPUT = f.readlines()

def has_abba(string):
    if len(string) < 4:
        return False

    for i in range(0, len(string) - 3):
        if string[i] != string[i + 1] and string[i + 1] == string[i + 2] and string[i] == string[i + 3]:
            return True

    return False

def has_aba(string):
    if len(string) < 3:
        return False

    for i in range(0, len(string) - 2):
        if string[i] != string[i + 1] and string[i] == string[i + 2]:
            return True

    return False

OUTSIDE = 'outside'
INSIDE = 'inside'

def part_one():
    count = 0
    for line in PUZZLE_INPUT:
        state = OUTSIDE

        ip = line.strip()
        outside_has_abba = False
        inside_has_abba = False
        char_count = 0
        for index, char in enumerate(ip):
            if char_count < 3:
                char_count += 1
                continue

            if char == '[':
                state = INSIDE
                char_count = 0
            elif char == ']':
                state = OUTSIDE
                char_count = 0
            else:
                if state == INSIDE:
                    inside_has_abba = inside_has_abba or has_abba(ip[index - 3:index + 1])
                else:
                    outside_has_abba = outside_has_abba or has_abba(ip[index - 3:index + 1])

            if inside_has_abba:
                break

        if outside_has_abba and not inside_has_abba:
            print "{} supports TLS.".format(ip)
            count += 1


    print "There are {} IP addresses that support TLS.".format(count)

def part_two():
    count = 0
    for line in PUZZLE_INPUT:
        ip = line.strip()
        state = OUTSIDE
        abas = set()
        babs = set()

        char_count = 0
        for index, char in enumerate(ip):
            if char_count < 2:
                char_count += 1
                continue

            if char == '[':
                state = INSIDE
                char_count = 0
            elif char == ']':
                state = OUTSIDE
                char_count = 0
            else:
                substring = ip[index - 2:index + 1]
                if state == INSIDE and has_aba(substring):
                    babs.add(substring)
                elif state == OUTSIDE and has_aba(substring):
                    abas.add(substring)

        flipped_babs = set()
        for bab in babs:
            flipped_babs.add(bab[1] + bab[0] + bab[1])

        if len(abas.intersection(flipped_babs)) > 0:
            print "{} supports SSL.".format(ip)
            count += 1

    print "There are {} IP addresses that support SSL.".format(count)

if __name__ == '__main__':
    part_one()
    part_two()
