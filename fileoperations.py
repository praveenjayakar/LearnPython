with open("sample.txt", "w") as file:
    file.write("Hey boys")

with open("sample.txt","r") as file:
    content = file.read()
    print("File content:" , content)

