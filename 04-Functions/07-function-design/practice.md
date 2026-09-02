# Function Design: Practice Lab

## Learn Faster

Draw a data-flow diagram for each program: input -> validation -> calculation -> result -> display. Split only where responsibilities differ.

## Tricky Problems

1. Refactor a student report that performs input, grading, and printing in one block.
2. Design pure functions for total, average, grade, and pass status.
3. Decide whether invalid input should raise `ValueError` or return a special value.
4. Remove global mutable state from an expense tracker.
5. Write a testable function whose output does not depend on the clock or user input.

## Method

Start with behavior, not abstractions. Name the smallest useful functions, define their contracts, then test each independently before composing them.

## Website Practice

- [Python Function Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Exercism Python Exercises](https://exercism.org/tracks/python/exercises)

## Completion Check

You can separate policy from interface code, reduce coupling, and explain how data travels through a program.
