import csv

# read csv data from path
def read_from_file(path: str = "data/students.csv"):
    data = []
    try:
        with open(path, 'r') as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        return None