import os

folder_path = input("Enter a list of folders with space: ").split()
print(folder_path)

for folder in folder_path:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide valid directory :", folder)
        break
    for file in files:
        print("------------------")
        print(file)

