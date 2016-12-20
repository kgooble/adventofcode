#!/usr/bin/env python

num_elves = 3014387

class Elf:
    def __init__(self, i):
        self.i = i

    def take_present(self):
        if self.next_elf is self:
            raise Exception("Hey!! I'm the last elf:" + str(self.i))

        self.next_elf = self.next_elf.next_elf

def count(elf):
    first = elf.i

    count = 1
    the_elf = elf.next_elf
    while the_elf.i != first:
        count += 1
        the_elf = the_elf.next_elf

    return count

def part_one():
    first_elf = Elf(1)
    elf = first_elf

    for i in range(1, num_elves):
        elf.next_elf = Elf(i + 1)
        elf = elf.next_elf

    print "done making elves."

    elf.next_elf = first_elf
    elf = first_elf

    iterations = 0
    while True:
        if iterations % 10000 == 0:
            print "did", iterations, "iterations"
            print count(elf), "elves left"

        elf.take_present()
        elf = elf.next_elf
        iterations += 1


if __name__ == '__main__':
    part_one()
