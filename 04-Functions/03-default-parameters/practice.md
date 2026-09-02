# Default Parameters: Practice Lab

## Learn Faster

Always test a default parameter twice: once omitted and once explicitly provided. For mutable data, test two separate calls for unwanted sharing.

## Tricky Problems

1. Predict two calls to a function using `items=[]` as a default.
2. Rewrite that function with `items=None` safely.
3. Design a greeting function with a customizable default message.
4. Explain why required parameters must come before defaults.
5. Create a configuration function using immutable defaults.

## Method

Use defaults for stable policy choices. Use `None` as a signal to create fresh mutable state inside the function.

## Website Practice

- [Python Default Argument Values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)
- [HackerRank Python Functions](https://www.hackerrank.com/domains/python)

## Completion Check

You can explain evaluation timing, safe defaults, and the mutable-default trap without memorizing a rule blindly.
