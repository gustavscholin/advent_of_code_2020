from itertools import combinations


def read_input(path):
    with open(path, 'r') as f:
        input_list = f.read().splitlines()
    return [int(i) for i in input_list]


if __name__ == '__main__':
    exp_rep = read_input('input.txt')
    prod = None
    for ent_1, ent_2, ent_3 in combinations(exp_rep, 3):
        if ent_1 + ent_2 + ent_3 == 2020:
            prod = ent_1 * ent_2 * ent_3

    print(prod)
