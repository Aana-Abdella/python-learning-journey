# Variables And Data Types

## Core Idea

A variable is a name bound to a value. Python values have types such as `str`, `int`, `float`, `bool`, `list`, `tuple`, `set`, and `dict`.

```python
text = "Hello"
number = 42
decimal = 3.14
is_active = True

print(type(text))
```

Think in three steps: name -> value -> type.

## Skills To Build

- Choose meaningful variable names.
- Distinguish assignment (`=`) from comparison (`==`).
- Convert values with `int()`, `float()`, and `str()`.
- Use `type()` while learning and debugging.
- Understand that Python is dynamically typed: a name can later be bound to another type.

## Problem-Solving Method

Write the data table before coding. Record each input, its type, and the required output. Test zero, negative numbers, empty text, and unexpected text.

## Common Trap

`input()` returns a string. Convert it before doing numeric arithmetic or comparisons.

## Further Reading

- [Python Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Exercism: Python concept exercises](https://exercism.org/tracks/python/concepts)
