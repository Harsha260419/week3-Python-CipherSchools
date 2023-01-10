numbers = range(1, 11)
squares = list(map(lambda x: x**2, numbers))
print(squares)

# map function is a built in function in python which takes a function and an iterable as arguments then map function applies the inputted function on each element of the iterable and then returns the result asobject to get the result in viewable format we have to change that list or tuple etc........


def square(a):
    return a**2


new_list = []
for i in numbers:
    new_list.append(square(i))
print(new_list)

names = ["Elon","Harsha","Larry","Sergrey","Sundar"]
length = map(len,names)
for i in length:
    print(i)
for j in length:
    print(j)

# you can loop only once in map function 