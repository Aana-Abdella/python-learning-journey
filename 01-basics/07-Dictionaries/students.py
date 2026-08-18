students = {
    "f_name" : "Aanaa",
    "l_name" : "Abdella",
    "gender" : "male",
    "status" : "single",
    "countey" : "Ethipoia",
    "city" : "Karamile",
    "address" : "Dire-Dawa"
}

print("before anything applied")
print(students)
print(len(students))

# Change to list

print(students.items())

# Remove keys from dictionaries
print("After method or constructor or funtction applied")

print(students.pop("f_name"))
print(students.popitem())
del students["city"]
