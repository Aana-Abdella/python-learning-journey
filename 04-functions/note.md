# Python Functions

Functions are named, reusable blocks of code that perform one focused job. They help you write code that is easier to read, test, reuse, and change.

A good function usually:

- Has one clear responsibility.
- Receives data through parameters.
- Does its work locally.
- Returns a useful result.
- Avoids unexpected changes outside itself.
- Has a name that describes an action or result.

Examples from this folder include `add`, `subtract`, `calculate_average`, `get_grade`, and `is_passed`.

## 1. Why Use Functions?

Without functions, the same logic may be repeated in many places:

```python
first_total = 10 + 5
second_total = 20 + 8
third_total = 4 + 7
```

With a function, the operation is defined once:

```python
def add(first_number, second_number):
    return first_number + second_number

first_total = add(10, 5)
second_total = add(20, 8)
third_total = add(4, 7)
```

Benefits:

1. **Reuse:** call the same logic many times.
2. **Readability:** a meaningful name explains what the code does.
3. **Maintenance:** fix the logic in one place.
4. **Testing:** test one small behavior at a time.
5. **Abstraction:** callers do not need to know every internal step.

## 2. Function Anatomy

```python
def function_name(parameter1, parameter2):
    """Optional description of the function."""
    result = parameter1 + parameter2
    return result
```

Parts of a function:

- `def`: tells Python that a function is being defined.
- `function_name`: the name used to call the function.
- Parameters: variable names that receive input.
- `:`: starts the function body.
- Indented body: the instructions run by the function.
- `return`: sends a value back to the caller.
- Docstring: explains the purpose, inputs, and output.

A function definition does not run the body immediately. It creates the function. The body runs when the function is called.

```python
def say_hello():
    print("Hello")

say_hello()  # The function runs here.
```

## 3. Parameters and Arguments

A **parameter** is the name in the function definition. An **argument** is the actual value passed during a call.

```python
def greet(name):       # name is a parameter
    return f"Hello, {name}!"

message = greet("Aanaa")  # "Aanaa" is an argument
```

### Positional arguments

Values are matched by their position:

```python
def describe_person(name, age):
    return f"{name} is {age} years old."

print(describe_person("Aanaa", 20))
```

### Keyword arguments

Values are matched by parameter name. This improves readability and allows arguments to appear in a different order.

```python
def create_account(username, email, active=True):
    return {
        "username": username,
        "email": email,
        "active": active,
    }

account = create_account(
    email="aanaa@example.com",
    username="aanaa",
)
```

### Default parameters

A default value is used when the caller does not provide that argument.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Aanaa"))             # Hello, Aanaa!
print(greet("Aanaa", "Welcome"))  # Welcome, Aanaa!
```

Required parameters should normally come before parameters with defaults:

```python
def connect(host, port=5432):
    return f"Connecting to {host}:{port}"
```

## 4. How Data Flows Through a Function

Think of a function as a small pipeline:

```text
caller data
    |
    v
arguments -> parameters -> local processing -> return value -> caller
                                             |
                                             +-> optional side effect
                                                such as print or file write
```

Example:

```python
def calculate_average(math_score, english_score, programming_score):
    total = math_score + english_score + programming_score
    average = total / 3
    return average

average = calculate_average(100, 85, 95)
print(average)
```

The flow is:

1. The caller sends `100`, `85`, and `95`.
2. Python assigns them to the three parameters.
3. The function creates local values `total` and `average`.
4. `return average` sends `93.333...` back.
5. The caller stores that result in `average`.

The function does not automatically know about variables in the caller. Data should usually enter through parameters and leave through `return`.

## 5. `return` Versus `print`

`print` displays a value. `return` gives a value back so another part of the program can use it.

```python
def show_double(number):
    print(number * 2)

result = show_double(5)
print(result)  # None
```

The function printed `10`, but it did not return `10`.

```python
def get_double(number):
    return number * 2

result = get_double(5)
print(result)  # 10
```

Use `return` when the result should be stored, compared, combined, or passed to another function. Use `print` at the user-interface boundary when the result only needs to be displayed.

A function without an explicit `return` returns `None`.

## 6. Function Composition

Function composition means using the output of one function as the input of another.

```python
def calculate_average(math_score, english_score, programming_score):
    return (math_score + english_score + programming_score) / 3


def get_grade(average):
    if 85 <= average <= 100:
        return "A"
    if 75 <= average < 85:
        return "B"
    if 70 <= average < 75:
        return "C"
    if 60 <= average < 70:
        return "D"
    if 0 <= average < 60:
        return "F"
    return "Invalid score"

