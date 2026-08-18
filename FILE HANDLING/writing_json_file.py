import json

student = {
    "name" : "Kali Krishna",
    "age" : 22,
    "education" : "B.Tech"
}

file_path = "output.json"

try:
    with open(file_path, "w") as file:
        json.dump(student, file, indent = 4) 
        print(f"json file {file_path} is created")

except FileExistsError:
    print("That file is already exists")