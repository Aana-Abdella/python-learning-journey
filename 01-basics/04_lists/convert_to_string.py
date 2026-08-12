# Converting a list to a string and vice versa

is_list = ["Python", "is", "awesome", "and", "I", "love", "it"]

python_string = ", ".join(is_list)  # Converting a list to a string

print(python_string)  # Output: Python is awesome and I love it

# convert the string back to a list

new_list = python_string.split(", ")  # Converting a string back to a list

print(new_list)  # Output: ['Python', 'is', 'awesome', 'and',