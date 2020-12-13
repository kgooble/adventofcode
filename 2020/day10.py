def part_1(adapters):
    one_diff_count = 0
    three_diff_count = 0
    current_voltage = 0

    for i in range(len(adapters)):
        adapter = adapters[i]
        diff = adapter - current_voltage
        if diff == 1:
            one_diff_count += 1
        elif diff == 3:
            three_diff_count += 1
        elif diff > 3:
            raise Error(f"Unexpected difference of {diff}")
        current_voltage = adapter

    three_diff_count += 1
    print(f"The multiplication is {one_diff_count * three_diff_count}")

def count_choices(current_index, choices, cached_choice_count):
    total_num_choices = 0
    if current_index == len(choices) - 1:
        return 1

    current_choice = 0 if current_index < 0 else choices[current_index]
    for i in range(1, 4):
        next_index = current_index + i
        if next_index < len(choices) and choices[next_index] <= current_choice + 3:
            if next_index in cached_choice_count:
                total_num_choices += cached_choice_count[next_index]
            else:
                num_choices = count_choices(next_index, choices, cached_choice_count)
                total_num_choices += num_choices
                cached_choice_count[next_index] = num_choices

    return total_num_choices

def part_2(adapters):
    print(adapters)
    total_num_choices = count_choices(-1, adapters, {});
    print(f"Total num choices {total_num_choices}")

if __name__ == '__main__':
    f = open('input_day10')

    adapters = []
    for line in f:
        adapters.append(int(line.strip()))

    adapters.sort()

    part_1(adapters)
    part_2(adapters)

    f.close()
