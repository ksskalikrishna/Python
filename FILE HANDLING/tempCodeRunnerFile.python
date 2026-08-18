import csv
file_path = "output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[1])
except FileNotFoundError:
    print(f"That {file_path} file is not found")
except PermissionError:
    print(f"You do not have permission to read {file_path} file")