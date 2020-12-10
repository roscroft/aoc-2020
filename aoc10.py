from utils import utils

def part_1(data):
    count_1 = 0
    count_3 = 0
    for i in range(1,len(data)):
        if data[i] - data[i-1] == 1:
            count_1 += 1
        elif data[i] - data[i-1] == 3:
            count_3 += 1
    return count_1*count_3

def part_2(data):
    dynm = [0] * len(data)
    dynm[0] = 1
    dynm[1] = 1
    dynm[2] = 2 if data[2] - data[0] <= 3 else 1
    for i in range(3, len(data)):
        dynm[i] = sum([dynm[j] if data[i] - data[j] <= 3 else 0 for j in range(i-3,i)])
    return dynm[-1]

#def part_2_m(data):


if __name__ == "__main__":
    day = 10
    data = utils.get_ints_from_file(f"data/aoc{day}_data.txt")
    data = sorted(data)
    data = [0] + data + [data[-1]+3]
    print(f"Part 1 solution: {part_1(data)}")
    print(f"Part 2 solution: {part_2(data)}")