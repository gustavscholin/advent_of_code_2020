def bags_inside(rules, bag_color):
    children_colors = rules[bag_color]['children_colors']
    children_cnts = rules[bag_color]['children_cnts']
    if not rules[bag_color]['children_colors']:
        return 0
    else:
        return sum([child_cnt + child_cnt * bags_inside(rules, child_color) for child_color, child_cnt in
                    zip(children_colors, children_cnts)])


def read_input(path):
    output = {}
    with open(path, 'r') as f:
        for line in f.read().splitlines():
            color, children_colors, children_cnts = parse_rule(line)
            output[color] = {'children_colors': children_colors, 'children_cnts': children_cnts}
    return output


def parse_rule(rule_str):
    rule_split = rule_str.split(' bags contain ')
    color = rule_split[0]
    children_colors = []
    children_cnts = []
    if rule_split[1] != 'no other bags.':
        childs = rule_split[1].split(', ')
        children_colors = [' '.join(child.split()[1:3]) for child in childs]
        children_cnts = [int(child.split()[0]) for child in childs]
    return color, children_colors, children_cnts


if __name__ == '__main__':
    rules = read_input('input.txt')
    bag_cnt = bags_inside(rules, 'shiny gold')
    print(bag_cnt)
