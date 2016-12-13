#!/usr/bin/env python

from Queue import *
from itertools import chain, combinations

"""
The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant.
"""

class Generator:
    def __init__(self, name):
        self.name = name

    def matches(self, microchip):
        return self.name == microchip.name

    def __eq__(self, other):
        return self.name == other.name and isinstance(other, Generator)

    def __repr__(self):
        return self.name[0].upper() + self.name[1] + 'G'

    def __hash__(self):
        return hash(repr(self))

class Microchip:
    def __init__(self, name):
        self.name = name

    def matches(self, generator):
        return self.name == generator.name

    def __eq__(self, other):
        return self.name == other.name and isinstance(other, Microchip)

    def __repr__(self):
        return self.name[0].upper() + self.name[1] + 'M'

    def __hash__(self):
        return hash(repr(self))

class State:
    def __init__(self, num_moves, elevator_posn, floors):
        self.num_moves = num_moves
        self.elevator_posn = elevator_posn
        self.floors = floors

    def current_floor(self):
        return self.floors[self.elevator_posn]

    def on_top_floor(self):
        return self.elevator_posn == len(self.floors) - 1

    def on_ground_floor(self):
        return self.elevator_posn == 0

    def next_state(self, elevator_content, movement):
        new_elevator_position = self.elevator_posn + movement
        new_floors = []

        for index, floor in enumerate(self.floors):
            new_floor = floor.copy()
            if index == new_elevator_position:
                for item in elevator_content:
                    new_floor.add(item)
            elif index == self.elevator_posn:
                new_floor = set([c for c in new_floor if c not in elevator_content])

            new_floors.append(new_floor)

        return State(self.num_moves + 1, new_elevator_position, new_floors)

    def is_valid(self):
        if self.elevator_posn < 0 or self.elevator_posn >= len(self.floors):
            return False

        for floor in self.floors:
            generators = [g for g in floor if isinstance(g, Generator)]
            microchips = [m for m in floor if isinstance(m, Microchip)]

            # Nothing to worry about if there are no generators or no microchips
            if len(generators) == 0 or len(microchips) == 0:
                continue

            # There is no way to match all the microchips if there are more
            # chips than generators
            if len(microchips) > len(generators):
                return False

            matched = 0
            for m in microchips:
                for g in generators:
                    # A microchip is safe if it has been matched with a generator
                    if m.matches(g):
                        matched += 1

            if len(microchips) > matched:
                return False

        return True

    def is_terminal(self):
        return all(len(floor) == 0 for floor in self.floors[:-1])

    def __repr__(self):
        floor_reprs = ['Num Moves: ' + str(self.num_moves)]

        for index in range(len(self.floors) - 1, -1, -1):
            floor = self.floors[index]
            floor_repr = ['F' + str(index + 1), '.']
            if index == self.elevator_posn:
                floor_repr[1] = 'E'

            floor_repr.extend(repr(c) for c in floor)

            floor_reprs.append(' '.join(floor_repr))

        return '\n'.join(floor_reprs)

    def __eq__(self, other):
        return self.elevator_posn == other.elevator_posn and self.floors == other.floors

    def __hash__(self):
        return self.elevator_posn + sum(len(floor) * 10 * (index + 1) for index, floor in enumerate(self.floors))

THULIUM = 'thulium'
PLUTONIUM = 'plutonium'
STRONTIUM = 'strontium'
PROMETHIUM = 'promethium'
RUTHENIUM = 'ruthenium'

def is_valid_content(elevator_content):
    if len(elevator_content) == 1:
        # If it's just one item, it's OK no matter what
        return True

    if all(isinstance(x, Microchip) for x in elevator_content):
        # If it's two microchips, that's fine too
        return True

    if all(isinstance(x, Generator) for x in elevator_content):
        # Two generators are fine too
        return True

    # It's a microchip and a generator, make sure that the chip doesn't get fried!
    return elevator_content[0].matches(elevator_content[1])

def part_one():
    floors = [
        set([ Microchip('hydrogen'), Microchip('lithium') ]),
        set([ Generator('hydrogen') ]),
        set([ Generator('lithium') ]),
        set([])
    ]
    floors = [
        set([ Generator(THULIUM), Microchip(THULIUM), Generator(PLUTONIUM), Generator(STRONTIUM) ]),
        set([ Microchip(PLUTONIUM), Microchip(STRONTIUM) ]),
        set([ Generator(PROMETHIUM), Microchip(PROMETHIUM), Generator(RUTHENIUM), Microchip(RUTHENIUM) ]),
        set([])
    ]

    initial_state = State(0, 0, floors)

    states = Queue()
    states.put(initial_state)
    visited_states = set()
    visited_states.add(initial_state)
    tried_states = 0
    state = None

    while not states.empty():
        tried_states += 1
        state = states.get()

        print "Processing state {} with num moves {}...".format(tried_states, state.num_moves)

        if state.is_terminal():
            print "It took {} steps to get to this state:".format(state.num_moves)
            print state
            break

        floor = state.current_floor()

        valid_elevator_content = chain.from_iterable(
                combinations(floor, i) for i in range(1, min(3, len(floor) + 1)))

        valid_elevator_content = [c for c in valid_elevator_content if is_valid_content(c)]
        
        next_states = []

        if not state.on_ground_floor():
            next_states += [state.next_state(c, -1) for c in valid_elevator_content]

        if not state.on_top_floor():
            next_states += [state.next_state(c, +1) for c in valid_elevator_content]

        next_states = [s for s in next_states if s.is_valid() and s not in visited_states]

        for s in next_states:
            states.put(s)
            visited_states.add(s)

    print "Done! Final state:"
    print state

def part_two():
    pass

if __name__ == '__main__':
    part_one()
    part_two()
