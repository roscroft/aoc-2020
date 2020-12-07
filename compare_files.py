with open("check_output.txt", "r") as h_file:
    myset = set(h_file.read().strip().split("\n"))

with open("passports.txt", "r") as r_file:
    otherset = set(r_file.read().strip().split("\n"))

print("H - R:", myset.difference(otherset))
print("R - H:", otherset.difference(myset))