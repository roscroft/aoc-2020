import re

def get_op_data(data):
    """Parses list of operations."""
    op_data = []
    for line in data:
        # Regex returns instruction and value into a tuple
        ins, val = re.findall(r"(nop|acc|jmp) \+?(-?\d+)", line)[0]
        op_data.append((ins, int(val)))
    return op_data

def execute(op_data):
    """Builds up an accumulator based on the op data. If the pointer goes beyond program input, it terminates and returns True, else False."""
    accum = 0
    ptr = 0
    visited = set()
    while ptr not in visited:
        visited.add(ptr)
        ins, val = op_data[ptr]
        if ins == "acc":
            accum += val
            ptr += 1
        elif ins == "nop":
            ptr += 1
        elif ins == "jmp":
            ptr += val
        if ptr >= len(op_data):
            return accum, True
    return accum, False

def part_1(op_data):
    return execute(op_data)[0]

def part_2(op_data):
    """Iterates through operations backwards, changing nop->jmp and vice versa attempting to find change that terminates program."""
    for ind in range(len(op_data)-1,-1,-1):
        ins, val = op_data[ind]
        if ins == "jmp":
            accum, terminates = execute(op_data[:ind] + [("nop", val)] + op_data[ind+1:])
        elif ins == "nop":
            accum, terminates = execute(op_data[:ind] + [("jmp", val)] + op_data[ind+1:])
        if terminates:
            return accum
    return "Does not terminate."

if __name__ == "__main__":
    day = 8
    with open(f"data/aoc{day}_data.txt") as data_file:
        data = data_file.read().strip().split("\n")
    data = get_op_data(data)
    print(f"Part 1 solution: {part_1(data)}")
    print(f"Part 2 solution: {part_2(data)}")