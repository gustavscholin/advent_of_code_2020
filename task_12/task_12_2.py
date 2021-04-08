import numpy as np


def read_input(path):
    with open(path, 'r') as f:
        output = f.read().splitlines()
    return output


def get_dir(deg):
    x_dir = np.cos(np.radians(deg))
    y_dir = np.sin(np.radians(deg))
    return np.array([x_dir, y_dir])


def get_rot_mat(deg):
    rad = np.radians(deg)
    return np.array([[np.cos(rad), -np.sin(rad)],
                     [np.sin(rad), np.cos(rad)]])


if __name__ == '__main__':
    instructions = read_input('input.txt')
    way_point = np.array([10, 1])
    pos = np.zeros(2)
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action == 'N':
            way_point += np.array([0, 1]) * value
        elif action == 'S':
            way_point += np.array([0, -1]) * value
        elif action == 'E':
            way_point += np.array([1, 0]) * value
        elif action == 'W':
            way_point += np.array([-1, 0]) * value
        elif action == 'L':
            rot_mat = get_rot_mat(value)
            way_point = np.matmul(rot_mat, way_point)
        elif action == 'R':
            rot_mat = get_rot_mat(-value)
            way_point = np.matmul(rot_mat, way_point)
        elif action == 'F':
            pos += way_point * value

    print(np.sum(np.abs(pos).round()))
