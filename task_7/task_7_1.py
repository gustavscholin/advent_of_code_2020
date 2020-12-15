def find_bag(rules, bag_color, find_color, incl_bag_list, excl_bag_list):
    if bag_color in incl_bag_list:
        return True
    if bag_color in excl_bag_list:
        return False
    if find_color in rules[bag_color]['children_colors']:
        incl_bag_list.append(bag_color)
        return True
    if not rules[bag_color]['children_colors']:
        excl_bag_list.append(bag_color)
        return False
    if any([find_bag(rules, child_color, find_color, incl_bag_list, excl_bag_list) for child_color in
                rules[bag_color]['children_colors']]):
        incl_bag_list.append(bag_color)
        return True
    else:
        excl_bag_list.append(bag_color)
        return False


def read_input(path):
    output = {}
    with open(path, 'r') as f:
        for line in f.read().splitlines():
            color, children_colors, child_cnts = parse_rule(line)
            output[color] = {'children_colors': children_colors, 'child_cnts': child_cnts}
    return output


def parse_rule(rule_str):
    rule_split = rule_str.split(' bags contain ')
    color = rule_split[0]
    child_colors = []
    child_cnts = []
    if rule_split[1] != 'no other bags.':
        childs = rule_split[1].split(', ')
        child_colors = [' '.join(child.split()[1:3]) for child in childs]
        child_cnts = [int(child.split()[0]) for child in childs]
    return color, child_colors, child_cnts


if __name__ == '__main__':
    rules = read_input('input.txt')
    incl_bag_list = []
    excl_bag_list = []
    for color in rules.keys():
        find_bag(rules, color, 'shiny gold', incl_bag_list, excl_bag_list)
    print(len(incl_bag_list))
