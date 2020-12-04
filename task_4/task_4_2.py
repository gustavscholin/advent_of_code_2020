import re


def read_input(path):
    output = []
    with open(path, 'r') as f:
        input_lines = f.read().split('\n\n')
    for line in input_lines:
        line = line.split()
        output.append({i.split(':')[0]: i.split(':')[1] for i in line})
    return output


def year_check(year_str, min, max):
    return year_str.isnumeric() and (min <= int(year_str) <= max)


def check_height(height_str):
    value = height_str[:-2]
    unit = height_str[-2:]
    if unit == 'cm':
        return value.isnumeric() and (150 <= int(value) <= 193)
    elif unit == 'in':
        return value.isnumeric() and (59 <= int(value) <= 76)
    return False


def check_hair(hair_str):
    if re.fullmatch(r'#[0-9a-f]{6}', hair_str):
        return True
    return False


def check_passport_id(id_str):
    return id_str.isnumeric() and len(id_str) == 9


def check_eye(eye_str):
    return eye_str in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


if __name__ == '__main__':
    credentials = read_input('input.txt')
    mandatory_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passport_count = 0

    for credential in credentials:
        if not all(key in credential.keys() for key in mandatory_keys):
            continue
        if not year_check(credential['byr'], 1920, 2002):
            continue
        if not year_check(credential['iyr'], 2010, 2020):
            continue
        if not year_check(credential['eyr'], 2020, 2030):
            continue
        if not check_height(credential['hgt']):
            continue
        if not check_hair(credential['hcl']):
            continue
        if not check_eye(credential['ecl']):
            continue
        if not check_passport_id(credential['pid']):
            continue
        valid_passport_count += 1

    print(valid_passport_count)
