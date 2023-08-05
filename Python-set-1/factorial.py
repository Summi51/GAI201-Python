# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(8))
