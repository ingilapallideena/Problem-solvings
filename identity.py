# converting one datatype to another datatype (24 types)
# Integer - Float
a = 10
print(float(a))
# Integer - String
a = 10
print(str(a))
# Integer - Boolean
a = 10
print(bool(a))
# Float - Integer
a = 12.8
print(int(a))
# Float - String
a = 12.8
print(str(a))
# Float - Boolean
a = 0.0
print(bool(a))
# String - Integer
a = "100"
print(int(a))
# String - Float
a = "25.5"
print(float(a))
# String- Boolean
a = "Hello"
print(bool(a))
# String- List
a = "Python"
print(list(a))
# String- Tuple
a = "Python"
print(tuple(a))
# String- Set
a = "Python"
print(set(a))
# List -Tuple
a = [1, 2, 3]
print(tuple(a))
# List -Set
a = [1, 2, 2, 3]
print(set(a))
# List -String
a = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(a))
# Tuple- List
a = (1, 2, 3)
print(list(a))
# Tuple- Set
a = (1, 2, 2, 3)
print(set(a))
# Tuple- String
a = ('P', 'y', 't', 'h', 'o', 'n')
print("".join(a))
# Set -List
a = {1, 2, 3}
print(list(a))
# Set -Tuple
a = {1, 2, 3}
print(tuple(a))
# Set -String
a = {'P', 'y', 't', 'h', 'o', 'n'}
print("".join(a))
# Boolean -Integer
a = True
print(int(a))
# Boolean -String
a = False
print(str(a))
# Integer -Complex
a = 10
print(complex(a))