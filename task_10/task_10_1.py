def read_input(path):
    with open(path, 'r') as f:
        output = [int(i) for i in f.read().splitlines()]
    return output


if __name__ == '__main__':
    adapters = read_input('input.txt')
    adapters.sort()
    comp_jolt = max(adapters) + 3
    outlet_jolt = 0
    jolts = [outlet_jolt, *adapters, comp_jolt]
    jolts_diff = [j-i for i, j in zip(jolts[:-1], jolts[1:])]
    print(jolts_diff.count(1) * jolts_diff.count(3))
