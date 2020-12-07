import re
def read_file(filename):
    with open(filename) as file:
        return file.readlines()
def parse_rule(rule):
    outer_bag = re.search(r'(.*) bags contain', rule).group(1)
    inner_bag_list = re.findall(r'\d+ (.*?) bag', rule)
    return (outer_bag, inner_bag_list)
def check_contains(bag_dict, bag_list, bag_color):
    count = 0
    for bag in bag_list:
        if bag == bag_color:
            count += 1
            break
        else:
            count += check_contains(bag_dict, bag_dict.get(bag), bag_color)
    return count > 0
def calc_bags(rule_list, bag_color):
    bag_dict = dict((parse_rule(rule) for rule in rule_list))
    print(bag_dict)
    count = 0
    for bag in bag_dict:
        count += check_contains(bag_dict, bag_dict.get(bag), bag_color)
    return count
if __name__ == "__main__":
    input = read_file("./data/aoc7_data2.txt")
    bag_color = "shiny gold"
    print(f"Part 1: {calc_bags(input, bag_color)}")