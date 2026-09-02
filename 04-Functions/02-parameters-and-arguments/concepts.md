# Parameters And Arguments

## Core Idea

Parameters describe the inputs a function accepts. Arguments are the values supplied at the call site.

```python
def introduce(name, age):
    return f"{name} is {age}."

introduce("Aanaa", 20)
introduce(name="Aanaa", age=20)
```

## Skills To Build

- Use positional and keyword arguments clearly.
- Put required parameters before optional ones.
- Keep interfaces small and meaningful.
- Understand argument binding and `TypeError` messages.

## Problem-Solving Method

Write the contract as a table of parameter name, expected type, required status, and meaning. Reject ambiguous interfaces.

## Common Trap

Do not provide the same parameter twice, such as `introduce("Aanaa", name="Maya", age=20)`.

## Further Reading

- [Python Function Arguments](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [Codewars Python Kata](https://www.codewars.com/kata/search/python)
