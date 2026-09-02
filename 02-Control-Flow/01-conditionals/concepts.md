# Conditions And Decisions

## Core Idea

Conditionals choose a path based on Boolean expressions. Python checks `if`, then `elif` branches from top to bottom, and uses `else` when no earlier branch matches.

```python
if score >= 85:
    grade = "A"
elif score >= 60:
    grade = "Pass"
else:
    grade = "Fail"
```

## Skills To Build

- Write precise comparisons and range checks.
- Combine rules with `and`, `or`, and `not`.
- Validate input before making a decision.
- Order overlapping conditions correctly.
- Use `is None` for missing values and `==` for value equality.

## Problem-Solving Method

List every possible outcome and boundary value before writing branches. Test just below, exactly at, and just above every boundary.

## Common Trap

The first matching branch wins. A broad condition placed before a specific one can make the specific branch unreachable.

## Further Reading

- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [HackerRank Python Challenges](https://www.hackerrank.com/domains/python)
