def something(n,*arg):
    x = [i**n for i in arg]
    if arg:
        return x
    else:
        print("You didn't pass any arg")

print(something(3))