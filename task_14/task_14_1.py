import re


def read_input(path):
    with open(path, 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    program = read_input('input.txt')
    mem = {}
    mask = None
    for line in program:
        if line[:4] == 'mask':
            mask = line.split(' = ')[-1]
        else:
            idx, val = [int(i) for i in re.findall('\d+', line)]
            val_bin = '{:036b}'.format(val)
            val_bin = ''.join([val_bin[i] if mask[i] == 'X' else mask[i] for i in range(36)])
            mem[idx] = int(val_bin, 2)

    print(sum(mem.values()))
