import re
from copy import deepcopy


def read_input(path):
    with open(path, 'r') as f:
        return f.read().splitlines()


def get_idx_bins(masked_idx_bin, idx_bins):
    if 'X' in masked_idx_bin:
        x_idx = masked_idx_bin.index('X')
        masked_idx_bin[x_idx] = '0'
        get_idx_bins(deepcopy(masked_idx_bin), idx_bins)
        masked_idx_bin[x_idx] = '1'
        get_idx_bins(deepcopy(masked_idx_bin), idx_bins)
        return idx_bins
    else:
        idx_bins.append(masked_idx_bin)
        return idx_bins


if __name__ == '__main__':
    program = read_input('input.txt')
    mem = {}
    mask = None
    for line in program:
        if line[:4] == 'mask':
            mask = line.split(' = ')[-1]
        else:
            idx, val = [int(i) for i in re.findall('\d+', line)]
            idx_bin = '{:036b}'.format(idx)
            masked_idx_bin = []
            for j in range(36):
                if mask[j] == '0':
                    masked_idx_bin.append(idx_bin[j])
                elif mask[j] == '1':
                    masked_idx_bin.append('1')
                elif mask[j] == 'X':
                    masked_idx_bin.append('X')

            idx_bins = []
            idx_bins = get_idx_bins(masked_idx_bin, idx_bins)

            for idx_bin in idx_bins:
                mem[int(''.join(idx_bin), 2)] = val

    print(sum(mem.values()))
