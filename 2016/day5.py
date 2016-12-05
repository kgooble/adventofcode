#!/usr/bin/env python

import hashlib

PUZZLE_INPUT = 'ojvtpuvg'

def part_one():
    password = ''
    i = 0
    while True:
        m = hashlib.md5()
        m.update(PUZZLE_INPUT + str(i))
        hex_code = m.hexdigest()

        if hex_code[:5] == '0' * 5:
            print 'succeeded on:' , i
            print 'got:', hex_code, hex_code[5]
            password += hex_code[5]
            if len(password) == 8:
                break

        i += 1

    print "The password is {}.".format(password)

def part_two():
    valid = [str(d) for d in range(0, 8)]
    parts = [None, None, None, None, None, None, None, None]
    i = 0
    while True:
        m = hashlib.md5()
        m.update(PUZZLE_INPUT + str(i))
        hex_code = m.hexdigest()

        if hex_code[:5] == '0' * 5 and hex_code[5] in valid and parts[int(hex_code[5])] is None:
            print 'succeeded on:' , i
            print 'got:', hex_code, hex_code[5], hex_code[6]
            parts[int(hex_code[5])] = hex_code[6]

            if all(part is not None for part in parts):
                break

        i += 1

    print "The password is {}.".format(''.join(parts))

if __name__ == '__main__':
    part_one()
    part_two()
