# Object-Oriented Programming

## Core Idea

A class defines a type. An object is an instance of that type with state and behavior.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
```

## Skills To Build

- Design classes around a clear responsibility.
- Initialize instance state in `__init__`.
- Use `self` to access instance data.
- Keep methods small and cohesive.
- Prefer composition when inheritance does not express a true relationship.

## Problem-Solving Method

Identify nouns as possible objects and verbs as possible methods. Define the minimum state required for each behavior.

## Common Trap

Do not create a class merely to hold unrelated functions. Start with a function unless an object needs persistent state or a shared interface.

## Further Reading

- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- [Exercism Python Exercises](https://exercism.org/tracks/python/exercises)
