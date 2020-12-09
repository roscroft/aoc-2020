def get_floats_from_file(filename):
    with open(filename) as data_file:
        read_data = [float(x) for x in data_file.read().strip().split("\n")]
        return read_data

def get_ints_from_file(filename):
    with open(filename) as data_file:
        read_data = [int(x) for x in data_file.read().strip().split("\n")]
        return read_data

def get_strs_from_file(filename):
    with open(filename) as data_file:
        read_data = data_file.read().strip().split("\n")
        return read_data

def get_strlines_from_file(filename):
    """List of lists; splits file on empty lines"""
    with open(filename) as data_file:
        read_data = data_file.read().split("\n\n")
        return [x.split("\n") for x in read_data]