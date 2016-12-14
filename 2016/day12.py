#!/usr/bin/env python

PUZZLE_INPUT = ''
with open('day12_input') as f:
    PUZZLE_INPUT = f.readlines()


def part_one():
    pc = 0

    registers = { 'a': 0, 'b': 0, 'c': 0, 'd': 0 }

    while pc < len(PUZZLE_INPUT):
        instruction = PUZZLE_INPUT[pc].strip().split(' ')

        cmd = instruction[0]

        if cmd == 'cpy':
            src = instruction[1]
            dest = instruction[2]

            if src in registers:
                registers[dest] = registers[src]
            else:
                registers[dest] = int(src)

        elif cmd == 'inc':
            src = instruction[1]
            registers[src] += 1

        elif cmd == 'dec':
            src = instruction[1]
            registers[src] -= 1

        elif cmd == 'jnz':
            src = instruction[1]

            if src in registers:
                if registers[src] != 0:
                    pc += int(instruction[2])
                    continue
            elif src != '0':
                pc += int(instruction[2])
                continue

        pc += 1

    print "The value left in register a is {}.".format(registers['a'])

def part_two():
    # See day one - put 1 in c register.
    pass

if __name__ == '__main__':
    part_one()
    part_two()
