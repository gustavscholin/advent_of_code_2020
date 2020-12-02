import re


def read_input(path):
    with open(path, 'r') as f:
        input_list = f.read().splitlines()
    return [re.split(r'\W+', i) for i in input_list]


def valid_idx(idx, pwd_char, pwd):
    return idx < len(pwd) and pwd[idx] == pwd_char


if __name__ == '__main__':
    pwds = read_input('input.txt')
    valid_pwds = 0
    for pwd in pwds:
        idx_1 = int(pwd[0]) - 1
        idx_2 = int(pwd[1]) - 1
        if valid_idx(idx_1, pwd[2], pwd[3]) != valid_idx(idx_2, pwd[2], pwd[3]):
            valid_pwds += 1

    print(valid_pwds)
