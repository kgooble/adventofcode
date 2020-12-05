def part1(rule, text):
    rule_parts = rule.split(' ')
    min_letters, max_letters = rule_parts[0].split('-')
    min_letters = int(min_letters)
    max_letters = int(max_letters)
    letter = rule_parts[1]

    num_letters_found = 0
    for ch in text:
        if ch == letter:
            num_letters_found += 1

    return num_letters_found >= min_letters and num_letters_found <= max_letters

def part2(rule, text):
    rule_parts = rule.split(' ')
    index_1, index_2 = rule_parts[0].split('-')
    index_1 = int(index_1) - 1
    index_2 = int(index_2) - 1
    letter = rule_parts[1]

    if text[index_1] == letter and text[index_2] != letter:
        return True

    if text[index_1] != letter and text[index_2] == letter:
        return True

    return False

if __name__ == '__main__':
    f = open("input_day2")

    num_valid_passwords_part1 = 0
    num_valid_passwords_part2 = 0

    for line in f:
        parts = line.strip().split(': ')
        rule = parts[0]
        text = parts[1]

        if part1(rule, text):
            num_valid_passwords_part1 += 1

        if part2(rule, text):
            num_valid_passwords_part2 += 1


    print("Number of valid passwords part 1: " + str(num_valid_passwords_part1))
    print("Number of valid passwords part 2: " + str(num_valid_passwords_part2))
    f.close()
