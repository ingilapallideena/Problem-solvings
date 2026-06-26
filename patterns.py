# Find length of number 3 separate each number 1,5,3   
# 1 power length of number sum check condition  in petterns 
num = int(input("Enter a number: "))
original = num
length = len(str(num))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit ** length
    num //= 10
if sum == original:
    print(original, "is an Armstrong Number")
else:
    print(original, "is not an Armstrong Number")