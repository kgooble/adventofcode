import re

REQUIRED_FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
VALID_EYE_COLORS = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def is_valid(passport):
    intersection = REQUIRED_FIELDS.intersection(passport.keys())
    valid = len(intersection) == len(REQUIRED_FIELDS)

    if not valid:
        return False

    for key, value in passport.items():
        if key == 'byr':
            year = int(value)
            if year < 1920 or year > 2002:
                print(f"Failed byr: {value} {year}")
                return False
        elif key == 'iyr':
            year = int(value)
            if year < 2010 or year > 2020:
                print(f"Failed iyr: {value} {year}")
                return False
        elif key == 'eyr':
            year = int(value)
            if year < 2020 or year > 2030:
                print(f"Failed eyr: {value} {year}")
                return False
        elif key == 'hgt':
            result = re.match('^([0-9]+)(in|cm)$', value)
            if result is None:
                print(f"Failed hgt: {value}")
                return False
            quantity = int(result.group(1))
            unit = result.group(2)
            if unit == 'cm' and (quantity < 150 or quantity > 193):
                print(f"Failed hgt centimetres: {value}")
                return False
            elif unit == 'in' and (quantity < 59 or quantity > 76):
                print(f"Failed hgt inches: {value}")
                return False
        elif key == 'hcl':
            if value[0] != '#':
                return False

            try:
                int(value[1:], 16)
            except ValueError:
                print(f"Failed hcl: {value}")
                return False
        elif key == 'ecl':
            if value not in VALID_EYE_COLORS:
                print(f"Failed ecl: {value}")
                return False
        elif key == 'pid':
            result = re.match('^[0-9]{9}$', value)
            if result is None:
                print(f"Failed pid: {value}")
                return False

    print(f"Passport was valid: {passport}")
    return valid

if __name__ == "__main__":
    f = open('input_day4')

    num_valid_passports = 0
    current_passport = {}
    for line in f:
        line = line.strip()
        if len(line) == 0:
            if is_valid(current_passport):
                num_valid_passports += 1
            current_passport = {}
        else:
            fields_in_current_line = line.split(' ')
            for field_key_value in fields_in_current_line:
                field_key, field_value = field_key_value.split(':')
                current_passport[field_key] = field_value

    if is_valid(current_passport):
        num_valid_passports += 1

    # 191 is too low
    print(f"Found {num_valid_passports} valid passports.")
    f.close()
