def read_input(path):
    with open(path, 'r') as f:
        player_1, player_2 = f.read().split('\n\n')
        player_1 = [int(i) for i in player_1.splitlines()[1:]]
        player_2 = [int(i) for i in player_2.splitlines()[1:]]
        return player_1, player_2


if __name__ == '__main__':
    player_1, player_2 = read_input('input.txt')
    while player_1 and player_2:
        card_1, card_2 = player_1.pop(0), player_2.pop(0)
        if card_1 > card_2:
            player_1.extend([card_1, card_2])
        else:
            player_2.extend([card_2, card_1])

    winner = player_1 if player_1 else player_2
    print(sum([card * (idx + 1) for idx, card in enumerate(winner[::-1])]))
