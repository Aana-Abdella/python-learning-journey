# Lists

## Core Idea

A list is an ordered, mutable collection. It is a good choice when order matters and items may change.

```python
numbers = [3, 1, 2]
numbers.append(4)
numbers.sort()
print(numbers)
```

## Skills To Build

- Index and slice safely.
- Add, remove, replace, and sort items.
- Iterate without losing track of the current item.
- Use list comprehensions for simple transformations.
- Copy a list intentionally with `list(items)` or `items.copy()`.

## Problem-Solving Method

Identify whether the task needs order, duplicates, mutation, or fast membership. Then choose the operation that directly expresses the requirement.

## Common Trap

Do not remove items from a list while iterating over that same list; filter into a new list instead.

## Further Reading

- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Exercism Python Exercises](https://exercism.org/tracks/python/exercises)
