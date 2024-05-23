import re
def read_file(path:str) ->str:
    with open(path, 'r') as f:
        file = f.read()
    return file

def handle_data_str(file:str):
    match = re.search(r'length\W*(?P<length>\d*)\W*capacity\W*(?P<capacity>\d*)', file)
    if match:
        length, capacity = match.group("length"), match.group("capacity")

        data = {}
        
        for dataset in re.findall(r'dataset (\d+):\n\s*sizes = \{([0-9,\s]+)}\s*vals = \{([0-9,\s]+)}', file):
            dataset_number = int(dataset[0])
            sizes = list(map(int, dataset[1].split(',')))
            vals = list(map(int, dataset[2].split(',')))

            data[dataset_number] = {
                'sizes': sizes,
                'vals': vals
            }
        if len(data.keys())!=0:
            return int(length), int(capacity), data
    raise ValueError("Data incorrect")