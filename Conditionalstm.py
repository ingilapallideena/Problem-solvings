#   Print given value is positive or not  
num = int(input("Enter a number: "))
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
# Given char(n) is upper case or lower case(without using built in function) 
ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    print("Uppercase Letter")
elif 'a' <= ch <= 'z':
    print("Lowercase Letter")
else:
    print("Not an Alphabet")