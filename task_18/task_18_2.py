import re


def read_input(path):
    with open(path, 'r') as f:
        return f.read().splitlines()


def get_parentheses_indices(expression):
    stack = 0
    start_idx = None
    end_idx = None

    for i, c in enumerate(expression):
        if c == '(':
            if stack == 0:
                start_idx = i
            stack += 1
        elif c == ')':
            stack -= 1
            if stack == 0:
                end_idx = i
                break
    return start_idx, end_idx


def evaluate_expression(expression):
    if '(' in expression:
        start, end = get_parentheses_indices(expression)
        evaluated_parenthesis = evaluate_expression(expression[start + 1:end])
        return evaluate_expression(expression[:start] + str(evaluated_parenthesis) + expression[end + 1:])
    else:
        while not expression.isnumeric():
            match = re.search('\d+ [\+] \d+', expression)
            if not match:
                match = re.search('\d+ [\*] \d+', expression)
            expression = expression[:match.start()] + str(eval(match.group())) + expression[match.end():]
        return int(expression)


if __name__ == '__main__':
    homework = read_input('input.txt')
    print(sum([evaluate_expression(expression) for expression in homework]))
