from itertools import combinations


def read_input(path):
    with open(path, 'r') as f:
        output = [int(i) for i in f.read().splitlines()]
    return output


if __name__ == '__main__':
    stream = read_input('input.txt')
    preamble_len = 25
    invalid_nbr = None
    for i in range(preamble_len, len(stream)):
        valid_sum = False
        preamble = stream[i - preamble_len:i]
        for int_1, int_2 in combinations(preamble, 2):
            if int_1 + int_2 == stream[i]:
                valid_sum = True
                break
        if not valid_sum:
            invalid_nbr = stream[i]
            break
    print(invalid_nbr)


