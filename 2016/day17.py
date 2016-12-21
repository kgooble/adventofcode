#!/usr/bin/env python

import hashlib
from Queue import *

salt = 'awrkjxxr'

def hash_a_thing(string):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()[:4]

class State:
    def __init__(self, position, steps):
        self.position = position
        self.steps = steps

    def num_moves(self):
        return len(self.steps)

    def is_terminal(self):
        return self.position[0] == 3 and self.position[1] == 3

    def next_state(self, x_dir, y_dir, direction):
        return State((self.position[0] + x_dir, self.position[1] + y_dir), self.steps + direction)

    def __eq__(self, other):
        return self.position == other.position and self.steps == other.steps

    def __hash__(self):
        return hash(self.position) + hash(self.steps)

    def __repr__(self):
        return str(self.position) + self.steps

def part_one():
    initial_state = State((0, 0), '')

    states = Queue()
    states.put(initial_state)

    visited_states = set()
    visited_states.add(initial_state)

    terminal_states = []

    tried_states = 0
    state = None

    open_doors = 'bcdef'

    while not states.empty():
        tried_states += 1
        state = states.get()

        if state.is_terminal():
            terminal_states.append(state)
            continue
            #print "It took {} steps to get to this state".format(state.num_moves())
            #print "The shortest path was", state.steps
            #break

        open_doors_str = hash_a_thing(salt + state.steps)

        next_states = []
        x = state.position[0]
        y = state.position[1]

        if y > 0 and open_doors_str[0] in open_doors:
            next_states.append(state.next_state(0, -1, 'U'))

        if x > 0 and open_doors_str[2] in open_doors:
            next_states.append(state.next_state(-1, 0, 'L'))

        if y < 3 and open_doors_str[1] in open_doors:
            next_states.append(state.next_state(0, 1, 'D'))

        if x < 3 and open_doors_str[3] in open_doors:
            next_states.append(state.next_state(1, 0, 'R'))

        for s in next_states:
            if s not in visited_states:
                visited_states.add(s)
                states.put(s)


    sorted_terminals = sorted(terminal_states, key=lambda x: len(x.steps))
    print len(sorted_terminals[-1].steps)

if __name__ == '__main__':
    part_one()
