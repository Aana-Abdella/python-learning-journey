thistuple =("apple", "banana", "cherry")

mylist = list(thistuple)  # Convert the tuple to a list

mylist[1] = "mango"  # Update the second element of the list

thsituple = tuple(mylist)  # Convert the list back to a tuple

print(thsituple)  # Output: ('apple', 'mango', 'cherry')

# add new element to the tuple

x = ("apple", "banana", "cherry")

y = list(x)

y.append("orange")

x = tuple(y)

print(x)


# Add tuple to tuple

fruit_tuple = ("banana", "strawberry")

add = ("mango","apple")

fruit_tuple += add

print(fruit_tuple)