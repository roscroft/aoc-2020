from utils import utils

def two_sum_to_2020(data):
    for i in range(len(data)):
        for j in range(i,len(data)):
            if data[i] + data[j] == 2020:
                return data[i]*data[j]
    return 0

def three_sum_to_2020(data):
    for i in range(len(data)):
        for j in range(i,len(data)):
            for k in range(j,len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i]*data[j]*data[k]
    return 0
    
if __name__ == "__main__":
    day = 1
    data = utils.get_ints_from_file(f"data/aoc{day}_data.txt")
    output_1 = two_sum_to_2020(data)
    print(output_1)
    output_2 = three_sum_to_2020(data)
    print(output_2)