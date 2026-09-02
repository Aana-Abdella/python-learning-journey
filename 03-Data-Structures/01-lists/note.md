1. Lists 

Lists are ordered, mutable collections of items. They are the most versatile structure and support numerous methods:

    Manipulation: You can add items using .append(), .insert(), or .extend(), and remove items using .remove() or .pop() 
    Slicing & Accessing: Use indices (starting at 0) or negative indices for convenience. You can also slice lists (e.g., [0:2]) to extract subsets 
    Sorting: Use .sort() to modify in-place or sorted() to return a new sorted list
    Conversion: Easily convert lists to strings with .join() and back to lists with .split() 

2. Tuples

Tuples are similar to lists but are immutable, meaning they cannot be modified after creation.

    They use parentheses () instead of square brackets [].
    Use them for data that should remain constant throughout your program.

3. Sets (23:37 - 27:18)

Sets are unordered collections of unique values.

    They use curly braces {}.
    They are highly efficient for membership tests (checking if an item exists) and handling unique items (duplicates are automatically removed).
    Advanced operations include .intersection(), .difference(), and .union() for comparing sets.

Bonus: Empty Structures (27:20 - 28:17)

    Lists: Use [] or list().
    Tuples: Use () or tuple().
    Sets: Must use set() because {} creates an empty dictionary.

