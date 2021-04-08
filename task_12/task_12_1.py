import numpy as np


def read_input(path):
    with open(path, 'r') as f:
        output = f.read().splitlines()
    return output


def get_dir(deg):
    x_dir = np.cos(np.radians(deg))
    y_dir = np.sin(np.radians(deg))
    return np.array([x_dir, y_dir])


if __name__ == '__main__':
    instructions = read_input('input.txt')
    pos = np.zeros(2)
    deg = 0
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action == 'N':
            pos += np.array([0, 1]) * value
        elif action == 'S':
            pos += np.array([0, -1]) * value
        elif action == 'E':
            pos += np.array([1, 0]) * value
        elif action == 'W':
            pos += np.array([-1, 0]) * value
        elif action == 'L':
            deg += value
        elif action == 'R':
            deg -= value
        elif action == 'F':
            pos += get_dir(deg) * value

    print(np.sum(np.abs(pos).round()))

