thistuple =("apple", "banana", "cherry")

mylist = list(thistuple)  # Convert the tuple to a list

mylist[1] = "mango"  # Update the second element of the list

thsituple = tuple(mylist)  # Convert the list back to a tuple

print(thsituple)  # Output: ('apple', 'mango', 'cherry')

# add new element to the tuple

x = ("apple", "banana", "cherry")

y = list(x)

# Appenf

y.append("orange")

x = tuple(y)

print(x)

#Remove items

y.remove("banana")
x = tuple(y)

print(x)

# Add tuple to tuple

fruit_tuple = ("banana", "strawberry")

add = ("mango","apple")

fruit_tuple += add

print(fruit_tuple)


#Join two tuples by using add them

tuple1 = ("Pyramid", "Stone")
tuple2 = ("oromo", "Ethiopia")

tuple3 = tuple1 + tuple2

print(tuple3)

# Multiple Tuples

tuple4 = ("Hararii", "Dire Dawa")

tuple5 = tuple4 *2

print(tuple5)