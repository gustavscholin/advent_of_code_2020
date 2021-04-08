from copy import deepcopy


def read_input(path):
    output = {}
    with open(path, 'r') as f:
        for j, line in enumerate(f.read().splitlines()):
            for i, val in enumerate(line):
                output[(i, j, 0, 0)] = val
    return output


def get_neighbors(coords, cubes):
    neighbors = {}
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            for z in (-1, 0, 1):
                for w in (-1, 0, 1):
                    offset_coords = (x, y, z, w)
                    if any(offset_coords):
                        neighbor_coords = tuple(sum(coord) for coord in zip(coords, offset_coords))
                        if not cubes.get(neighbor_coords):
                            neighbors[neighbor_coords] = '.'
                        else:
                            neighbors[neighbor_coords] = cubes[neighbor_coords]
    return neighbors


if __name__ == '__main__':
    cubes = read_input('input.txt')
    for cycle in range(6):
        for coords in list(cubes.keys()):
            neighbors = get_neighbors(coords, cubes)
            for neighbor_coords, neighbor_val in neighbors.items():
                if not cubes.get(neighbor_coords):
                    cubes[neighbor_coords] = neighbor_val

        new_cubes = deepcopy(cubes)
        for coords, val in cubes.items():
            neighbors = get_neighbors(coords, cubes)
            active_neighbors = list(neighbors.values()).count('#')
            if val == '#':
                if not 2 <= active_neighbors <= 3:
                    new_cubes[coords] = '.'
            elif val == '.' and active_neighbors == 3:
                new_cubes[coords] = '#'

        cubes = new_cubes

    print(list(cubes.values()).count('#'))
