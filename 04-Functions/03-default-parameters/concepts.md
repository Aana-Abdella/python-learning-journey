# Default Parameters

## Core Idea

A default parameter supplies a value when the caller omits that argument.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

Defaults make common calls short while preserving customization.

## Skills To Build

- Choose safe immutable defaults such as strings, numbers, and `None`.
- Use `None` when a fresh list or dictionary is needed per call.
- Keep defaults after required parameters.
- Explain when a default is evaluated.

## Problem-Solving Method

Write both the omitted-argument and explicit-argument calls. Check that each call receives independent state.

## Common Trap

Never use `items=[]` or `settings={}` as a default when the function mutates it. The object is shared between calls.

## Further Reading

- [Python Default Argument Values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)
- [HackerRank Python Functions](https://www.hackerrank.com/domains/python)
