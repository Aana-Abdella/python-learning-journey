

#this_tuple = ("apple",)

#print(type(this_tuple))

empty_tuple = ()
print(type(empty_tuple))  # Output: <class 'tuple'>


this_tuple = ("apple", "banana", "cherry", 10,  True, 3.14, None)

types = [type(item) for item in this_tuple]

print(types)  # Output: [<class 'str'>, <class 'str'>, <class 'str'>, <class 'int'>, <class 'bool'>, <class 'float'>, <class 'NoneType'>]

# get the type of tuple using the map() method

tuple_types = list(map(type, this_tuple))

print(tuple_types) 

