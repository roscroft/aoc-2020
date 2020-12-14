from utils import utils

#[[0,0], [1,0], [2,0], [3,0], ...]
#[[0,1], [1,1], [2,1], [3,1], ...]

def new_state(cell_dct, coord, status):
    # Return a list of the form (occupied, unoccupied, empty)
    # coords = (x,y) - look at (x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)
    x = coord[0]
    y = coord[1]
    neighbors = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if [i,j] != [0,0] and cell_dct.get((x+i,y+j)) == "#":
                neighbors += 1
    if status=="L" and neighbors == 0:
        return "#"
    elif status=="#" and neighbors >= 4:
        return "L"
    else:
        return status

def new_state_2(cell_dct, coord, status):
    # Now we care about the first seat in any direction. So if the i,j is a ., keep looking 
    x = coord[0]
    y = coord[1]
    neighbors = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if [i,j] != [0,0]:
                if cell_dct.get((x+i,y+j)) == "#":
                    neighbors += 1
                elif cell_dct.get((x+i,y+j)) == ".":
                    itr_i, itr_j = i,j
                    while cell_dct.get((x+itr_i,y+itr_j)) == ".":
                        itr_i += i
                        itr_j += j
                        if cell_dct.get((x+itr_i,y+itr_j)) == "#":
                            neighbors += 1

    if status=="L" and neighbors == 0:
        return "#"
    elif status=="#" and neighbors >= 5:
        return "L"
    else:
        return status    

def pretty_print_1(cell_dct):
    print_lst = [[0]*10 for i in range(10)]
    for coord, status in cell_dct.items():
        x = coord[0]
        y = coord[1]
        print_lst[x][y] = status
    for row in print_lst:
        print(" ".join(row))

def pretty_print_2(cell_dct):
    print_lst = [[0]*93 for i in range(98)]
    for coord, status in cell_dct.items():
        x = coord[0]
        y = coord[1]
        print_lst[x][y] = status
    for row in print_lst:
        print(" ".join(row))

def part_1(cell_dct):
    # initialize a changes variable and loop until the field stops changing
    cur_dct = cell_dct
    changes = 1
    while changes > 0:
        #pretty_print(cur_dct)
        #print("      ")
        changes = 0
        new_cell_dct = {}
        for coord, status in cur_dct.items():
            new_status = new_state(cur_dct, coord, status)
            if new_status != status:
                changes += 1
            new_cell_dct[coord] = new_status
        cur_dct = new_cell_dct

    counter = 0
    for _, status in cur_dct.items():
        if status == "#":
            counter += 1
    return counter

def part_2(data):
    # initialize a changes variable and loop until the field stops changing
    cur_dct = cell_dct
    changes = 1
    while changes > 0:
        #pretty_print_1(cur_dct)
        #print("      ")
        changes = 0
        new_cell_dct = {}
        for coord, status in cur_dct.items():
            new_status = new_state_2(cur_dct, coord, status)
            if new_status != status:
                changes += 1
            new_cell_dct[coord] = new_status
        cur_dct = new_cell_dct

    counter = 0
    for _, status in cur_dct.items():
        if status == "#":
            counter += 1
    return counter

if __name__ == "__main__":
    day = 11
    data = utils.get_strs_from_file(f"data/aoc{day}_data.txt")
    cell_dct = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            cell_dct[(i,j)] = data[i][j]
    print(f"Part 1 solution: {part_1(cell_dct)}")
    print(f"Part 2 solution: {part_2(data)}")