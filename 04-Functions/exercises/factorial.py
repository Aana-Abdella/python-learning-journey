def factorial(n):

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n== 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    try:
        print(f"The factorial of {n} is {factorial(n)}")
    except ValueError as e:
        print(e)    

n = int(input("Enter a number to calculate its factorial: "))

print(factorial(n))  # Output: 120