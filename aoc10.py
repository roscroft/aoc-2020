from utils import utils

def part_1(data):
    count_1 = sum([1 if data[i] - data[i-1] == 1 else 0 for i in range(len(data))])
    count_3 = sum([1 if data[i] - data[i-1] == 3 else 0 for i in range(len(data))])
    return count_1*count_3

def part_2(data):
    dynm = [1] + [0]*(len(data)-1)
    for i in range(1, len(data)):
        dynm[i] = sum([dynm[i-j] if data[i] - data[i-j] <= 3 else 0 for j in range(1, 4)])
    return dynm[-1]

if __name__ == "__main__":
    day = 10
    data = utils.get_ints_from_file(f"data/aoc{day}_data.txt")
    data = sorted(data)
    data = [0] + data + [data[-1]+3]
    print(f"Part 1 solution: {part_1(data)}")
    print(f"Part 2 solution: {part_2(data)}")