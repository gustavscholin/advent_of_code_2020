def read_input(path):
    with open(path, 'r') as f:
        output = tuple(f.read().splitlines())
    return output


if __name__ == '__main__':
    eta, bus_ids = read_input('input.txt')
    bus_ids = bus_ids.split(',')
    bus_ids = [int(bus_id) for bus_id in list(filter(lambda s: s != 'x', bus_ids))]
    wait_times = [bus_id - (int(eta) % bus_id) for bus_id in bus_ids]
    print(min(wait_times) * bus_ids[wait_times.index(min(wait_times))])

