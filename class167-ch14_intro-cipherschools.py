def square(a):
    return a**2
s = square
print(s(7))
print(square.__name__)
print(s.__name__)
print(s)
print(square)