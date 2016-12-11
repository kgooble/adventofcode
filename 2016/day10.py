#!/usr/bin/env python

PUZZLE_INPUT = ''
with open('day10_input') as f:
    PUZZLE_INPUT = f.readlines()

def give_bot(bots, bot, val):
    if bot not in bots:
        bots[bot] = []

    bots[bot].append(val)

def part_one():
    bots = {}

    transfer_instructions = []

    for line in PUZZLE_INPUT:
        instruction = line.strip()
        instruction_parts = instruction.split(' ')
        if len(instruction_parts) == 6:
            # value x goes to bot k
            val = int(instruction_parts[1])
            bot = int(instruction_parts[-1])

            give_bot(bots, bot, val)

            print "Bot {} now has {} in its hands.".format(bot, bots[bot])
        else:
            transfer_instructions.append(instruction_parts)

    i = 0
    while True:
        if i >= len(transfer_instructions):
            i = 0

        instruction_parts = transfer_instructions[i]
        i += 1

        if len(instruction_parts) == 0:
            print "Already processed this instruction. Skipping."
            continue

        # bot k gives low to output|bot x and high to output|bot y
        bot = int(instruction_parts[1])

        if bot not in bots:
            print "Bot {} is not holding anything, so cannot compare.".format(bot)
            continue

        bot_hands = bots[bot]

        if len(bot_hands) < 2:
            print "Bot {} is not holding enough, so cannot compare.".format(bot)
            continue

        low_17 = False
        high_61 = False
        if instruction_parts[5] == 'bot':
            other_bot = int(instruction_parts[6])
            low = min(bot_hands)
            low_17 = low == 17
            bot_hands.remove(low)
            give_bot(bots, other_bot, low)
            transfer_instructions[i - 1] = []
            print "Bot {} gave (low) {} to bot {}; "\
                  "now the first bot has {} and the second has {}.".format(
                    bot, low, other_bot, bots[bot], bots[other_bot])

        if instruction_parts[-2] == 'bot':
            other_bot = int(instruction_parts[-1])
            high = max(bot_hands)
            high_61 = high == 61
            bot_hands.remove(high)
            give_bot(bots, other_bot, high)
            transfer_instructions[i - 1] = []
            print "Bot {} gave (high) {} to bot {}; "\
                  "now the first bot has {} and the second has {}.".format(
                    bot, high, other_bot, bots[bot], bots[other_bot])

        if low_17 and high_61:
            print "***The bot responsible for comparing value-17 and value-61 microchips is {}.***".format(bot)
            break



def part_two():
    pass

if __name__ == '__main__':
    part_one()
    part_two()
