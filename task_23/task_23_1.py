if __name__ == '__main__':
    cups = [6, 5, 3, 4, 2, 7, 9, 1, 8]
    max_label = max(cups)
    min_label = min(cups)
    current = cups[0]

    dest_indices = []

    for _ in range(100):
        taken = [cups.pop((cups.index(current) + 1) % len(cups)) for _ in range(3)]

        destination = current - 1 if current - 1 >= min_label else max_label
        while destination in taken:
            destination = destination - 1 if destination - 1 >= min_label else max_label

        destination_idx = cups.index(destination)
        dest_indices.append(destination_idx)
        insert_idx = (destination_idx + 1) % len(cups)
        cups[insert_idx:insert_idx] = taken

        current = cups[(cups.index(current) + 1) % len(cups)]

    while cups[0] != 1:
        cups.append(cups.pop(0))

    print(''.join([str(i) for i in cups[1:]]))
