# parameters
# args
# default parameters
# kwargs
def func(name='noIntel',age=24):
    print(name,end=" ")
    print(age)
func()#default parameters kick in when no arguments are passed to the parmeter these are kind of default values which will be by passed if the arguments are passed
# if we want to use all these 4 types of arguments at once then we have to follow an order which is as mentioned at the top otherwise it'll throw an error
def fuck(name,*arg, umr=33, **kwarg):
    print(name)
    print(arg)
    print(umr)
    print(kwarg)
fuck("Rocky",2018,2022,umr=34,a=1,b=2)
