# Python Conditionals

Conditionals let a program make decisions. They evaluate a condition as `True` or `False`, then choose which block of code to run.

A conditional answers a question such as:

- Is the user old enough?
- Is this number positive?
- Which grade range contains this score?
- Is the username and password valid?

## 1. The Basic Decision

```python
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

The data flow is:

```text
age = 20 -> compare age >= 18 -> True -> run the if block
```

Python runs only one branch of this `if` statement. The indentation shows which statements belong to each branch.

## 2. Boolean Expressions

A condition is an expression that produces `True` or `False`.

```python
print(5 > 3)       # True
print(5 == 3)      # False
print(5 != 3)      # True
print(5 <= 5)      # True
```

Comparison operators:

| Operator | Meaning |
| --- | --- |
| `==` | equal to |
| `!=` | not equal to |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |

Do not confuse assignment with comparison:

```python
score = 80       # Store 80 in score.
score == 80      # Ask whether score equals 80.
```

## 3. `if`, `elif`, and `else`

Use `if` for the first condition, `elif` for additional alternatives, and `else` for everything that did not match.

```python
score = 82

if score >= 85:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(grade)
```

Python checks branches from top to bottom and stops after the first true condition. Order matters.

This is usually wrong:

```python
if score >= 60:
    grade = "C"
elif score >= 85:
    grade = "A"
```

A score of `90` matches `score >= 60` first, so it never reaches the A branch. Put more specific or higher ranges first.

## 4. Combining Conditions

Use `and` when every condition must be true.

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Access granted")
```

Use `or` when at least one condition must be true.

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("The office is closed")
```

Use `not` to reverse a Boolean value.

```python
is_logged_in = False

if not is_logged_in:
    print("Please log in")
```

A useful mental model:

```text
A and B -> both must be True
A or B  -> at least one must be True
not A   -> reverse A
```

Use parentheses when they make the intended grouping clearer:

```python
if (age >= 18 and has_id) or is_admin:
    print("Access granted")
```

## 5. Chained Comparisons

Python allows readable range checks:

```python
score = 78

if 0 <= score <= 100:
    print("Valid score")
```

This means `0 <= score and score <= 100`.

For grading, use non-overlapping ranges:

```python
if 85 <= score <= 100:
    grade = "A"
elif 75 <= score < 85:
    grade = "B"
elif 60 <= score < 75:
    grade = "C"
else:
    grade = "F"
```

Validate invalid values before using the ranges:

```python
if not 0 <= score <= 100:
    print("Invalid score")
elif score >= 85:
    print("A")
else:
    print("Below A")
```

## 6. Truthy and Falsy Values

Python can use values directly as conditions. These values are commonly falsy:

- `False`
- `None`
- `0` and `0.0`
- `""` (empty string)
- `[]`, `{}`, and `()` (empty collections)

Most other values are truthy.

```python
username = input("Username: ").strip()

if username:
    print(f"Welcome, {username}")
else:
    print("Username cannot be empty")
```

For exact Boolean comparison, use `is` for `True` or `False` only when necessary. Usually this is clearer:

```python
if is_active:
    print("Active")
```

Use `is None` when checking for `None`:

```python
if result is None:
    print("No result")
```

## 7. Nested Conditionals

A conditional can contain another conditional.

```python
age = 22
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Enter the event")
    else:
        print("Buy a ticket first")
else:
    print("You are too young")
```

Nested code can become difficult to read. Sometimes a combined condition is clearer:

```python
if age >= 18 and has_ticket:
    print("Enter the event")
```

Use nesting when the second decision only makes sense after the first decision succeeds.

## 8. Conditional Expressions

For a very small choice, use a conditional expression:

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)
```

Do not use a conditional expression for several branches or complicated logic. A normal `if` statement is easier to read in those cases.

## 9. Membership and Identity

Use `in` to check whether a value exists in a collection or string.

```python
allowed_roles = ["admin", "editor"]
role = "editor"

if role in allowed_roles:
    print("Can edit")
```

Use `not in` for the opposite:

```python
if username not in blocked_users:
    print("Account is available")
```

Use `is` for object identity, especially `None`. Use `==` for value equality.

```python
first_list = [1, 2]
second_list = [1, 2]

print(first_list == second_list)  # True: same values
print(first_list is second_list)  # False: different objects
```

## 10. Input, Conversion, and Validation

`input()` always returns a string. Convert it before numeric comparisons.

