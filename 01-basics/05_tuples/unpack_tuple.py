# Unpack the tuple

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk*

my_tuple = (1, 2, 5.5, "Aana", "is the", "Programmer")

(Aana, the , *pro) = my_tuple

print(my_tuple)