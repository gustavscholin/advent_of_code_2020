import re


def read_input(path):
    with open(path, 'r') as f:
        input_list = f.read().splitlines()
    return [re.split(r'\W+', i) for i in input_list]


if __name__ == '__main__':
    pwds = read_input('input.txt')
    valid_pwds = 0
    for pwd in pwds:
        lower_bound = int(pwd[0])
        higher_bound = int(pwd[1])
        cnt = pwd[3].count(pwd[2])
        if lower_bound <= cnt <= higher_bound:
            valid_pwds += 1

    print(valid_pwds)
