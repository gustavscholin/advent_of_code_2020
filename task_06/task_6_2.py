def read_input(path):
    output = []
    with open(path, 'r') as f:
        for line_group in f.read().split('\n\n'):
            output.append([set(line) for line in line_group.splitlines()])
    return output


if __name__ == '__main__':
    groups = read_input('input.txt')
    print(sum([len(set.intersection(*group)) for group in groups]))
