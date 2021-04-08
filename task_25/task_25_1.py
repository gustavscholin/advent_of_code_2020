def read_input(path):
    with open(path, 'r') as f:
        return [int(i) for i in f.read().splitlines()]


def transform(value, subject_nbr):
    return (value * subject_nbr) % 20201227


if __name__ == '__main__':
    card_pub_key, door_pub_key = read_input('input.txt')

    value = 1
    loop_size = 0
    while value != card_pub_key:
        value = transform(value, 7)
        loop_size += 1

    value = 1
    for _ in range(loop_size):
        value = transform(value, door_pub_key)

    print(value)
