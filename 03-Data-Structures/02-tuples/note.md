
**Tuple** are used to store multiple items in a single variable.
       -it is built in
       -it is unchangable
       -written with round brackets and also wothout brackets.

**Tuple Items** 
       -ordered, unchangable, and allow duplicate values.

**Ordered** 
     -it have defined order and order not change.

**Unchangable** 
    -we cannot change , add, remove ,add or remove items from tuple

**Duplicate**
     -tuple are indexed, it have items with the same values

𝗞𝗲𝘆 𝗖𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿𝗶𝘀𝘁𝗶𝗰𝘀
• 𝗢𝗿𝗱𝗲𝗿𝗲𝗱: Elements have a defined sequence that will not change.
• 𝗜𝗺𝗺𝘂𝘁𝗮𝗯𝗹𝗲: You cannot add, remove, or modify items after creation.
• 𝗛𝗲𝘁𝗲𝗿𝗼𝗴𝗲𝗻𝗲𝗼𝘂𝘀: Can store mixed data types (integers, strings, lists).
• 𝗛𝗮𝘀𝗵𝗮𝗯𝗹𝗲: Can be used as keys in a dictionary (if all elements are also immutable).
 
   *METHODS@*
     len()
     type() is used     


# 3. Check for a Tuple Using isinstance()
   --If you are writing conditional logic to check if an object is a tuple,
   -- it is best practice to use isinstance() instead of type() == tuple because it natively supports subclassing:



# Access The Tuple 
  -- access tuple items by referring to the index number, inside square brackets:
  -- also using range of index.

  for example 
  my tuple = ("python", "java", "php", 1, 12.05, none) 
You can access tuple items by referring to the index number, inside square brackets:
  print(my_tuple[2:5])  output : ("php". 1, 12.05)

  it means start from 2 and 2 is included and upto 5 but 5 is not included

# Negative indexing 
  it also the same with posotive indexing but you have to use small negative number to big negative number

   for example 
  my tuple = ("python", "java", "php", 1, 12.05, none) 
You can access tuple items by referring to the index number, inside square brackets:
  print(my_tuple[-5:-2])  output : ("java". "php", 1, )
    it means start from 2 and 2 is included and upto 5 but 5 is not included
    
    
# Check if Item Exists
   --To determine if a specified item is present in a tuple use the *in* keyword:
   -- use *not in* keyword:

# Change Tuple Values
 -- tuples are unchangable. once you create you cant remove item or add item 

 trick: You have to change to list and add or remove item, and back change to tuple.


# Add tuple to a tuple
 -- to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
 



 # Tuple Methods

Python has two built-in methods that you can use on tuples.
𝗠𝗲𝘁𝗵𝗼𝗱 	𝗗𝗲𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found