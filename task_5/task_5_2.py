import math


def read_input(path):
    with open(path, 'r') as f:
        output = f.read().splitlines()
    return output


# binary space partitioning
def bsp(code, max_idx, low_char, high_char):
    span = (0, max_idx)
    for code_char in code:
        mid_point = (span[1] - span[0]) / 2 + span[0]
        if code_char == low_char:
            span = (span[0], math.floor(mid_point))
        elif code_char == high_char:
            span = (math.ceil(mid_point), span[1])
    assert span[0] == span[1]
    return span[0]


if __name__ == '__main__':
    seat_codes = read_input('input.txt')
    seat_ids = []

    for seat_code in seat_codes:
        row_code = seat_code[:7]
        column_code = seat_code[7:]
        row = bsp(row_code, 127, 'F', 'B')
        column = bsp(column_code, 7, 'L', 'R')
        seat_ids.append(row * 8 + column)

    seat_ids.sort()
    for i in range(len(seat_ids) - 1):
        if seat_ids[i + 1] != seat_ids[i] + 1:
            print(seat_ids[i] + 1)
            break
