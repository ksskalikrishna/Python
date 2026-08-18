import json
file_path = "output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["education"])
except FileNotFoundError:
    print(f"That {file_path} file is not found")
except PermissionError:
    print(f"You do not have permission to read {file_path} file")