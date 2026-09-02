# Variables And Data Types

This chapter explains how Python names values, identifies their types, converts input, and moves data through a program.

## 1. The Mental Model

A variable is a name bound to an object. The object has a type; the name can later be rebound to another object.

```python
score = 95
score = "ninety-five"
```

The data flow is:

```text
evaluate value -> create or find object -> bind a name -> use the value
```

Python is dynamically typed. This means a name is not permanently restricted to one type, but clear code should still use predictable types.

## 2. Assignment Syntax

```python
name = value
```

```python
name = "Aanaa"
age = 20
height = 1.75
is_student = True
```

Use descriptive `snake_case` names such as `total_price`, not vague names such as `x`.

### Multiple assignment

```python
first_name, last_name = "Aanaa", "Abdella"
x = y = 0

left, right = 10, 20
left, right = right, left
```

The right side is evaluated before the names are updated.

### Naming rules

- Start with a letter or underscore.
- Continue with letters, digits, or underscores.
- Names are case-sensitive.
- Do not use keywords such as `if`, `for`, or `class`.
- Use uppercase names by convention for constants: `MAX_ATTEMPTS = 3`.

## 3. Built-In Data Types

```python
text = "Hello"          # str
whole_number = 42       # int
decimal_number = 3.14   # float
active = True            # bool
nothing = None           # NoneType
items = [1, 2, 3]       # list
coordinates = (10, 20)  # tuple
unique_ids = {1, 2, 3}  # set
profile = {"name": "Aanaa"}  # dict
```

| Need | Type |
| --- | --- |
| Text | `str` |
| Whole-number arithmetic | `int` |
| Fractional measurement | `float` |
| Yes/no state | `bool` |
| Ordered values that change | `list` |
| Fixed ordered record | `tuple` |
| Unique membership | `set` |
| Lookup by label | `dict` |
| Missing result | `None` |

## 4. Inspecting Values And Types

```python
value = 42
print(value)
print(type(value))
print(isinstance(value, int))
print(repr(value))
```

`type()` reports the type. `isinstance()` checks compatible types. `repr()` shows debugging detail, including quotes and whitespace.

## 5. Data Flow: Input To Output

Most beginner programs follow this pipeline:

```text
input text -> conversion -> validation -> calculation -> formatted output
```

```python
price_text = "12.50"
quantity_text = "3"

price = float(price_text)
quantity = int(quantity_text)
if price < 0 or quantity < 0:
    raise ValueError("values cannot be negative")

total = price * quantity
print(f"Total: ${total:.2f}")
```

Step by step:

1. Both input values begin as `str`.
2. `float()` and `int()` create numeric values.
3. Validation rejects impossible values.
4. Arithmetic creates `total`.
5. The f-string formats the result for a person.

Keep the calculation value separate from its display form.

## 6. Input And Conversion

`input()` always returns text, even when the user types digits.

```python
age_text = input("Age: ").strip()

try:
    age = int(age_text)
except ValueError:
    print("Age must be a whole number.")
else:
    print(f"Next year: {age + 1}")
```

Common conversions:

```python
whole = int("42")
decimal = float("3.14")
text = str(42)
```

These fail because the text does not match the target format:

```python
# int("hello")
# int("3.14")
```

### Boolean conversion

```python
bool(0)        # False
bool(1)        # True
bool("")       # False
bool("False")  # True: non-empty text is truthy
```

The string `"False"` is text, not Boolean false.

## 7. Operators And Expressions

```python
x, y = 7, 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)   # 3.5
print(x // y)  # 3
print(x % y)   # 1
print(x ** y)  # 49
```

Use parentheses when they make precedence clear:

```python
first = 10 + 5 * 2       # 20
second = (10 + 5) * 2    # 30
```

`+` and `*` also work with strings: `"ha" * 3` produces `"hahaha"`.

## 8. Equality, Identity, And Membership

```python
first = [1, 2]
second = [1, 2]
print(first == second)  # True: equal contents
print(first is second)  # False: different objects
```

Use `==` for value equality and `is None` for missing values:

```python
result = None
if result is None:
    print("No result")
```

Use `in` for membership:

```python
allowed_roles = {"admin", "editor"}
if "editor" in allowed_roles:
    print("Editing allowed")
```

## 9. Mutability And References

Strings and numbers are immutable: operations create new values.

```python
message = "hello"
message.upper()
print(message)  # hello
message = message.upper()
print(message)  # HELLO
```

Lists and dictionaries are mutable:

```python
numbers = [1, 2]
alias = numbers
alias.append(3)
print(numbers)  # [1, 2, 3]
```

Both names refer to one list. Copy when independent top-level changes are needed:

```python
copy_of_numbers = numbers.copy()
```

## 10. Floating-Point Precision

Some decimal fractions cannot be represented exactly in binary floating point.

```python
print(0.1 + 0.2 == 0.3)  # Often False
```

Use approximate comparison for measurements:

```python
import math
print(math.isclose(0.1 + 0.2, 0.3))
```

For money, consider integer cents or `decimal.Decimal`.

## 11. Complete Example

```python
product_name = input("Product: ").strip()
price_text = input("Price: ").strip()
quantity_text = input("Quantity: ").strip()

try:
    price = float(price_text)
    quantity = int(quantity_text)
except ValueError:
    print("Enter a decimal price and whole-number quantity.")
else:
    if price < 0 or quantity < 0:
        print("Values cannot be negative.")
    else:
        total = price * quantity
        print(f"{product_name}: ${total:.2f}")
```

## 12. Problem-Solving Checklist

Before coding, identify:

1. What values enter the program?
2. What type should each value have?
3. What output is required?
4. Which values are temporary?
5. What happens for empty, invalid, negative, or very large input?
6. Which data type supports the required operations?

When debugging, use `print(repr(value), type(value))`.

## 13. Syntax Reference

```python
variable_name = value
first, second = 1, 2

print(value)
print(type(value))
print(isinstance(value, int))

whole_number = int(text)
decimal_number = float(text)
display_text = str(value)

try:
    number = int(text)
except ValueError:
    print("Invalid number")

if value == expected:
    print("Same value")
if value is None:
    print("Missing")

print(f"Total: {total:.2f}")
```

## Further Reading

- [Python Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Python Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Python Input And Output](https://docs.python.org/3/tutorial/inputoutput.html)
