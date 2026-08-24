# Lists that contain numbers can be 
thislist = [1, 2, 3, 4, 5]
anotherlist = [6, 7, 8, 9, 10]

print(sum(thislist))  # Output: 15

print(thislist)  # Output: [1, 2, 3, 4, 5] 


# Some list methods can be used to modify the list, such as append(), remove(), and pop().

new_list = thislist.remove(3)  # Removing the number 3 from the list

print(new_list)

thislist.append(6)  # Adding the number 6 to the end of the list

print(thislist)  # Output: [1, 2, 4, 5, 6]

the_list = thislist.pop()  # Removing the last element from the list
print(the_list)  # Output: 6
print(thislist)  # Output: [1, 2, 4, 5]

thislist.extend(anotherlist)  # Inserting anotherlist at the second to last position of thislist

print(thislist)  # Output: [1, 2, 4, [6, 7, 8, 9, 10], 5]

# thislist.extend(anotherlist)  # Adding the elements of anotherlist to thislist

print(thislist)  # Output: [1, 2, 4, [6, 7, 8, 9, 10], 5, 6, 7, 8, 9, 10]
# the_list = thislist.extend("another_list")  # Adding the elements of anotherlist to thislist

# print(the_list)  # Output: None

print(thislist.index(4))  # Output: 2

print( 2 in thislist)  # Output: True


# Using loops to iterate through the elements of a list

for index, value in enumerate(thislist):
    print("The index of item is : ", index, "The value of an item is :", value)

    #or you can use f-strings to format the output

    print(f"Index: {index}; value: {value}")


