def read_input(path):
    output = []
    with open(path, 'r') as f:
        input_lines = f.read().split('\n\n')
    for line in input_lines:
        line = line.split()
        output.append({i.split(':')[0]: i.split(':')[1] for i in line})
    return output


if __name__ == '__main__':
    credentials = read_input('input.txt')
    mandatory_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passport_count = 0

    for credential in credentials:
        if all(key in credential.keys() for key in mandatory_keys):
            valid_passport_count += 1

    print(valid_passport_count)
