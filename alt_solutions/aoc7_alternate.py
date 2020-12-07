import re
def read_file(filename):
    with open(filename) as file:
        return file.readlines()
def parse_rule(rule):
    outer_bag = re.search(r'(.*) bags contain', rule).group(1)
    inner_bag_list = re.findall(r'\d+ (.*?) bag', rule)
    return (outer_bag, inner_bag_list)
def parse_rule_2(rule):
    outer_bag = re.search(r'(.*) bags contain', rule).group(1)
    inner_bag_list = re.findall(r'(\d+) (.*?) bag', rule)
    return (outer_bag, inner_bag_list)
def check_contains(bag_dict, current_color, search_color):
    if search_color in bag_dict[current_color]:
        return 1
    elif not bag_dict[current_color]:
        # Empty bag
        return 0
    else:
        for color in bag_dict[current_color]:
            if check_contains(bag_dict, color, search_color):
                return 1
        return 0
def calc_bags(rule_list, bag_color):
    bag_dict = dict((parse_rule(rule) for rule in rule_list))
    count = 0
    for bag in bag_dict.keys():
        count += check_contains(bag_dict, bag, bag_color)
    return count
def check_contains_2(bag_dict, current_color):
    total = 1
    for num, bag in bag_dict[current_color]:
        total += int(num) * check_contains_2(bag_dict, bag)
    return total
def calc_bags_2(rule_list, bag_color):
    bag_dict = dict((parse_rule_2(rule) for rule in rule_list))
    count = 0
    for bag in bag_dict.keys():
        if bag == bag_color:
            count += check_contains_2(bag_dict, bag)
    return count-1
if __name__ == "__main__":
    input = read_file("./data/aoc7_data.txt")
    bag_color = "shiny gold"
    print(f"Part 1: {calc_bags(input, bag_color)}")
    print(f"Part 2: {calc_bags_2(input, bag_color)}")