# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."


n = 13
isPrime = False

if n <= 1:
    isPrime = False

for i in range(2, n):
    if n % i == 0:
        isPrime = False
        break

if not isPrime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
