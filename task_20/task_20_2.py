import re


def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n\n')[:-1]


def get_tiles(tile_strs):
    tiles = {}
    for tile_str in tile_strs:
        tile = tile_str.splitlines()
        tile_id = int(re.search('\d+', tile[0]).group())
        tiles[tile_id] = tile[1:]
    return tiles


def remove_borders(tile):
    return [r[1:-1] for r in tile[1:-1]]


def get_borders(tile):
    top = tile[0]
    bottom = tile[-1]
    left = ''.join([s[0] for s in tile])
    right = ''.join([s[-1] for s in tile])
    return [top, right, bottom, left]


def get_start_tile():
    for tile_id, tile in tiles.items():
        borders = get_borders(tile)
        edge_border_indices = []
        for idx, border in enumerate(borders):
            if all_borders.count(border) + all_borders.count(border[::-1]) == 1:
                edge_border_indices.append(idx)
        if len(edge_border_indices) == 2:
            if 2 in edge_border_indices:
                tiles[tile_id] = vflip(tiles[tile_id])
            if 1 in edge_border_indices:
                tiles[tile_id] = hflip(tiles[tile_id])
            return tile_id


def hflip(tile):
    return [r[::-1] for r in tile]


def vflip(tile):
    return tile[::-1]


def rrot(tile):
    return [''.join(list(r)) for r in zip(*tile[::-1])]


def lrot(tile):
    return [''.join(list(r)) for r in zip(*tile)][::-1]


def find_sea_monster(row1, row2, row3):
    row1 = list(row1)
    row2 = list(row2)
    row3 = list(row3)
    row1_indices = [18]
    row2_indices = [0, 5, 6, 11, 12, 17, 18, 19]
    row3_indices = [1, 4, 7, 10, 13, 16]
    for i in range(len(row1) - 19):
        row_matches = [
            all([row1[i + j] in '#O' for j in row1_indices]),
            all([row2[i + j] in '#O' for j in row2_indices]),
            all([row3[i + j] in '#O' for j in row3_indices])
        ]
        if all(row_matches):
            for idx in row1_indices:
                row1[i + idx] = 'O'
            for idx in row2_indices:
                row2[i + idx] = 'O'
            for idx in row3_indices:
                row3[i + idx] = 'O'
    return ''.join(row1), ''.join(row2), ''.join(row3)


if __name__ == '__main__':
    tile_strings = read_input('input.txt')
    tiles = get_tiles(tile_strings)
    all_borders = [border for tile in tiles.values() for border in get_borders(tile)]
    matching_tile_id = get_start_tile()
    id_image = [[matching_tile_id]]
    image = [[remove_borders(tiles[matching_tile_id])]]
    matching_borders = get_borders(tiles.pop(matching_tile_id))
    right_matching_border = matching_borders[1]
    bottom_matching_border = matching_borders[2]
    while True:
        while True:
            match_found = False
            for tile_id, tile in tiles.items():
                borders = get_borders(tile)
                if right_matching_border in borders:
                    idx = borders.index(right_matching_border)
                    if idx == 0:
                        tiles[tile_id] = vflip(tiles[tile_id])
                        tiles[tile_id] = rrot(tiles[tile_id])
                    elif idx == 1:
                        tiles[tile_id] = hflip(tiles[tile_id])
                    elif idx == 2:
                        tiles[tile_id] = rrot(tiles[tile_id])
                    match_found = True
                    break
                elif right_matching_border[::-1] in borders:
                    idx = borders.index(right_matching_border[::-1])
                    if idx == 0:
                        tiles[tile_id] = lrot(tiles[tile_id])
                    elif idx == 1:
                        tiles[tile_id] = vflip(tiles[tile_id])
                        tiles[tile_id] = hflip(tiles[tile_id])
                    elif idx == 2:
                        tiles[tile_id] = vflip(tiles[tile_id])
                        tiles[tile_id] = lrot(tiles[tile_id])
                    elif idx == 3:
                        tiles[tile_id] = vflip(tiles[tile_id])
                    match_found = True
                    break

            if match_found:
                id_image[-1].append(tile_id)
                image[-1].append(remove_borders(tiles[tile_id]))
                right_matching_border = get_borders(tiles.pop(tile_id))[1]
            else:
                break

        match_found = False
        for tile_id, tile in tiles.items():
            borders = get_borders(tile)
            if bottom_matching_border in borders:
                idx = borders.index(bottom_matching_border)
                if idx == 1:
                    tiles[tile_id] = lrot(tiles[tile_id])
                elif idx == 2:
                    tiles[tile_id] = vflip(tiles[tile_id])
                elif idx == 3:
                    tiles[tile_id] = hflip(tiles[tile_id])
                    tiles[tile_id] = lrot(tiles[tile_id])
                match_found = True
                break
            elif bottom_matching_border[::-1] in borders:
                idx = borders.index(bottom_matching_border[::-1])
                if idx == 0:
                    tiles[tile_id] = hflip(tiles[tile_id])
                elif idx == 1:
                    tiles[tile_id] = vflip(tiles[tile_id])
                    tiles[tile_id] = lrot(tiles[tile_id])
                elif idx == 2:
                    tiles[tile_id] = hflip(tiles[tile_id])
                    tiles[tile_id] = vflip(tiles[tile_id])
                elif idx == 3:
                    tiles[tile_id] = rrot(tiles[tile_id])
                match_found = True
                break

        if match_found:
            id_image.append([tile_id])
            image.append([remove_borders(tiles[tile_id])])
            matching_borders = get_borders(tiles.pop(tile_id))
            right_matching_border = matching_borders[1]
            bottom_matching_border = matching_borders[2]
        else:
            break

    formated_image = []
    for tile_row in image:
        for row in [''.join(r) for r in zip(*tile_row)]:
            formated_image.append(row)

    for _ in range(2):
        formated_image = hflip(formated_image)
        for _ in range(4):
            formated_image = lrot(formated_image)
            for i in range(len(formated_image) - 2):
                formated_image[i:i + 3] = find_sea_monster(*formated_image[i:i + 3])

    print(sum([row.count('#') for row in formated_image]))
