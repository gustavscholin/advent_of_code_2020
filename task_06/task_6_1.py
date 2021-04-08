def read_input(path):
    with open(path, 'r') as f:
        output = [s.replace('\n', '') for s in f.read().split('\n\n')]
    return output


if __name__ == '__main__':
    groups = read_input('input.txt')
    print(sum([len(set(group)) for group in groups]))
