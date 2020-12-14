import numpy as np
from utils import utils

def part_1(data):
    pos = np.array([0,0])
    facing = np.array([1,0])
    dir_dict = {"N": np.array([0,1]), "S": np.array([0,-1]), "E": np.array([1,0]), "W": np.array([-1,0])}

    for move in data:
        direction, distance = move[:1], int(move[1:])
        if direction in ["N", "S", "E", "W"]:
            pos += distance*dir_dict[direction]
        elif direction == "F":
            pos += distance*facing
        elif direction == "R":
            for _ in range(distance // 90):
                facing = np.array([facing[1], facing[0]*-1])
        elif direction == "L":
            for _ in range(distance // 90):
                facing = np.array([facing[1]*-1, facing[0]])
    
    return abs(pos[0]) + abs(pos[1])
        

def part_2(data):
    ship = np.array([0,0])
    waypoint = np.array([10,1])
    dir_dict = {"N": np.array([0,1]), "S": np.array([0,-1]), "E": np.array([1,0]), "W": np.array([-1,0])}

    for move in data:
        direction, distance = move[:1], int(move[1:])
        if direction in ["N", "S", "E", "W"]:
            waypoint += distance*dir_dict[direction]
        elif direction == "F":
            ship += distance*waypoint
        elif direction == "R":
            for _ in range(distance // 90):
                waypoint = np.array([waypoint[1], waypoint[0]*-1])
        elif direction == "L":
            for _ in range(distance // 90):
                waypoint = np.array([waypoint[1]*-1, waypoint[0]])
    
    return abs(ship[0]) + abs(ship[1])

if __name__ == "__main__":
    day = 12
    data = utils.get_strs_from_file(f"data/aoc{day}_data.txt")
    print(f"Part 1 solution: {part_1(data)}")
    print(f"Part 2 solution: {part_2(data)}")