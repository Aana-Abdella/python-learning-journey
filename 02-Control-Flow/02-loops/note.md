# Python Loops

Loops repeat a block of code. They are useful when the same operation must run for every item in a collection or until a condition changes.

Python has two main loops:

- `for`: repeat for each item in an iterable.
- `while`: repeat while a condition remains true.

## 1. Why Use Loops?

Without a loop, repeated work becomes repetitive:

```python
print("1 squared is", 1 * 1)
print("2 squared is", 2 * 2)
print("3 squared is", 3 * 3)
```

A loop expresses the pattern once:

```python
for number in range(1, 4):
    print(number, "squared is", number * number)
```

The data flow is:

```text
collection or range -> next item -> loop body -> next item -> ... -> finished
```

## 2. The `for` Loop

A `for` loop assigns each item to a loop variable, one at a time.

```python
names = ["Aanaa", "Maya", "Noah"]

for name in names:
    print(f"Hello, {name}!")
```

The loop runs three times:

```text
name = "Aanaa" -> print
name = "Maya"  -> print
name = "Noah"  -> print
```

The variable `name` is updated automatically at the start of each iteration.

## 3. The `range()` Function

`range()` produces a sequence of numbers. The stop value is not included.

```python
for number in range(5):
    print(number)  # 0, 1, 2, 3, 4
```

Forms of `range`:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Examples:

```python
for number in range(2, 6):
    print(number)  # 2, 3, 4, 5

for number in range(0, 10, 2):
    print(number)  # 0, 2, 4, 6, 8

for number in range(5, 0, -1):
    print(number)  # 5, 4, 3, 2, 1
```

Common mistake: `range(1, 5)` does not include `5`.

## 4. Looping Through Common Collections

### Strings

```python
for character in "Python":
    print(character)
```

### Lists

```python
scores = [80, 92, 75]

for score in scores:
    print(score)
```

### Dictionaries

```python
student = {"name": "Aanaa", "grade": "A"}

for key, value in student.items():
    print(key, value)
```

Use `.keys()` for keys and `.values()` for values when that expresses the intent more clearly.

### Sets

```python
colors = {"red", "blue", "green"}

for color in colors:
    print(color)
```

Sets do not guarantee a useful display order. Do not write code that depends on the order of a set.

## 5. `enumerate()`

Use `enumerate()` when you need both an index and a value.

```python
names = ["Aanaa", "Maya", "Noah"]

for index, name in enumerate(names, start=1):
    print(index, name)
```

Prefer this over manually maintaining an index counter. It keeps the index and item synchronized.

## 6. `zip()`

Use `zip()` to process corresponding items from multiple iterables.

```python
names = ["Aanaa", "Maya"]
scores = [95, 88]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

`zip()` stops when the shortest iterable ends.

## 7. The `while` Loop

A `while` loop repeats while its condition is true.

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

A while loop has three important parts:

1. Initial state: `count = 1`.
2. Condition: `count <= 3`.
3. Progress update: `count += 1`.

Without progress, the condition may never become false and the loop can run forever.

## 8. Sentinel Loops

A sentinel is a special value that tells a loop to stop.

```python
while True:
    command = input("Enter a command, or quit: ").strip().lower()

    if command == "quit":
        break

    print(f"You entered: {command}")
```

The loop is intentionally infinite until the sentinel command is received. Make the stopping rule obvious.

## 9. `break` and `continue`

`break` exits the nearest loop immediately.

```python
numbers = [3, 7, 10, 12]

for number in numbers:
    if number == 10:
        break
    print(number)
```

This prints `3` and `7`.

`continue` skips the rest of the current iteration and starts the next one.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

This prints `1`, `2`, `4`, and `5`.

Use `break` when the answer has been found. Use `continue` when one item should be skipped.

## 10. Loop `else`

A loop `else` block runs when the loop finishes normally, not when it exits through `break`.

```python
numbers = [2, 4, 6, 8]

for number in numbers:
    if number % 2 != 0:
        print("Found an odd number")
        break
else:
    print("No odd numbers found")
```

This is useful for search problems. The `else` means that no `break` happened.

A `while` loop can also have an `else` block:

```python
attempts = 0
while attempts < 3:
    attempts += 1
else:
    print("All attempts used")
```

## 11. Accumulators and Counters

An accumulator stores a running result.

```python
prices = [10, 5, 8]
total = 0

for price in prices:
    total += price

print(total)
```

A counter records how many times something happens.

```python
scores = [55, 80, 92, 40]
passed_count = 0

for score in scores:
    if score >= 60:
        passed_count += 1

print(passed_count)
```

Initialize the accumulator or counter before the loop, update it inside the loop, and use it after the loop.

## 12. Building a New Collection

Start with an empty collection and add transformed values.

```python
numbers = [1, 2, 3, 4]
squares = []

for number in numbers:
    squares.append(number * number)

print(squares)
```

For simple transformations, a list comprehension is a concise alternative:

```python
squares = [number * number for number in numbers]
```

Use a normal loop when the logic has multiple steps, validation, side effects, or complex branching.

## 13. Nested Loops

A nested loop is a loop inside another loop.

```python
for row in range(1, 3):
    for column in range(1, 4):
        print(f"({row}, {column})")
```

For every outer iteration, the inner loop completes all its iterations. If the outer loop runs 2 times and the inner loop runs 3 times, the body runs 6 times.

Nested loops are useful for grids and tables, but they can become slow for large inputs.

## 14. Modifying Collections While Looping

Changing a list while iterating over it can skip items or produce confusing behavior.

Avoid this:

```python
numbers = [1, 2, 3, 4]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)
```

Build a new list instead:

```python
numbers = [1, 2, 3, 4]
odd_numbers = [number for number in numbers if number % 2 != 0]
```

Or iterate over a copy when in-place removal is required:

```python
for number in numbers.copy():
    if number % 2 == 0:
        numbers.remove(number)
