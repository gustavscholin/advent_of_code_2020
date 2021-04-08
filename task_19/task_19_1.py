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
    rules_str, messages_str = read_input('light_input.txt')
    rules = {rule.split(':')[0]: rule.split(': ')[1] for rule in rules_str.splitlines()}
    messages = messages_str.splitlines()
    valid_messages_zero = expand_rule('0')
    print(len(set.intersection(valid_messages_zero, set(messages))))
