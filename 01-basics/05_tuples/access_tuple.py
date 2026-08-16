# Access the tuple elements using indexing

my_tuple = ("apple", "banana", "cherry", 10,  True, 3.14, None)

print(my_tuple[0])  # Output: apple

# Negative indexing to access the last element of the tuple

print(my_tuple[-1])  # Output: None

# Accessing a range of elements using slicing

print(my_tuple[1:4])  # Output: ('banana', 'cherry', 10)

# negative range slicing to access elements from the end of the tuple

print(my_tuple[-4:-1])  # Output: (10, True, 3.14)

# Accessing elements using a step value in slicing

print(my_tuple[::2])  # Output: ('apple', 'cherry', True, None)

# accessing elements using a negative step value in slicing

print(my_tuple[::-1])  # Output: (None, 3.14, True, 10, 'cherry', 'banana', 'apple')

print(my_tuple[1:5:2])  # Output: ('banana', 10)
# Checking if an element exists in the tuple using the 'in' keyword

if "apple" in my_tuple:
    print("Yes, 'apple' is in the tuple")  # Output: Yes, 'apple' is in the tuple