import re


def read_input(path):
    with open(path, 'r') as f:
        return [lines.splitlines() for lines in f.read().split('\n\n')]


def rules_check(nbr):
    for rule in rules:
        for span in rule:
            if span[0] <= nbr <= span[1]:
                return True
    return False


if __name__ == '__main__':
    rules, _, nearby_tickets = read_input('input.txt')
    rules = [[[int(edge) for edge in span.split('-')] for span in re.findall('\d+-\d+', rule)] for rule in rules]
    nearby_tickets = [ticket.split(',') for ticket in nearby_tickets[1:]]
    invalid_vals = []
    for nearby_ticket in nearby_tickets:
        for nbr in nearby_ticket:
            nbr = int(nbr)
            if not rules_check(nbr):
                invalid_vals.append(nbr)
                break
    print(sum(invalid_vals))
