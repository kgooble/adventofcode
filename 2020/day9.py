PREAMBLE_LENGTH = 25
NUM_NUMS_TO_CONSIDER = 25

def part_1(numbers):
    for i in range (PREAMBLE_LENGTH, len(numbers)):
        prev_numbers = numbers[(i - NUM_NUMS_TO_CONSIDER):i]
        cur_num = numbers[i]
        found = False
        for j in range(0, NUM_NUMS_TO_CONSIDER):
            for k in range(j, NUM_NUMS_TO_CONSIDER):
                if prev_numbers[j] + prev_numbers[k] == cur_num:
                    found = True
                    break
            if found:
                break

        if not found:
            return cur_num

def part_2(numbers, invalid_number):
    for i in range(len(numbers)):
        total_sum = numbers[i]
        contiguous_set = [numbers[i]]
        for j in range(i + 1, len(numbers)):
            total_sum += numbers[j]
            contiguous_set.append(numbers[j])
            if total_sum > invalid_number:
                break
            elif total_sum == invalid_number:
                contiguous_set.sort()
                return contiguous_set[0] + contiguous_set[-1]

if __name__ == '__main__':
    f = open('input_day9')

    numbers = []
    for line in f:
        numbers.append(int(line.strip()))

    invalid_number = part_1(numbers)

    print(f"Part 1: The first invalid number is {invalid_number}")

    encryption_weakness = part_2(numbers, invalid_number)

    print(f"Part 2: The encryption weakness is {encryption_weakness}")

    f.close()
