

my_dict = {'name': 'praveen', 'age': 27, 'sex': 'male'}
print(my_dict)
#del my_dict['age']
print(my_dict)
print(my_dict['age'])

if 'age' in my_dict:
    print("Age is present in my dict")
else:
    print("not present")


for key, value in my_dict.items():
    print(key, value)


