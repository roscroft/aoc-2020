from utils import utils

def masked(num, mask):
    bin_num = bin(int(num))[2:]
    bin_num = "0"*(36-len(bin_num))+bin_num
    res = ""
    for i in range(len(bin_num)):
        if mask[i] == "X":
            res += bin_num[i]
        else:
            res += mask[i]
    return int(res, 2)

def part_1(data):
    mem = {}
    mask = ""
    for line in data:
        ins, num = line.split(" = ")
        if ins == "mask":
            mask = num
        else:
            adr = ins[4:-1]
            mem[adr] = masked(num, mask)

    return sum([num for _, num in mem.items()])

def get_adrs(bin_adr, mask):
    def get_x_perms(mask):
        xs = mask.count("X")
        max_len = len(bin(2**xs-1)[2:])
        p_list = []
        for i in range(0,2**xs):
            bin_i = bin(i)[2:]
            bin_i_len = len(bin_i)
            p_list.append("0"*(max_len-bin_i_len)+bin_i)
        return p_list

    adrs = []
    x_perms = get_x_perms(mask)
    for perm in x_perms:
        p = 0
        adr = ""
        for i in range(len(bin_adr)):
            if mask[i] == "0":
                adr += f"{bin_adr[i]}"
            elif mask[i] == "1":
                adr += f"{mask[i]}"
            else:
                adr += f"{perm[p]}"
                p += 1
        adrs.append(adr)
    return adrs

def part_2(data):
    mem = {}
    mask = ""
    for line in data:
        ins, num = line.split(" = ")
        if ins == "mask":
            mask = num
        else:
            adr = ins[4:-1]
            bin_adr = bin(int(adr))[2:]
            bin_adr = "0"*(36-len(bin_adr))+bin_adr
            adrs = get_adrs(bin_adr, mask)
            for adr in adrs:
                mem[adr] = int(num)

    return sum([num for _, num in mem.items()])

if __name__ == "__main__":
    day = 14
    data = utils.get_strs_from_file(f"data/aoc{day}_data.txt")
    print(f"Part 1 solution: {part_1(data)}")
    print(f"Part 2 solution: {part_2(data)}")