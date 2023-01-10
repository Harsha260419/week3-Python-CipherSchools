def multiply(*args):
    total = 1
    for i in args:
        total *= i
    print(total)
num = [2,3,4]
multiply(*[5,6,7])
multiply(*num) #use * to unpack the list