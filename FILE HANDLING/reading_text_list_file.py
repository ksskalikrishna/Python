file_path = "output_list.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"That {file_path} file is not found")
except PermissionError:
    print(f"You do not have permission to read {file_path} file")