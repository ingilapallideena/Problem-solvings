# .sum of list product of the list max,min,length of list
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
product = 1
for i in numbers:
    product *= i
maximum = max(numbers)
minimum = min(numbers)
length = len(numbers)
print("List:", numbers)
print("Sum =", total)
print("Product =", product)
print("Maximum =", maximum)
print("Minimum =", minimum)
print("Length =", length)