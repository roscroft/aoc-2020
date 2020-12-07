import utils
import re
valid_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
npc_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    
def part_1(data):
    with open("aoc4_data.txt") as data_file:
        count = 0
        pwd_dict = {}
        for line in data_file.read().strip().split("\n"):
            if line != "":
                fields = line.split()
                for field in fields:
                    key = field.split(":")
                    pwd_dict[key[0]] = key[1]
            else:
                keys = pwd_dict.keys()
                count += (keys == valid_keys or keys == npc_keys)
                pwd_dict = {}
    return count

def part_2(data):
    with open("aoc4_data.txt") as data_file:
        count = 0
        pwd_dict = {}
        passports = data_file.read().strip().split("\n")
        counter_max = len(passports)
        counter = 0
        for line in passports:
            if line != "" or counter >= counter_max:
                fields = line.split()
                for field in fields:
                    key = field.split(":")
                    pwd_dict[key[0]] = key[1]
                counter += 1
            else:
                keys = pwd_dict.keys()
                if keys == valid_keys or keys == npc_keys:
                    byr = bool(re.match(r"^19[2-9][0-9]|200[0-2]$", pwd_dict["byr"]))
                    iyr = bool(re.match(r"^201[0-9]|2020$", pwd_dict["iyr"]))
                    eyr = bool(re.match(r"^202[0-9]|2030$", pwd_dict["eyr"]))
                    hgt = bool(re.match(r"^(?:1[5-8][0-9]|19[0-3])cm$", pwd_dict["hgt"])) or bool(re.match(r"^(?:59|6[0-9]|7[0-6])in$", pwd_dict["hgt"]))
                    hcl = bool(re.match(r"^#[0-9a-f]{6}$", pwd_dict["hcl"]))
                    ecl = bool(re.match(r"^(?:amb|blu|brn|gry|grn|hzl|oth)$", pwd_dict["ecl"]))
                    pid = bool(re.match(r"^\d{9}$", pwd_dict["pid"]))
                    count += (byr and iyr and eyr and hgt and hcl and ecl and pid)
                pwd_dict = {}
                counter += 1
        return count

if __name__ == "__main__":
    data = utils.get_strs_from_file("aoc4_data.txt")
    output_1 = part_1(data)
    print(output_1)
    output_2 = part_2(data)
    print(output_2)