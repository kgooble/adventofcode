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
            print 'succeded on:' , i
            print 'got:', hex_code, hex_code[5]
            password += hex_code[5]
            if len(password) == 8:
                break

        i += 1

    print "The password is {}.".format(password)

def part_two():
    pass

if __name__ == '__main__':
    part_one()
    part_two()
