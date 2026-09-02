# Function Design

## Core Idea

Good function design makes data flow visible: input enters, one responsibility runs, and a predictable result leaves.

```python
def calculate_average(scores):
    if not scores:
        raise ValueError("scores cannot be empty")
    return sum(scores) / len(scores)
```

## Skills To Build

- Separate input, validation, calculation, and display.
- Prefer pure functions for business rules.
- Name functions after actions or results.
- Keep side effects at the program boundary.
- Raise clear errors for invalid input.

## Problem-Solving Method

Draw the call graph before coding. If one function has several unrelated responsibilities, split it at the responsibility boundary.

## Common Trap

A function that reads input, calculates, prints, and changes global state is hard to reuse and test.

## Further Reading

- [Python Function Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Exercism Python Exercises](https://exercism.org/tracks/python/exercises)
