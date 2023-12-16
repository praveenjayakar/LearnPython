instance = input("Enter your instance type: ")
print(instance)
if instance == "t2.micro":
    print("we will create", instance, "for you")
elif instance == "t2.large":
    print("we will create", instance, "for you")
elif instance == "t2.xarge":
    print("we will create", instance, "for you")
elif instance == "t2.small":
    print("we will create", instance, "for you")
else:
    print("Please provide a valid type")

