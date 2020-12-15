from collections import Counter


def read_input(path):
    with open(path, 'r') as f:
        output = [int(i) for i in f.read().splitlines()]
    return output


if __name__ == '__main__':
    adapters = read_input('input.txt')
    all_jolts = [*adapters, max(adapters) + 3]
    all_jolts.sort()
    cnt = Counter()
    cnt[0] = 1
    for jolt in all_jolts:
        cnt[jolt] = cnt[jolt - 1] + cnt[jolt - 2] + cnt[jolt - 3]
    print(cnt[all_jolts[-1]])
