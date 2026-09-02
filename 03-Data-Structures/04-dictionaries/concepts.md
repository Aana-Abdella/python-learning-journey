# Dictionaries

## Core Idea

A dictionary maps hashable keys to values. Use it when the data has labels or when lookup by a key is central.

```python
student = {"name": "Aanaa", "grade": "A"}
print(student["name"])
student["passed"] = True
```

## Skills To Build

- Read, add, update, and remove key-value pairs.
- Iterate through `.items()`, `.keys()`, and `.values()`.
- Use `.get()` when a key may be absent.
- Design nested records carefully.
- Count and group values with dictionaries.

## Problem-Solving Method

Choose a key that uniquely identifies each record. Decide what missing keys mean before writing the lookup.

## Common Trap

Accessing a missing key with `data[key]` raises `KeyError`; `.get(key, default)` expresses optional lookup.

## Further Reading

- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [HackerRank Python Dictionaries](https://www.hackerrank.com/domains/python)
