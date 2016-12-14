#!/usr/bin/env python

from Queue import *
from itertools import chain, combinations

def is_valid(s):
    x = s[0]
    y = s[1]

    if x < 0 or y < 0:
        return False

    return not is_wall(x, y)

def is_wall(x, y):
    the_sum = 1358 + x * (3 + x) + y * (2 * x + 1 + y)
    binary_repr = "{0:b}".format(the_sum)
    sum_of_bits = sum(int(b) for b in binary_repr)

    return sum_of_bits % 2 == 1

def part_one():
    initial_state = (1, 1, 0)

    states = Queue()
    states.put(initial_state)

    visited_states = set()
    visited_states.add((1, 1))

    tried_states = 0
    state = None

    while not states.empty():
        tried_states += 1
        state = states.get()
        x = state[0]
        y = state[1]
        n = state[2]

        if n == 50:
            break

        print "Processing state {} with num moves {}...".format(tried_states, n)

        if x == 31 and y == 39:
            print "It took {} steps to get to this state:".format(n)
            print state
            break

        next_states = [(x - 1, y,     n + 1),
                       (x,     y + 1, n + 1),
                       (x + 1, y,     n + 1),
                       (x,     y - 1, n + 1)]

        for s in next_states:
            coords = (s[0], s[1])
            if is_valid(s) and coords not in visited_states:
                states.put(s)
                visited_states.add(coords)

    print "Done! Final state:"
    print state

    print "Distinct places:"
    print len(visited_states)

def part_two():
    pass

if __name__ == '__main__':
    part_one()
    part_two()
