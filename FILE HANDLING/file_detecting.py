#file_detection
import os

file_path = "C:/Users/DELL/Desktop/VERILOG ASSIGNMENTS/test1.txt"

if os.path.exists(file_path):
    print(f"In the location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is directory / folder")
else:
    print("That location does'nt exists") 