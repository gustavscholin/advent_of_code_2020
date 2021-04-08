import re
import numpy as np
from copy import deepcopy


def read_input(path):
    with open(path, 'r') as f:
        return f.read().splitlines()


def add_neighbours(coord, tiles):
    for direction in dirs.values():
        neighbour_coord = tuple(coord + direction)
        if not tiles.get(neighbour_coord):
            tiles[neighbour_coord] = 'w'


def get_neighbours(coord, tiles):
    neighbours = []
    for direction in dirs.values():
        neighbour_coord = tuple(coord + direction)
        neighbours.append(tiles.get(neighbour_coord))
    return neighbours


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

        add_neighbours(coord, tiles)

        coord = tuple(coord)
        if not tiles.get(coord):
            tiles[coord] = 'b'
        else:
            tiles[coord] = 'b' if tiles[coord] == 'w' else 'w'

    print(list(tiles.values()).count('b'))

    for _ in range(100):
        tiles_copy = deepcopy(tiles)
        for coord in tiles.keys():
            neighbours = get_neighbours(coord, tiles)
            if tiles[coord] == 'b' and (neighbours.count('b') == 0 or neighbours.count('b') > 2):
                tiles_copy[coord] = 'w'
            elif tiles[coord] == 'w' and neighbours.count('b') == 2:
                tiles_copy[coord] = 'b'
                add_neighbours(coord, tiles_copy)

        tiles = tiles_copy

    print(list(tiles.values()).count('b'))
