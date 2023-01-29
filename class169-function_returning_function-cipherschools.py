def outer_fun():
    def inner_fun():    
        print("This is inner function")
    return inner_fun
war=outer_fun()
war()