students = ["Raju", "Ramu", "Ravi", "Rakesh"]

file_path = "output.json"

try:
    with open(file_path, "w") as file:
        for student in students:
            file.write(student + ", ")
        print(f"text list file {file_path} is created")

except FileExistsError:
    print("That file is already exists")