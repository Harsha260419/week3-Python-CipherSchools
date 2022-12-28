def num_filter(l):
    return [str(i) for i in l if type(i)==int or type(i)==float]
print(num_filter([True, False, "Elon", 1,2,3.3]))

# this is also known as fucking pythonic code