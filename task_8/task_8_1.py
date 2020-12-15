def read_input(path):
    with open(path, 'r') as f:
        output = [{'op': line.split()[0], 'arg': int(line.split()[1])} for line in f.read().splitlines()]
    return output


if __name__ == '__main__':
    instructions = read_input('input.txt')
    read_indices = set()
    pointer = 0
    accum = 0
    while pointer not in read_indices:
        read_indices.add(pointer)
        op = instructions[pointer]['op']
        arg = instructions[pointer]['arg']
        if op == 'acc':
            accum += arg
            pointer += 1
        elif op == 'jmp':
            pointer += arg
        elif op == 'nop':
            pointer += 1
    print(accum)
