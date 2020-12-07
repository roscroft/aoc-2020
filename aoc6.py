from functools import reduce

def part_1(data):
    return sum([len(reduce(lambda x,y: set(x).union(set(y)), x)) for x in data])

def part_2(data):
    return sum([len(reduce(lambda x,y: set(x).intersection(set(y)), x)) for x in data])

if __name__ == "__main__":
    day = 6
    with open(f"data/aoc{day}_data.txt", "r") as data_file:
        read_data = data_file.read().split("\n\n")
        data = [x.split("\n") for x in read_data]
    print(f"Part 1 solution: {part_1(data)}")
    print(f"Part 2 solution: {part_2(data)}")