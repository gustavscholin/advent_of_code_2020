if __name__ == '__main__':
    cups = [6, 5, 3, 4, 2, 7, 9, 1, 8]
    full_len = 1000000
    rounds = 10000000

    linked_cups = {}
    for i in range(full_len):
        if i < len(cups) - 1:
            linked_cups[cups[i]] = cups[i + 1]
        elif i == len(cups) - 1:
            linked_cups[cups[i]] = len(cups) + 1 if full_len > len(cups) else cups[0]
        elif i == full_len - 1:
            linked_cups[full_len] = cups[0]
        else:
            linked_cups[i + 1] = i + 2

    current = cups[0]

    for _ in range(rounds):
        c1 = linked_cups[current]
        c2 = linked_cups[c1]
        c3 = linked_cups[c2]
        linked_cups[current] = linked_cups[c3]

        destination = ((current - 2) % full_len) + 1
        while destination in [c1, c2, c3]:
            destination = ((destination - 2) % full_len) + 1

        linked_cups[c3] = linked_cups[destination]
        linked_cups[destination] = c1

        current = linked_cups[current]

    print(linked_cups[1] * linked_cups[linked_cups[1]])
