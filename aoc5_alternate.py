from math import floor, ceil
def read_file(filename):
    with open(filename) as file:
        return file.readlines()
def calculate_seat_id(line):
    row_total = 128
    col_total = 8
    row_min = 1
    row_max = row_total
    col_min = 1
    col_max = col_total
    for i in range(7):
        if (line[i] == "F"):
            row_max = floor(row_max - (row_max - row_min)/2)
        elif (line[i] == "B"):
            row_min = ceil(row_min + (row_max - row_min)/2)
    for i in range(7, len(line)):
        if (line[i] == "L"):
            col_max = floor(col_max - (col_max - col_min)/2)
        elif (line[i] == "R"):
            col_min = ceil(col_min + (col_max - col_min)/2)
    # set index to 0
    row_min -= 1
    col_min -= 1
    seat_id = row_min * 8 + col_min
    return seat_id
def calculate_highest_id(line_list):
    return max([calculate_seat_id(line) for line in line_list])
def calculate_missing_seat(line_list):
    sorted_seats = sorted([calculate_seat_id(line) for line in line_list])
    start, end = sorted_seats[0], sorted_seats[-1]
    return set(range(start, end+1)).difference(sorted_seats)
if __name__ == "__main__":
    input = read_file("input.txt")
    print(f"Part 1: {calculate_highest_id(input)}")
    print(f"Part 2: {calculate_missing_seat(input).pop()}")