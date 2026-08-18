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
print("the lenths of students is:" ,len(students))

# Add or modify

print("Adding or modifying items to dictionarries")
students["skills"] = ['Python','Scripting','javascript','node','AI-Autimation']
print(students["skills"][0])
print(students["skills"])


# Accessing students using key or indexing anything else.

# Change to list

print(students.items())

# Remove keys from dictionaries
print("After method or constructor or funtction applied")

print(students.pop("f_name"))
print(students.popitem())
del students["city"]


# Checking in students

print("after checking in")

print("address" in students)
print("age" in students)