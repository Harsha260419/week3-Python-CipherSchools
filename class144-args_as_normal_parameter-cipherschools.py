def multiply(n,*arg):
    print(n)
    print(arg)
    x = 1
    for i in arg:
        x *= i
    print(x)
multiply(5,6,7,8,9)

# here n is treated as normal argument but * is an operator which takes arguments and stores them as tuples
# and also you cannot write n after *arg because whatever you write will go into *arg not into n
# for * you don't have to pass any arguments but for normal parameters like n you have to give something as input otherwise error happens