# Atleast 10 different output generate in SLICING 
text = "rishika"
print("1.", text[:])       # Entire string
print("2.", text[:4])      # First 4 characters
print("3.", text[2:])      # From index 2 to end
print("4.", text[1:5])     # Index 1 to 4
print("5.", text[-3:])     # Last 3 characters
print("6.", text[:-2])     # Except last 2 characters
print("7.", text[::2])     # Every 2nd character
print("8.", text[1::2])    # Every 2nd character from index 1
print("9.", text[::-1])    # Reverse string
print("10.", text[::-2])   # Reverse with step 2
print("11.", text[::3])    # Every 3rd character
print("12.", text[-5:-1])  # Negative indexing
print("13.", text[2:6:2])  # Index 2 to 5 with step 2
print("14.", text[-1])     # Last character
print("15.", text[0])      # First character