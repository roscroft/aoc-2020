def part1_ol(data):
    return reduce(lambda a,b: sum(a) + len(b), reduce(lambda a,b: ([], set(a.strip() + b.strip())) if type(a) != tuple else (a[0] + [len(a[1])], set()) if b == "\n" else (a[0], a[1].union(b.strip())), data))
def part2_ol(data):
    return reduce(lambda a,b: sum(a) + len(b[0].intersection(*b[1:])), reduce(lambda a,b: ([], [set(a.strip()), set(b.strip())]) if type(a) != tuple else (a[0] + [len(a[1][0].intersection(*a[1][1:]))], []) if b == "\n" else (a[0], a[1] + [set(b.strip())]), data))