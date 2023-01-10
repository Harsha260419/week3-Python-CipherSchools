numbers = range(1,5) # tuples, strings ---- iterables
squares = map(lambda a : a**2, numbers) #iterator
for i in numbers:
    print(i)

number_iter = iter(squares)
itera = next(number_iter)
print(itera)
print(itera)
print(itera)