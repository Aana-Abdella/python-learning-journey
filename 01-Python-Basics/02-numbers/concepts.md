# Numbers And Arithmetic

## Core Idea

Python supports integers and floating-point numbers, with arithmetic operators for addition, subtraction, multiplication, division, floor division, remainder, and powers.

```python
x, y = 10, 3
print(x + y)
print(x / y)
print(x // y)
print(x % y)
print(x ** 2)
```

`/` produces a true-division result. `//` produces floor division. `%` is useful for divisibility and repeating patterns.

## Skills To Build

- Track operator precedence with parentheses.
- Choose a numeric type appropriate to the data.
- Round only when displaying results, not prematurely during calculations.
- Use `%` to detect even numbers and cycles.
- Check for division by zero.

## Problem-Solving Method

Translate the word problem into variables and formulas. Calculate intermediate values with descriptive names. Verify the formula with a small hand-worked example.

## Common Trap

Floating-point values can contain small representation errors. Use a tolerance when comparing calculated decimals.

## Further Reading

- [Python Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [HackerRank Python: Math](https://www.hackerrank.com/domains/python)
