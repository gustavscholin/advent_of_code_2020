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
    valid_contig_set = None
    for contig_set_len in range(2, len(stream) + 1):
        for i in range(contig_set_len - 1, len(stream)):
            contig_set = stream[i - contig_set_len - 1:i + 1]
            if sum(contig_set) == invalid_nbr:
                valid_contig_set = contig_set
                break
        if valid_contig_set:
            break
    print(min(valid_contig_set) + max(valid_contig_set))
