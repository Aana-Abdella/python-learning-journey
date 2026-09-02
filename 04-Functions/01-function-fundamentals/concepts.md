# Function Fundamentals

## Core Idea

A function packages one responsibility behind a name. Inputs enter through parameters and a result leaves through `return`.

```python
def add(first_number, second_number):
    return first_number + second_number
```

## Skills To Build

- Define and call functions correctly.
- Distinguish a returned value from printed output.
- Keep local variables local.
- Compose small functions into a workflow.
- Write functions that are easy to test.

## Problem-Solving Method

State the function contract first: inputs, output, rules, and errors. Then write one example call and one edge-case call.

## Common Trap

A function that prints a result returns `None` unless it also uses `return`.

## Further Reading

- [Python Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Exercism Python Exercises](https://exercism.org/tracks/python/exercises)