average = calculate_average(100, 85, 95)
grade = get_grade(average)
print(grade)
```

The data flow is:

```text
scores -> calculate_average -> average -> get_grade -> grade
```

Small functions can be combined to create a larger feature without making one giant function.

## 7. Local Scope and Global Scope

A variable created inside a function is local to that function.

```python
def make_message():
    message = "Finished"
    return message

result = make_message()
print(result)
# print(message)  # NameError: message is local to the function
```

A variable defined outside a function is global to that module. Reading a global value is possible, but changing global state makes code harder to understand and test.

Prefer this:

```python
def calculate_total(price, tax_rate):
    return price + (price * tax_rate)
```

Instead of relying on a global value:

```python
TAX_RATE = 0.15


def calculate_total(price):
    return price + (price * TAX_RATE)
```

Use parameters for values that can change or that make the function easier to reuse.

## 8. Mutable Values and Side Effects

Lists and dictionaries can be changed inside a function. This is called mutation.

```python
def add_task(tasks, task):
    tasks.append(task)
    return tasks

my_tasks = []
add_task(my_tasks, "Study functions")
print(my_tasks)
```

This is valid, but the caller's list changes. Make that behavior clear through the function name and documentation.

Avoid a mutable object as a default parameter:

```python
# Avoid this.
def add_task(task, tasks=[]):
    tasks.append(task)
    return tasks
```

The same list is reused between calls. Use `None` instead:

```python
def add_task(task, tasks=None):
    if tasks is None:
        tasks = []
    tasks.append(task)
    return tasks
```

A side effect is an action that affects something outside the function, such as printing, changing a list, writing a file, or updating a database. Side effects are sometimes necessary, but functions that calculate and return values are generally easier to test.

## 9. Type Hints and Docstrings

Type hints document the expected types. They do not automatically validate values at runtime.

```python
def calculate_discount(price: float, percent: float) -> float:
    return price * (percent / 100)
```

A docstring can explain the contract of a function:

```python
def calculate_discount(price: float, percent: float) -> float:
    """Return the discount amount for a price and percentage."""
    return price * (percent / 100)
```

A useful contract answers:

- What does the function do?
- What inputs does it accept?
- What does it return?
- What happens for invalid input?

## 10. Validation and Errors

Validate data at the boundary where it enters your program.

```python
def get_grade(average):
    if not 0 <= average <= 100:
        raise ValueError("average must be between 0 and 100")

    if average >= 85:
        return "A"
    if average >= 75:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"
```

The caller can handle the error:

```python
try:
    grade = get_grade(105)
except ValueError as error:
    print(f"Invalid input: {error}")
```

Do not silently return a misleading result for invalid data. Choose a clear policy: validate and raise an error, return a special value, or ask the user for corrected input.

## 11. `*args` and `**kwargs`

Use `*args` when a function accepts any number of positional arguments.

```python
def add_many(*numbers):
    return sum(numbers)

print(add_many(2, 3, 5, 10))
```

Inside the function, `numbers` is a tuple.

Use `**kwargs` when a function accepts any number of keyword arguments.

```python
def show_settings(**settings):
    for name, value in settings.items():
        print(f"{name}: {value}")

show_settings(theme="dark", font_size=14)
```

Inside the function, `settings` is a dictionary. Use these features when variable input is part of the design, not just to avoid choosing clear parameters.

## 12. Functions as Values

In Python, functions can be stored in variables, passed to other functions, and returned from functions.

```python
def square(number):
    return number * number

operation = square
print(operation(4))
```

A function that receives another function is a higher-order function:

```python
def apply_operation(number, operation):
    return operation(number)

print(apply_operation(5, square))
```

A short one-use function can be written with `lambda`, but a normal `def` function is usually clearer for reusable logic.

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda number: number * number, numbers))
```

## 13. Recursion

A recursive function calls itself. It needs:

1. A base case that stops recursion.
2. A recursive case that moves toward the base case.

```python
def countdown(number):
    if number == 0:
        print("Done")
        return

    print(number)
    countdown(number - 1)
```

Use a loop when it is simpler. Recursion is useful for naturally nested problems such as tree structures, but careless recursion can cause infinite calls or a recursion limit error.

## 14. Modules and Calling Other Functions

A module is a Python file. Import functions from another file to reuse them.

```python
# calculator.py
def add(first_number, second_number):
    return first_number + second_number
```

```python
# app.py
from calculator import add

print(add(5, 3))
```

Use a main guard when a file contains both reusable functions and runnable example code:

```python
def main():
    print("Program started")


if __name__ == "__main__":
    main()
```

