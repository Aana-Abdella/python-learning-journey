# Tuples

## Core Idea

A tuple is an ordered, immutable collection. Tuples are useful for fixed records and returning several values from a function.

```python
point = (10, 20)
x, y = point
print(x, y)
```

## Skills To Build

- Create one-item tuples with `(value,)`.
- Unpack values into named variables.
- Use tuple indexing and slicing.
- Recognize that tuple immutability protects the tuple structure, not necessarily nested mutable objects.
- Use tuples when the record should not be reassigned.

## Problem-Solving Method

Ask whether the collection represents a fixed record or a changing collection. Choose a tuple for fixed structure and a list for changing membership.

## Common Trap

Parentheses are not what makes a tuple; the comma does. `value,` is a tuple, while `(value)` is just a value in parentheses.

## Further Reading

- [Python Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Data Structures Exercises](https://exercism.org/tracks/python/exercises)
