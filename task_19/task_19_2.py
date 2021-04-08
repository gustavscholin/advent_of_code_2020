from itertools import product


def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n\n')


def expand_rule(rule_idx):
    if isinstance(rules[rule_idx], set):
        return rules[rule_idx]
    elif rules[rule_idx][0].isnumeric():
        sets = []
        for children in rules[rule_idx].split(' | '):
            expanded_children = [expand_rule(child) for child in children.split()]
            valid_messages = {''.join(message) for message in product(*expanded_children)}
            sets.append(valid_messages)
        return set.union(*sets)
    else:
        rules[rule_idx] = set(rules[rule_idx].strip('"'))
        return rules[rule_idx]


if __name__ == '__main__':
    rules_str, messages_str = read_input('input.txt')
    rules = {rule.split(':')[0]: rule.split(': ')[1] for rule in rules_str.splitlines()}
    messages = messages_str.splitlines()
    valid_messages_42 = expand_rule('42')
    valid_messages_31 = expand_rule('31')

    assert len({len(s) for s in valid_messages_42}) == 1
    len_42_part = len(list(valid_messages_42)[0])
    assert len({len(s) for s in valid_messages_31}) == 1
    len_31_part = len(list(valid_messages_31)[0])

    valid_messages_cnt = 0
    for message in messages:
        idx = 0
        cnt_42_part = 0
        cnt_31_part = 0
        while idx + len_42_part <= len(message):
            if not message[idx:idx + len_42_part] in valid_messages_42:
                break
            cnt_42_part += 1
            idx += len_42_part
        while idx + len_31_part <= len(message):
            if not message[idx:idx + len_31_part] in valid_messages_31:
                break
            cnt_31_part += 1
            idx += len_31_part
        if idx == len(message) and (0 < cnt_31_part < cnt_42_part):
            valid_messages_cnt += 1

    print(valid_messages_cnt)
