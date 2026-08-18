import csv

students = [["Name", "Age", "Branch"],
            ["Raju", 22, "ECE"],
            ["Ramu", 21, "CSE"],
            ["Ravi", 21, "EEE"],
            ["Rakesh", 23, "MECH"]] 

file_path = "output.csv"

try:
    with open(file_path, "w", newline = "") as file:
        writer = csv.writer(file)
        for row in students:
            writer.writerow(row)
        print(f"csv file {file_path} is created")

except FileExistsError:
    print("That file is already exists")