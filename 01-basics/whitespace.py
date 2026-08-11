# the programm remove the whitespace from the string using strip() method

message = "   Hello World   "

print("The original string is:", message)

# use the strip() method to remove whitespace from the string

sripped_message = message.strip()

#print the string after removing whitespace

print("The string after removing whitespace is:", sripped_message)


#the programm remove the whitespace from the string using lstrip() method

original_message = "   Hello World   "

print("The original string is:", original_message)

# use the lstrip() method to remove whitespace from the left side of the string

lstripped_message = original_message.lstrip()

#print the string after removing whitespace from the left side

print("The string after removing whitespace from the left side is:", lstripped_message)

#the programm remove the whitespace from the string using rstrip() method

unstripped_message = "   Hello World   "

print("The original string is:", unstripped_message)

# use the rstrip() method to remove whitespace from the right side of the string   

rstripped_message = unstripped_message.rstrip()

#print the string after removing whitespace from the right side

print("The string after removing whitespace from the right side is:", rstripped_message)

# The programm remove the whitespace from the string using replace() method


#the programm that print in new line using \n

message1 = "Hello "

message2 = "world "

print(message1, message2, sep='\n')
