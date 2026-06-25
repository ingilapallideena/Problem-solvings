#  Sum of Digits  
num = 1234
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print(total)
#  Reverse a Number
num = 1234
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print(reverse)
# Count Digits in a Numbe
num = 12345
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)
# count even or odd
num = 17
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#  Check Prime Number
num = 13
if num < 2:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
# # | Find Factorial of a Number 
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i

print(fact)
# Find Factors of a Number 
num = 12
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
# | Check Palindrome Number
num = 121
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
#  Check Armstrong Number  
num = 153
original = num
digits = len(str(num))
total = 0
while num > 0:
    digit = num % 10
    total += digit ** digits
    num //= 10
if total == original:
    print("Armstrong")
else:
    print("Not Armstrong")
# | Find GCD (HCF) of Two Numbers
a = 12
b = 18
while b != 0:
    a, b = b, a % b
print(a)
