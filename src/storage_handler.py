import csv

# read csv data from path
def read_from_file(path: str):
    try:
        with open(path, 'r') as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        return None
    
# write 
def write_row_to_file(path: str, data):
    with open(path, 'w') as file:
            csv.writer(file).writerow(data)

# write 
def write_rows_to_file(path: str, data):
    with open(path, 'w') as file:
            csv.writer(file).writerows(data)