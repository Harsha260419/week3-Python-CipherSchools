def square(a):
    return a**2
s = square
print(s(7))
print(square.__name__)
print(s.__name__)
print(s)
print(square)

def cube(a):
    return a**3
c = cube
print(c(7))
print(cube(7))
print(cube)
print(c)