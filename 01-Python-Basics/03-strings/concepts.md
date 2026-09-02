# Strings And Text

## Core Idea

A string is an immutable sequence of characters. Indexing reads one character; slicing reads a range; methods create transformed strings.

```python
message = " Python "
clean = message.strip().lower()
print(clean)
print(clean[0:3])
```

Useful tools include `strip`, `split`, `join`, `replace`, `lower`, `upper`, `title`, and f-strings.

## Skills To Build

- Normalize input before comparing it.
- Use f-strings for readable formatting.
- Remember that string methods return new strings.
- Use slices with clear start and stop boundaries.
- Separate text parsing from final display.

## Problem-Solving Method

Define the exact desired output first. Test empty text, extra whitespace, mixed case, punctuation, and repeated separators.

## Common Trap

Strings cannot be changed in place. Store the returned value: `text = text.strip()`.

## Further Reading

- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Exercism Python: Strings](https://exercism.org/tracks/python/exercises)
