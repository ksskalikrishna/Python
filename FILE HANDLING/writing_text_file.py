txt_data = "Kali Krishna is a good boy"

file_path = "C:/Users/DELL/Desktop/VERILOG ASSIGNMENTS/test1.txt"

try:
    with open(file_path, "w") as file:
        file.write("\n" + txt_data)
        print(f"text file {file_path} is created")

except FileExistsError:
    print("That file is already exists")