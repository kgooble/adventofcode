def part_1():
    for i in range (0, len(all_numbers)):
        for j in range (i + 1, len(all_numbers)):
            number_1 = all_numbers[i]
            number_2 = all_numbers[j]
            if number_1 + number_2 == 2020:
                print(number_1 * number_2)

def part_2():
    for i in range (0, len(all_numbers)):
        for j in range (i + 1, len(all_numbers)):
            for k in range (j + 1, len(all_numbers)):
                number_1 = all_numbers[i]
                number_2 = all_numbers[j]
                number_3 = all_numbers[k]
                if number_1 + number_2 + number_3 == 2020:
                    print(number_1 * number_2 * number_3)


if __name__ == '__main__':
    f = open("input_day1")

    all_numbers = []
    for line in f:
        number = int(line.strip())
        all_numbers.append(number)

    part_1()
    part_2()

    f.close()
