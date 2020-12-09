from utils import utils

def add_to_sums_dict(sums_dict, num):
    sums_dict[num] = set()
    for base, _ in sums_dict.items():
        if base != num:
            sums_dict[num].add(base+num)
            sums_dict[base].add(base+num)
    return sums_dict

def remove_from_sums_dict(sums_dict, num):
    del sums_dict[num]
    for base, _ in sums_dict.items():
        sums_dict[base].remove(num+base)
    return sums_dict

def valid(num, sums_dict):
    for _, sums in sums_dict.items():
        if num in sums:
            return True
    return False

def part_1(data):
    preamble = 25
    sums_dict = {}
    for i in range(0, preamble):
        num = data[i]
        sums_dict = add_to_sums_dict(sums_dict, num)
    for i in range(preamble, len(data)):
        num = data[i]
        if not valid(num, sums_dict):
            return num
        else:
            sums_dict = remove_from_sums_dict(sums_dict, data[i-25])
            sums_dict = add_to_sums_dict(sums_dict, data[i])
    return None

def greedy_sum(data, target_num):
    # Greedily consume as many numbers as possible to see if we can reach target num
    running_sum = 0
    for i in range(len(data)):
        num = data[i]
        running_sum += num
        if running_sum == target_num:
            return max(data[:i]) + min(data[:i])
        elif running_sum > target_num:
            return None
    return None

def part_2(data):
    target_num = part_1(data)
    # Data list backwards starting just before target
    reverse_data = data[data.index(target_num)-1::-1]
    for i in range(len(reverse_data)):
        target_sum = greedy_sum(reverse_data[i:], target_num)
        if target_sum:
            return target_sum
    return None

if __name__ == "__main__":
    day = 9
    data = utils.get_ints_from_file(f"data/aoc{day}_data.txt")
    print(f"Part 1 solution: {part_1(data)}")
    print(f"Part 2 solution: {part_2(data)}")