# Square Pattern
rows = 4
for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()
#rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print() 
# Number Triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Repeated Number Triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()
# Alphabet Triangle
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()
# Inverted Star Triangle
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
# Inverted Number Triangle
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()