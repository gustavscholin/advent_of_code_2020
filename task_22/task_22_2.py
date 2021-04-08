def read_input(path):
    with open(path, 'r') as f:
        player_1, player_2 = f.read().split('\n\n')
        player_1 = [int(i) for i in player_1.splitlines()[1:]]
        player_2 = [int(i) for i in player_2.splitlines()[1:]]
        return player_1, player_2


def recursive_game(player_1, player_2):
    player_decks = set()
    while player_1 and player_2:
        if str(player_1) + str(player_2) in player_decks:
            return 1, player_1
        else:
            player_decks.add(str(player_1) + str(player_2))

        card_1, card_2 = player_1.pop(0), player_2.pop(0)
        if len(player_1) >= card_1 and len(player_2) >= card_2:
            winner, _ = recursive_game(player_1[:card_1], player_2[:card_2])
        elif card_1 > card_2:
            winner = 1
        else:
            winner = 2

        if winner == 1:
            player_1.extend([card_1, card_2])
        else:
            player_2.extend([card_2, card_1])

    return (1, player_1) if player_1 else (2, player_2)


if __name__ == '__main__':
    player_1, player_2 = read_input('input.txt')
    winner, deck = recursive_game(player_1, player_2)
    print(sum([card * (idx + 1) for idx, card in enumerate(deck[::-1])]))