This lets another file import the functions without automatically running the example program.

## 15. How to Solve Function Problems

Use this process for almost every exercise:

### Step 1: Understand the contract
Write down the inputs, output, and rules.

```text
Input: a list of numbers
Output: the largest number
Rule: do not sort the list
```

### Step 2: Choose the function signature
Give the function the smallest useful interface.

```python
def find_largest(numbers):
    pass
```

### Step 3: Work through one example by hand
For `[4, 9, 2]`, start with `4`, compare with `9`, keep `9`, compare with `2`, keep `9`.

### Step 4: Write the simplest algorithm
Do not optimize before the basic behavior is correct.

### Step 5: Return the result
Avoid hiding the answer inside a `print` unless displaying output is the function's specific job.

### Step 6: Test normal and edge cases
Check empty input, one item, duplicate values, negative values, zero, and invalid input when relevant.

### Step 7: Improve naming and structure
If a function is difficult to explain, it may be doing too many jobs. Split it into smaller functions.

## 16. Testing Functions

A direct test compares the returned result with the expected result.

```python
def multiply(first_number, second_number):
    return first_number * second_number

assert multiply(3, 4) == 12
assert multiply(0, 10) == 0
assert multiply(-2, 3) == -6
```

For a function that raises an error:

```python
def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("divisor cannot be zero")
    return dividend / divisor

try:
    divide(10, 0)
except ValueError:
    pass
else:
    raise AssertionError("divide should reject zero")
```

Tests make the function's expected behavior visible and protect it during future changes.

## 17. Common Mistakes

### Forgetting parentheses when calling

```python
print(greet)    # Function object
print(greet())  # Calls the function, if no arguments are required
```

### Forgetting `return`

```python
def add(first_number, second_number):
    first_number + second_number  # The result is discarded
```

### Returning too early

Code after `return` in the same path does not run.

### Mixing input, calculation, and output unnecessarily

A reusable function should usually calculate and return. Keep `input()` and final `print()` in the program flow or a separate interface function.

### Using unclear names

Prefer `calculate_average(scores)` over `do_it(values)`.

### Making one giant function

Separate input handling, validation, calculation, and display when each part has a different responsibility.

### Using too many parameters

If a function needs many related values, consider a list, dictionary, or class. Do not group unrelated values just to shorten the code.

## 18. Practice Questions

Attempt each question before looking at an implementation. Write the function first, then write calls that prove it works.

### Simple

1. Write `say_hello()` that prints `Hello, Python!`.
2. Write `double(number)` that returns twice the given number.
3. Write `is_even(number)` that returns `True` for even numbers and `False` for odd numbers.

### Easy

1. Write `find_largest(first_number, second_number)` without using `max()`.
2. Write `count_vowels(text)` that returns the number of vowels in a string.
3. Write `calculate_total(price, quantity)` and return the price multiplied by quantity.
4. Write `greet(name, greeting="Hello")` using a default parameter.

### Intermediate

1. Write `calculate_average(numbers)` that returns the average of a list. Decide what should happen for an empty list.
2. Write `get_grade(average)` using the ranges A, B, C, D, and F. Reject scores below 0 or above 100.
3. Write `remove_duplicates(items)` that returns a new list while preserving the original order.
4. Write `calculate_cart_total(items, tax_rate)` where each item is a dictionary containing `price` and `quantity`.
5. Split a student grade program into functions for input, average calculation, grade calculation, pass/fail status, and display.

### Expert

1. Write `compose(first_function, second_function)` so that the result applies `first_function` and then `second_function`.
2. Write a memoized recursive function that calculates Fibonacci numbers efficiently.
3. Write `validate_student(student)` that checks required fields, score ranges, and data types, raising clear `ValueError` messages.
4. Design a function-based expense tracker that can add an expense, remove an expense, calculate totals by category, and return a monthly summary without using global mutable state.
5. Refactor a large program so that pure calculation functions are separated from input and output functions. Explain how data flows between each function.

## 19. Final Syntax Reference

```python
def function_name(required_parameter, optional_parameter="default"):
    """Describe the function's purpose and returned value."""
    if required_parameter is None:
        raise ValueError("required_parameter is required")

    result = do_work(required_parameter, optional_parameter)
    return result


def do_work(value, option):
    return value


answer = function_name("data")
print(answer)

# Positional and keyword arguments
function_name("data", "custom")
function_name(required_parameter="data", optional_parameter="custom")

# Flexible arguments
def flexible_function(*args, **kwargs):
    return args, kwargs

# Main program entry point
if __name__ == "__main__":
    print(function_name("data"))
```
