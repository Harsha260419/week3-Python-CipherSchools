def add(a,d):
    return a+d
def new_add(*args):
    total = 0
    for i in args:
        total += i
    return total
print(new_add(1,2,3,4,5,6,7,8,9))
print(new_add(*(1,2,3,4))) #tuple unpacking
def fuck(name,*arg, umr=33, **kwarg):
    print(name)
    print(arg)
    print(umr)
    print(kwarg)
fuck("Rocky",2018,2022,umr=34,a=1,b=2)