# Loops And Repetition

## Core Idea

A `for` loop processes items in an iterable. A `while` loop repeats while a condition is true.

```python
for number in range(1, 4):
    print(number)

count = 0
while count < 3:
    count += 1
```

## Skills To Build

- Choose `for` for known collections or ranges.
- Choose `while` for changing conditions and sentinel input.
- Track counters, totals, and current best values.
- Use `break` to stop searching and `continue` to skip an item.
- Prove that every `while` loop can terminate.

## Problem-Solving Method

Write the initial state, loop condition, state update, and final result before coding. Trace the first three iterations by hand.

## Common Trap

A `while` loop without progress becomes infinite. Also remember that `range(stop)` excludes `stop`.

## Further Reading

- [Python `for` Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Exercism Python Exercises](https://exercism.org/tracks/python/exercises)
