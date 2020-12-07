import re
from utils import utils

def parse(pass_str):
    m = re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', pass_str)
    lb, ub, letter, password = m.groups()
    return (int(lb), int(ub), letter, password)

def part_1(data):
    count = 0
    for pass_str in data:
        lb, ub, letter, password = parse(pass_str)
        letter_count = len(re.findall(rf'{letter}', password))
        if lb <= letter_count and letter_count <= ub:
            count += 1
    return count

def part_2(data):
    count = 0
    for pass_str in data:
        lb, ub, letter, password = parse(pass_str)
        match_lower = password[lb-1] == letter
        match_upper = password[ub-1] == letter
        if match_lower != match_upper:
            count += 1
    return count

if __name__ == "__main__":
    day = 2
    data = utils.get_strs_from_file(f"data/aoc{day}_data.txt")
    output_1 = part_1(data)
    print(output_1)
    output_2 = part_2(data)
    print(output_2)