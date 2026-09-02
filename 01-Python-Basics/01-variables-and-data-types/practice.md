# Variables And Data Types: Expert Practice

Use this as a deliberate practice lab. Do not search for a solution first. Write the input, output, type contract, algorithm, and edge cases.

## Practice Cycle

1. Predict one small example.
2. Write the type of each input and output.
3. Implement the smallest correct version.
4. Test normal, boundary, and invalid cases.
5. Explain one design choice.
6. Refactor only after tests pass.

Keep a mistake log with `symptom -> cause -> rule learned`.

## Level 1: Simple

1. Create variables for your name, age, height, and student status. Print values and types.
2. Convert `"25"` to an integer and print next year's age.
3. Convert Celsius to Fahrenheit.
4. Ask for two numbers and print sum, difference, product, and quotient.
5. Swap two variables without a third variable.

### Worked example

```python
celsius = 20
fahrenheit = (celsius * 9 / 5) + 32
print(fahrenheit)
```

## Level 2: Easy

1. Build a safe age converter that handles non-numeric text.
2. Calculate a product total from price and quantity with two decimal places.
3. Predict the type and value of `"5" * 2`, `5 * 2`, and `5.0 * 2`.
4. Report whether text is empty after `.strip()`.
5. Build a score summary using `int`, `float`, and formatted output.

## Level 3: Intermediate

1. Build a receipt accepting product, price, quantity, discount, and tax. Validate all numeric boundaries.
2. Create a kilometer/mile and Celsius/Fahrenheit converter. Reject unknown units.
3. Write `parse_value(text)` that returns an integer, decimal, Boolean, or unchanged text.
4. Parse comma-separated scores and report invalid entries without stopping valid entries.
5. Compare two records and report differing fields and types.

## Level 4: Expert Challenges

### 1. Typed configuration loader

Create `parse_config(raw_config, schema)`.

```python
schema = {
    "debug": bool,
    "port": int,
    "timeout": float,
    "app_name": str,
}
```

Requirements:

- Return a new dictionary; do not mutate input.
- Accept `true` and `false` case-insensitively.
- Raise clear errors for unknown keys and invalid values.
- Include the key name in every error.

### 2. Exact money calculator

Build a receipt calculator that accepts prices such as `"12.50"`, applies discount and tax, and avoids floating-point surprises. Choose integer cents or `Decimal`, explain why, and test one-cent, zero, and large values.

### 3. Deep comparison

Write `compare_values(left, right, path="root")` for nested dictionaries and lists.

Expected style:

```text
root.user.age: 20 (int) != "20" (str)
```

Detect different types, missing keys, and list indexes without modifying either input.

### 4. Immutable profile update

Write `update_profile(profile, **changes)` that returns a new profile without changing the original. Test nested data and document whether the copy is shallow or deep.

### 5. Data-flow refactor

Choose an existing script and divide it into:

```text
read_input -> convert_input -> validate_input -> calculate_result -> display_result
```

Document the type at every stage and test invalid input.

## Tricky Questions

Predict before running:

```python
value = "10"
print(value + "5")
print(int(value) + 5)
```

```python
items = [1, 2]
alias = items
copy = items.copy()
alias.append(3)
copy.append(4)
print(items)
print(copy)
```

```python
print(bool("False"))
print(bool(0))
print(bool([]))
```

Answers: `105` then `15`; `[1, 2, 3]` then `[1, 2, 4]`; and `True`, `False`, `False`.

## Test Matrix

| Case | Example |
| --- | --- |
| Normal | `"42"` |
| Empty | `""` |
| Whitespace | `" 42 "` |
| Invalid text | `"four"` |
| Decimal text | `"4.2"` |
| Zero | `"0"` |
| Negative | `"-3"` |
| Very large | near the program limit |

## Website Practice

- [Exercism Python Track](https://exercism.org/tracks/python/exercises)
- [HackerRank Python](https://www.hackerrank.com/domains/python)
- [Codewars Python Kata](https://www.codewars.com/kata/search/python)
- [Python Built-in Types](https://docs.python.org/3/library/stdtypes.html)

Solve locally first. Compare approaches only after you can explain your own solution.

## Mastery Check

You are ready to continue when you can explain names, objects, types, conversion, identity, equality, mutability, validation, and complete input-to-output data flow.
