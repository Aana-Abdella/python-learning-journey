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

# Copy from students

print("The new and copied from the fist dictionary")

new_dict = students.copy()

new_dict["f_name"] = "Aanaa"

print(new_dict)

# clear students after copy to new_dict 
print(" clear students after copy to new_dict ")
students.clear()
print(students)

#get keys of dictionaries

keys = students.keys()
new_keys = new_dict.keys()

values = new_dict.values()
print(keys)
print(new_keys)
print(values)
print(new_dict.get("f_name"))

third_dict = new_dict.copy()


#delete dict
print("after delete nothing is here")
del new_dict

print("but there is the third dict it copied from new_dict before delete")

print(third_dict)