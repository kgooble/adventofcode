import re

if __name__ == '__main__':
    f = open('input_day14')


    address_space = { }
    current_mask = 'X' * 36
    for line in f:
        line = line.strip()
        if line.startswith('mask'):
            current_mask = line.split(' = ')[1]
        else:
            result = re.match('mem\[(\d+)\] = (\d+)', line)
            address = int(result.group(1))
            value = int(result.group(2))
            binary_value = list('{0:036b}'.format(value))

            # apply mask to value
            for i in range(0, len(current_mask)):
                current_mask_char = current_mask[i]
                new_value = binary_value[i]
                if current_mask_char != 'X':
                    new_value = current_mask_char
                binary_value[i] = new_value

            binary_value = ''.join(binary_value)

            # write to address
            address_space[address] = int(binary_value, 2)

    total = 0
    for val in address_space.values():
        total += val

    print(total)

    f.close()
