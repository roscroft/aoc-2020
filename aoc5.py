import utils

def convert_dec(digits):
    char_replace = {"F":"0", "L":"0", "B":"1", "R":"1"}
    for char, digit in char_replace.items():
        digits = digits.replace(char, digit)
    return int(digits, 2)

def part_1(data):
    return max(map(convert_dec, data))

def part_2(data):
    seat_ids = list(map(convert_dec, data))
    min_seat = min(seat_ids)
    max_seat = max(seat_ids)
    return int(max_seat*(max_seat+1)/2 - min_seat*(min_seat-1)/2 - sum(seat_ids))

if __name__ == "__main__":
    data = utils.get_strs_from_file("aoc5_data.txt")
    print(f"Part 1 solution: {part_1(data)}")
    print(f"Part 2 solution: {part_2(data)}")