```

## 15. How to Solve Loop Problems

1. Identify what must repeat.
2. Choose `for` when processing known items or a known range.
3. Choose `while` when repetition depends on a changing condition or user input.
4. Name the loop variable after the item it represents.
5. Identify state such as a total, counter, current best value, or attempt count.
6. Write the stopping condition before writing the loop body.
7. Trace the first few iterations by hand.
8. Test empty input, one item, many items, and boundary values.

Example: find the first number greater than 50.

```python
def find_first_large(numbers):
    for number in numbers:
        if number > 50:
            return number
    return None
```

The function returns as soon as it finds an answer. Returning from a function also stops the loop.

## 16. Debugging Loops

When a loop behaves incorrectly, inspect these questions:

- What is the value before the first iteration?
- What values does the loop variable receive?
- Is the condition checked before or after the update?
- Does every path update the state?
- Can the loop run zero times?
- Is `break` skipping work too early?
- Is `continue` skipping the update needed for progress?

A trace table helps:

| Iteration | `count` before | Condition | Action | `count` after |
| --- | ---: | --- | --- | ---: |
| 1 | 1 | true | print | 2 |
| 2 | 2 | true | print | 3 |
| 3 | 3 | true | print | 4 |
| 4 | 4 | false | stop | 4 |

## 17. Common Loop Mistakes

### Infinite `while` loops

The condition never becomes false because the state is not updated correctly.

### Off-by-one errors

The loop starts or stops one step too early or too late. Remember that `range` excludes its stop value.

### Wrong accumulator initialization

Use `0` for a sum, `1` for a product, an empty list for collected results, and `None` when no best value exists yet.

### Confusing `break` and `continue`

`break` ends the loop; `continue` skips only the current iteration.

### Reusing unclear variables

Use `student`, `score`, or `index` instead of vague names such as `thing` or `x`.

### Modifying the collection being iterated

Filter into a new collection or iterate over a copy.

### Doing too much inside one loop

Extract calculations into functions when the body becomes difficult to explain.

## 18. Practice Questions

### Simple

1. Print the numbers from 1 through 10 with a `for` loop.
2. Print each character in a word.
3. Use a `while` loop to count down from 5 to 1.
4. Calculate the sum of `[2, 4, 6, 8]`.

### Easy

1. Print a multiplication table for a chosen number.
2. Count how many vowels appear in a string.
3. Find the largest value in a list without using `max()`.
4. Print only the even numbers from a list.
5. Ask for numbers until the user enters `0`, then print their total.

### Intermediate

1. Write `find_first_duplicate(items)` that returns the first repeated item.
2. Write `calculate_average(numbers)` using an accumulator and counter.
3. Build a number-guessing game with a maximum number of attempts.
4. Print a rectangle of stars using nested loops.
5. Remove all negative values from a list without changing the list during iteration.

### Expert

1. Write a function that returns the longest consecutive run of equal values.
2. Build a menu loop that validates commands and ends only when the user chooses quit.
3. Find all pairs in a list whose sum equals a target value.
4. Create a prime-number generator that stops at a requested limit.
5. Refactor a nested-loop report into functions with clear input and output contracts.

## 19. Trick Questions

Predict the output before running each example.

### Trick 1: `range` excludes the stop value

```python
for number in range(1, 4):
    print(number)
```

Answer: `1`, `2`, and `3`. The stop value `4` is excluded.

### Trick 2: `continue` skips the update

```python
count = 0

while count < 3:
    if count == 1:
        continue
    count += 1
```

What happens? The loop becomes infinite because when `count` reaches `1`, `continue` skips `count += 1` forever. Put the update before the `continue`, or redesign the condition.

### Trick 3: `break` affects only the nearest loop

```python
for row in range(2):
    for column in range(3):
        if column == 1:
            break
        print(row, column)
```

Answer: `0 0` and `1 0`. The inner loop stops, but the outer loop continues.

### Trick 4: Loop `else` and `break`

```python
for number in [2, 4, 6]:
    if number % 2 != 0:
        break
else:
    print("All even")
```

Answer: `All even`. The loop completes without using `break`.

### Trick 5: Empty loops

```python
for number in range(0):
    print("inside")

print("done")
```

Answer: only `done`. The loop body runs zero times.

### Trick 6: Reusing the loop variable

```python
for number in range(3):
    pass

print(number)
```

Answer: `2` in normal Python module code. The loop variable remains after the loop. Do not rely on this as a replacement for clear program state.

### Trick 7: `zip` stops at the shortest input

```python
names = ["Aanaa", "Maya", "Noah"]
scores = [90, 80]

for name, score in zip(names, scores):
    print(name, score)
```

Answer: only `Aanaa 90` and `Maya 80`. `Noah` has no matching score.

### Trick 8: Changing a list while iterating

```python
numbers = [1, 2, 3, 4]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)

print(numbers)
```

The result may surprise you because removing an item shifts later indexes. Filter into a new list instead.

## 20. Final Syntax Reference

```python
# for loop
for item in iterable:
    process(item)


# range loop
for number in range(start, stop, step):
    print(number)


# while loop
while condition:
    update_state()


# search with break and loop else
for item in items:
    if matches(item):
        result = item
        break
else:
    result = None


# index and value
for index, item in enumerate(items, start=1):
    print(index, item)


# corresponding items
for left, right in zip(left_items, right_items):
    print(left, right)


# collect transformed values
result = [transform(item) for item in items]
```
