def read_file(filename):
    with open(filename) as file:
        return [[line.rstrip("\n").split(), 0] for line in file]
def clean_input(input_list):
    for input in input_list:
        input[1] = 0
def is_fixed(input_list):
    index = 0
    accumulator = 0
    max_index = len(input_list)
    while(True):
        if index == max_index:
            return True
        elif input_list[index][1] == 1:
            return False
        else:
            input_list[index][1] = 1
        instruction = input_list[index][0][0]
        increment = int(input_list[index][0][1])
        if instruction == "acc":
            accumulator += increment
            index += 1
        elif instruction == "jmp":
            index += increment
        elif instruction == "nop":
            index += 1
def part1(input_list):
    index = 0
    accumulator = 0
    max_index = len(input_list)
    while(True):
        if index == max_index or input_list[index][1] == 1:
            break
        else:
            input_list[index][1] = 1
        instruction = input_list[index][0][0]
        increment = int(input_list[index][0][1])
        if instruction == "acc":
            accumulator += increment
            index += 1
        elif instruction == "jmp":
            index += increment
        elif instruction == "nop":
            index += 1
    return accumulator
def part2(input_list):
    index = len(input_list)-1
    while(True):
        instruction = input_list[index][0][0]
        if instruction == "jmp":
            input_list[index][0][0] = "nop"
            if is_fixed(input_list):
                clean_input(input_list)
                return part1(input_list)
            input_list[index][0][0] = "jmp"
            clean_input(input_list)
        index -= 1
if __name__ == "__main__":
    filename = "input.txt"
    input_list = read_file(filename)
    print(f"Part 1: {part1(input_list)}")
    clean_input(input_list)
    print(f"Part 2: {part2(input_list)}")