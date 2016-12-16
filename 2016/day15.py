#!/usr/bin/env python

PUZZLE_INPUT = """
Disc #1 has 7 positions; at time=0, it is at position 0.
Disc #2 has 13 positions; at time=0, it is at position 0.
Disc #3 has 3 positions; at time=0, it is at position 2.
Disc #4 has 5 positions; at time=0, it is at position 2.
Disc #5 has 17 positions; at time=0, it is at position 0.
Disc #6 has 19 positions; at time=0, it is at position 7.
Disc #7 has 11 positions; at time=0, it is at position 0.
""".strip().split('\n')

def part_one():
    discs = []

    for line in PUZZLE_INPUT:
        parts = line.strip().split(' ')
        num_positions = int(parts[3])
        initial_position = int(parts[-1][:-1])
        discs.append((num_positions, initial_position))

    print discs

    i = 0
    while True:
        print "Trying index", i
        all_zero = True
        for j in range(0, len(discs)):
            disc = discs[j]
            num_positions = disc[0]
            initial_position = disc[1]
            final_position = (i + j + 1 + initial_position) % num_positions

            if final_position != 0:
                all_zero = False
                break

        if all_zero:
            print "The first time you can press the button to get a capsule is {}.".format(i)
            break

        i += 1


def part_two():
    pass

if __name__ == '__main__':
    part_one()
    part_two()
