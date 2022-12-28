numbers = list(range(1,11))
even = []
for i in numbers:
    if i%2==0:
        even.append(i)
print(even)

ev1 = [i for i in numbers if i%2==0]
print(ev1)

# actually you don't even have to create a variable named numbers you can directly write it in list comprehension as below

ev2 = [i for i in range(1,11) if i%2==0]
print(ev2)

# pythonic!!