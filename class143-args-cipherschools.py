# *operator
# *arg
# the purpose of arg is we can take as many as arguments as input from the user for the function 
# def tot(a,b):
#     return a+b
# print(tot(5,6,11)) # here it'll give an error because max arguments can be given are 2 so to remove this disadvantage we use *arg

def tot(*arg):
    print(arg)
    print(type(arg))
    total=0
    for num in arg:
        total+=num
    print(total)
tot(5,6,7,8)
        