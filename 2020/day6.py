def part1(f):
    current_answer_set = set()
    group_count_total = 0
    for line in f:
        line = line.strip()
        if len(line) == 0:
            group_count_total += len(current_answer_set)
            current_answer_set = set()
        else:
            answers = list(line)
            current_answer_set.update(answers)

    answers = list(line)
    current_answer_set.update(answers)
    group_count_total += len(current_answer_set)

    print(f"The sum of these sets is {group_count_total}")


def part2(f):
    current_answer_set = set()
    group_count_total = 0
    first_person = True
    f.seek(0)
    for line in f:
        line = line.strip()
        if len(line) == 0:
            group_count_total += len(current_answer_set)
            current_answer_set = set()
            first_person = True
        else:
            answers = set(line)
            if first_person:
                current_answer_set = answers
                first_person = False
            else:
                current_answer_set = current_answer_set.intersection(answers)

    answers = set(line)

    if first_person:
        current_answer_set = answers
    else:
        current_answer_set = current_answer_set.intersection(answers)

    group_count_total += len(current_answer_set)
    print(f"The sum of these sets is {group_count_total}")


if __name__ == '__main__':
    f = open('input_day6')

    part1(f)
    part2(f)

    f.close()
