# Variables And Data Types: Practice Lab

## Learn Faster

Use a prediction table before running code:

| Expression | Predicted type | Predicted value |
| --- | --- | --- |
| `42` | `int` | `42` |
| `3.14` | `float` | `3.14` |
| `"42"` | `str` | `"42"` |
| `bool(0)` | `bool` | `False` |

Change one value at a time and explain the result aloud. This builds type awareness faster than rereading definitions.

## Tricky Problems

1. Predict the type of `"7"`, `7`, and `7.0`.
2. Explain why `"2" + "3"` differs from `2 + 3`.
3. Build a converter that accepts a text number and reports whether it is an integer or decimal.
4. Find the type and value after `value = 5; value = "five"`.

## Method

When an error appears, inspect the value and type immediately with `print(repr(value), type(value))`. Then decide whether conversion belongs at the input boundary.

## Website Practice

- [Exercism: Python concepts](https://exercism.org/tracks/python/concepts)
- [HackerRank: Python Introduction](https://www.hackerrank.com/domains/python)

## Completion Check

You can explain assignment, conversion, truth values, and the difference between a value's display and its type.
