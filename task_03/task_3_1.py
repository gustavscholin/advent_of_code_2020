class GrowingList(list):

    def __getitem__(self, index):
        while index >= len(self):
            self.extend(self * 2)
        return list.__getitem__(self, index)


def read_input(path):
    output = []
    with open(path, 'r') as f:
        for line in f.read().splitlines():
            output.append(GrowingList(line))
    return output


if __name__ == '__main__':
    map = read_input('input.txt')
    tree_count = 0
    slope = (3, 1)
    pos = (0, 0)

    while pos[1] < len(map):
        if map[pos[1]][pos[0]] == '#':
            tree_count += 1
        pos = (pos[0] + slope[0], pos[1] + slope[1])

    print(tree_count)
