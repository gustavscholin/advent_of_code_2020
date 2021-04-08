if __name__ == '__main__':
    starting_nbrs = [0, 1, 4, 13, 15, 12, 16]
    spoken_nbrs = {nbr: turn for turn, nbr in enumerate(starting_nbrs[:-1])}
    last_spoken = starting_nbrs[-1]
    for turn in range(len(starting_nbrs) - 1, 2019):
        if spoken_nbrs.get(last_spoken) is None:
            next_spoken = 0
        else:
            next_spoken = turn - spoken_nbrs[last_spoken]
        spoken_nbrs[last_spoken] = turn
        last_spoken = next_spoken

    print(last_spoken)
