import utils

def part_1(x_inc, y_inc, data):
    count = 0
    x = 0
    y = 0
    line_length = len(data[0])
    while y < len(data):
        count += (data[y][x] == "#")
        x = (x + x_inc) % line_length
        y += y_inc
    return count

def part_2(data):
    pairs = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    trees = 1
    for pair in pairs:
        trees *= part_1(pair[0], pair[1], data)
    return trees

if __name__ == "__main__":
    data = utils.get_strs_from_file("aoc3_data.txt")
    x_inc = 3
    y_inc = 1
    output_1 = part_1(x_inc, y_inc, data)
    print(output_1)
    output_2 = part_2(data)
    print(output_2)