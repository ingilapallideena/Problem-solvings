# Add Two Numbers
def add(a, b):
    return a + b
print(add(10, 20))
#  Find Square of a Number
def square(n):
    return n * n
print(square(5))
# Find Cube of a Number
def cube(n):
    return n ** 3
print(cube(4))
# Check Even or Odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_odd(7))
#  Find Largest of Two Numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b
print(largest(15, 25))
# Find Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(factorial(5))
#  Check Prime Number
def prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
print(prime(11))
# Reverse a Number
def reverse_num(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
print(reverse_num(1234))
#  Find Sum of Digits
def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s
print(sum_digits(1234))
#  Check Palindrome Number
def palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if temp == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(palindrome(121))