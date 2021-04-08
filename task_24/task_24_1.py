import re
import numpy as np


def read_input(path):
    with open(path, 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    sequences = read_input('input.txt')
    tiles = {}
    dirs = {
        'e': np.array([1, -1, 0]),
        'se': np.array([0, -1, 1]),
        'sw': np.array([-1, 0, 1]),
        'w': np.array([-1, 1, 0]),
        'nw': np.array([0, 1, -1]),
        'ne': np.array([1, 0, -1])
    }

    for sequence in sequences:
        coord = np.array([0, 0, 0])
        instructions = re.findall(r'e|se|sw|w|nw|ne', sequence)
        for inst in instructions:
            coord += dirs[inst]

        coord = tuple(coord)
        if not tiles.get(coord):
            tiles[coord] = 'b'
        else:
            tiles[coord] = 'b' if tiles[coord] == 'w' else 'w'

    print(list(tiles.values()).count('b'))