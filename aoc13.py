import re
from functools import reduce
from utils import utils

def part_1(data):
    timestamp = int(data[0])
    bus_ids = [int(bus_id) for bus_id in re.findall(r"(\d+)", data[1])]

    min_gap = 10000
    min_bus_id = 0

    for bus_id in bus_ids:
        gap = (timestamp // bus_id)*bus_id + bus_id - timestamp
        if gap < min_gap:
            min_gap = gap
            min_bus_id = bus_id

    return min_gap * min_bus_id
    
def part_2(data):
    bus_data = [(int(bus_id), index) for index, bus_id in enumerate(data[1].split(",")) if bus_id != 'x']
    bus_ids = [bus_id for bus_id, _ in bus_data]
    bus_mods = [bus_id-index for bus_id, index in bus_data]
    return chinese_remainder_theorem(bus_ids, bus_mods)

def chinese_remainder_theorem(nums, modulos):
    # Take in a list of numbers and their modulos; for x*a = n, y*b = n+i, z*c = n+j, etc.,
    # the modulos will be equal to 0, y-i, z-j, etc.
    def bezout(a,b):
        old_r, r = a, b
        old_s, s = 1, 0
        old_t, t = 0, 1
        while r != 0:
            quotient = old_r // r
            (old_r, r) = (r, old_r - quotient * r)
            (old_s, s) = (s, old_s - quotient * s)
            (old_t, t) = (t, old_t - quotient * t)
        
        #print(f"Bezout coeffecients: {(old_s, old_t)}")
        #print(f"Greatest common divisor: {old_r}")
        #print(f"Quotients by the GCD: {(t, s)}")
        return (old_s, old_t)

    running_sum = 0
    M = reduce(lambda x,y: x*y, nums)
    nums_modulos = zip(nums, modulos)
    for num, modulo in nums_modulos:
        b_i = int(M/num)
        mod_mult_inverse = bezout(b_i, num)[0]
        running_sum += modulo*mod_mult_inverse*b_i
    return running_sum % M

if __name__ == "__main__":
    day = 13
    data = utils.get_strs_from_file(f"data/aoc{day}_data.txt")
    print(f"Part 1 solution: {part_1(data)}")
    print(f"Part 2 solution: {part_2(data)}")