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
            firsts = get_firsts(seat_map, x, y)
            if seat_map[y][x] == 'L' and all(seat != '#' for seat in firsts):
                to_occupy.append((x, y))
            elif seat_map[y][x] == '#' and firsts.count('#') >= 5:
                to_free.append((x, y))
    for x, y in to_occupy:
        seat_map[y][x] = '#'
    for x, y in to_free:
        seat_map[y][x] = 'L'
    return seat_map


def get_firsts(seat_map, x, y):
    firsts = []
    for x_rel, y_rel in [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]:
        dist = 1
        while 0 <= x + x_rel * dist < width and 0 <= y + y_rel * dist < length:
            if seat_map[y + y_rel * dist][x + x_rel * dist] != '.':
                firsts.append(seat_map[y + y_rel * dist][x + x_rel * dist])
                break
            dist += 1
    return firsts


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