import re


def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n\n')[:-1]


def get_tile_borders(tiles):
    tile_borders = {}
    for tile_str in tiles:
        tile = tile_str.splitlines()
        tile_id = int(re.search('\d+', tile[0]).group())
        top = tile[1]
        bottom = tile[-1]
        left = ''.join([s[0] for s in tile[1:]])
        right = ''.join([s[-1] for s in tile[1:]])
        tile_borders[tile_id] = (top, bottom, left, right)
    return tile_borders


if __name__ == '__main__':
    tiles = read_input('input.txt')
    tile_borders = get_tile_borders(tiles)
    all_borders = [border for tile in tile_borders.values() for border in tile]
    corner_tile_id_product = 1
    for tile_id, borders in tile_borders.items():
        edge_borders = 0
        for border in borders:
            if all_borders.count(border) + all_borders.count(border[::-1]) == 1:
                edge_borders += 1
        if edge_borders == 2:
            corner_tile_id_product *= tile_id
    print(corner_tile_id_product)
