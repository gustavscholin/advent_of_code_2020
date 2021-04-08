from copy import deepcopy


def read_input(path):
    with open(path, 'r') as f:
        output = [{'op': line.split()[0], 'arg': int(line.split()[1])} for line in f.read().splitlines()]
    return output


def check_terminable(instructions):
    read_indices = set()
    pointer = 0
    accum = 0
    while pointer not in read_indices and pointer != len(instructions):
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
    return pointer == len(instructions), accum


if __name__ == '__main__':
    instructions = read_input('input.txt')
    accum = None
    for i in range(len(instructions)):
        if instructions[i]['op'] in ('jmp', 'nop'):
            mod_instructions = deepcopy(instructions)
            mod_instructions[i]['op'] = 'jmp' if instructions[i]['op'] == 'nop' else 'nop'
            terminable, accum = check_terminable(mod_instructions)
            if terminable:
                break

    print(accum)
