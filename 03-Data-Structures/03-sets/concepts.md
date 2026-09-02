# Sets

## Core Idea

A set stores unique, hashable values and supports fast membership checks and mathematical operations.

```python
first = {1, 2, 3}
second = {3, 4}
print(first | second)
print(first & second)
```

## Skills To Build

- Remove duplicates with `set` when order is not required.
- Use union, intersection, difference, and symmetric difference.
- Test membership with `in`.
- Remember that sets are unordered and do not support indexing.
- Keep mutable values out of sets.

## Problem-Solving Method

Translate the problem into collection relationships: shared items, only-in-A, only-in-B, or all unique items.

## Common Trap

An empty set is `set()`, not `{}`. `{}` creates an empty dictionary.

## Further Reading

- [Python Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Codewars Python Kata](https://www.codewars.com/kata/search/python)
