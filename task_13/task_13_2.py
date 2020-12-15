import math


def read_input(path):
    vals = []
    indices = []
    with open(path, 'r') as f:
        for idx, val in enumerate(f.read().splitlines()[-1].split(',')):
            if val != 'x':
                vals.append(int(val))
                indices.append(idx)
    return vals, indices


def lcm(ints):
    result = ints[0]
    for integer in ints[1:]:
        result = result * integer // math.gcd(result, integer)
    return result


if __name__ == '__main__':
    bus_ids, deltas = read_input('input.txt')
    t = 0
    done_ids = [bus_ids[0]]
    period = lcm(done_ids)
    while True:
        nbr_done = len(done_ids)
        t += period

        for delta, bus_id in zip(deltas, bus_ids):
            if bus_id in done_ids:
                continue
            if (t + delta) % bus_id == 0:
                done_ids.append(bus_id)

        if len(done_ids) == len(bus_ids):
            break
        if len(done_ids) > nbr_done:
            period = lcm(list(done_ids))

    print(t)
