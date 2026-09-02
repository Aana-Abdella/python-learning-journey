# Lists: Practice Lab

## Learn Faster

For each problem, decide whether you need order, duplicates, mutation, or fast membership before choosing a list operation.

## Tricky Problems

1. Predict the result of aliasing: `other = values; other.append(1)`.
2. Remove all negative numbers without mutating the list during iteration.
3. Return the second-largest distinct value and define behavior for too-short input.
4. Explain the difference between `items[:]` and `items`.
5. Convert a nested list into a flat list using a deliberate strategy.

## Method

Start with a normal loop for clarity. Replace it with a comprehension only when the transformation remains readable. Test empty and duplicate-heavy lists.

## Website Practice

- [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Codewars Python Kata](https://www.codewars.com/kata/search/python)

## Completion Check

You can choose safe mutation patterns, preserve order when needed, and explain aliasing versus copying.