```python
age_text = input("Enter your age: ")

try:
    age = int(age_text)
except ValueError:
    print("Please enter a whole number.")
else:
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
```

A reliable input flow is:

```text
input text -> convert type -> validate range -> make decision -> display result
```

Separate validation from the decision when the program grows:

```python
def is_valid_score(score):
    return 0 <= score <= 100


def get_grade(score):
    if not is_valid_score(score):
        return "Invalid score"
    if score >= 85:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    return "F"
```

## 11. Short-Circuit Evaluation

Python may stop evaluating a combined condition as soon as its result is known.

With `and`, a false first condition is enough:

```python
if user is not None and user.is_active:
    print("Active user")
```

Python checks `user.is_active` only if `user is not None` is true. This prevents an error when `user` is `None`.

With `or`, a true first condition is enough:

```python
name = entered_name or "Guest"
```

If `entered_name` is empty, `name` becomes `"Guest"`.

## 12. How to Solve Conditional Problems

1. List the possible outcomes.
2. Identify the input values needed for the decision.
3. Write the boundary rules exactly.
4. Order conditions from most specific or highest priority to lowest.
5. Handle invalid input explicitly.
6. Test values at every boundary.

For a grading problem, test:

```text
-1, 0, 59, 60, 74, 75, 84, 85, 100, 101
```

Boundary testing finds errors such as using `>` when `>=` was required.

## 13. Common Conditional Mistakes

### Using `=` instead of `==`

`=` assigns a value; `==` compares values.

### Forgetting that input is text

`int(input(...))` or another conversion is needed before numeric comparison.

### Overlapping branches

A broad condition placed first can prevent later branches from running.

### Incorrect Boolean logic

Write the sentence first. For example, "age is at least 18 and has an ID" becomes `age >= 18 and has_id`.

### Comparing with `is`

Use `==` for values and `is None` for `None`.

### Deep nesting

Combine conditions or extract a helper function when nesting makes the path hard to follow.

## 14. Practice Questions

### Simple

1. Write a program that prints whether a number is positive, negative, or zero.
2. Write `is_even(number)` using a conditional.
3. Check whether a person is old enough to vote.

### Easy

1. Write `find_largest(first_number, second_number, third_number)` without using `max()`.
2. Write a temperature classifier for cold, warm, and hot ranges.
3. Check whether a character is a vowel or consonant.
4. Validate that a username is not empty.

### Intermediate

1. Build a grade calculator with valid scores from 0 to 100.
2. Write an admission decision using age, exam score, and payment status.
3. Create a simple login check with a maximum of three possible outcomes: success, wrong password, or unknown user.
4. Write a shipping-cost calculator based on destination and order total.

### Expert

1. Build a permission system for roles `admin`, `editor`, and `viewer` without repeating conditions.
2. Write a function that classifies a triangle as equilateral, isosceles, scalene, or invalid.
3. Design a discount function where the best eligible discount is selected from several rules.
4. Refactor deeply nested decision code into small functions with clear names.

## 15. Trick Questions

Predict the output before running each example.

### Trick 1: `and` returns an operand

```python
result = "hello" and 0
print(result)
```

Answer: `0`. `and` stops at the first falsy value and returns it.

### Trick 2: `or` returns an operand

```python
name = "" or "Guest"
print(name)
```

Answer: `Guest`. `or` returns the first truthy value.

### Trick 3: Branch order matters

```python
score = 90

if score >= 50:
    print("Pass")
elif score >= 85:
    print("Excellent")
```

Answer: `Pass`. The first true branch ends the chain.

### Trick 4: `input()` returns text

```python
age = input("Age: ")
if age >= "18":
    print("Adult")
```

The comparison is a string comparison, not a numeric comparison. Convert with `int()` after validating the input.

### Trick 5: `==` versus `is`

```python
first = [1, 2]
second = [1, 2]
print(first == second)
print(first is second)
```

Answer: `True`, then `False`. The lists have equal contents but are different objects.

### Trick 6: `not` changes the Boolean result

```python
items = []
if not items:
    print("No items")
```

Answer: `No items`. An empty list is falsy.

## 16. Final Syntax Reference

```python
if condition:
    statement()
elif another_condition:
    other_statement()
else:
    fallback_statement()


if first_condition and (second_condition or third_condition):
    print("All required rules passed")


result = value_if_true if condition else value_if_false


try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")
else:
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
```
