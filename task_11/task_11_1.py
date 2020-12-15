from copy import deepcopy


def read_input(path):
    with open(path, 'r') as f:
        output = [list(line) for line in f.read().splitlines()]
    return output


def sim_one_step(seat_map):
    to_occupy = []
    to_free = []
    for y in range(length):
        for x in range(width):
            if seat_map[y][x] == '.':
                continue
            adj = get_adj(seat_map, x, y)
            if seat_map[y][x] == 'L' and all(seat != '#' for seat in adj):
                to_occupy.append((x, y))
            elif seat_map[y][x] == '#' and adj.count('#') >= 4:
                to_free.append((x, y))
    for x, y in to_occupy:
        seat_map[y][x] = '#'
    for x, y in to_free:
        seat_map[y][x] = 'L'
    return seat_map


def get_adj(seat_map, x, y):
    adj = []
    for x_rel, y_rel in [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]:
        i = x + x_rel
        j = y + y_rel
        if 0 <= i < width and 0 <= j < length:
            adj.append(seat_map[j][i])
    return adj


if __name__ == '__main__':
    seat_map = read_input('input.txt')
    length = len(seat_map)
    width = len(seat_map[0])
    while True:
        old_seat_map = deepcopy(seat_map)
        seat_map = sim_one_step(seat_map)
        if old_seat_map == seat_map:
            break
    occupied_seats = 0
    for row in seat_map:
        occupied_seats += row.count('#')
    print(occupied_seats)
