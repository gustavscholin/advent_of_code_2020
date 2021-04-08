import re
from functools import reduce


def read_input(path):
    with open(path, 'r') as f:
        return [lines.splitlines() for lines in f.read().split('\n\n')]


def abide_any_rule(nbr):
    for rule in field_rules:
        for span in rule:
            if span[0] <= nbr <= span[1]:
                return True
    return False


def is_valid_ticket(ticket):
    for nbr in ticket:
        nbr = int(nbr)
        if not abide_any_rule(nbr):
            return False
    return True


def field_vals_abide_rule(field_vals, rule):
    for val in field_vals:
        if not any([span[0] <= val <= span[1] for span in rule]):
            return False
    return True


if __name__ == '__main__':
    field_rules, my_ticket, nearby_tickets = read_input('input.txt')
    my_ticket = [int(val) for val in my_ticket[1].split(',')]
    field_rules = [[[int(edge) for edge in span.split('-')] for span in re.findall('\d+-\d+', rule)] for rule in
                   field_rules]
    nearby_tickets = [ticket.split(',') for ticket in nearby_tickets[1:]]
    valid_tickets = []
    for nearby_ticket in nearby_tickets:
        if is_valid_ticket(nearby_ticket):
            valid_tickets.append(nearby_ticket)

    valid_field_rules = {}
    for field_idx in range(len(field_rules)):
        field_vals = [int(valid_ticket[field_idx]) for valid_ticket in valid_tickets]
        valid_field_rules[field_idx] = []
        for rule_idx, rule in enumerate(field_rules):
            if field_vals_abide_rule(field_vals, rule):
                valid_field_rules[field_idx].append(rule_idx)

    field_mapping = {}
    while valid_field_rules:
        for field in valid_field_rules.keys():
            if len(valid_field_rules[field]) == 1:
                rule = valid_field_rules.pop(field)[0]
                break
        field_mapping[rule] = field
        for field_rules in valid_field_rules.values():
            field_rules.remove(rule)

    departure_vals = [my_ticket[field_mapping[i]] for i in range(6)]
    print(reduce(lambda x, y: x * y, departure_vals))
