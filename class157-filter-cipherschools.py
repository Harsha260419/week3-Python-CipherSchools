def is_even(a):
    return a%2==0
numbers = range(1,11)
evens = list(filter(lambda a:a%2==0, numbers))
print(evens)