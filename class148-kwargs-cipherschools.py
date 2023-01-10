# ** kwargs or keyword arguments
# ** is the parameter and kwargs is the name you give it to call you can assign any name to it
def fuck(**ass):
    print(ass)
    print(type(ass))
    for k, v in ass.items():
        print(f"{k} : {v}")


fuck(name="Elon", age=51)
# it takes the input and gathers it and stores it as dictionary.


def bitch(name, **oh):
    print(name, end=" ")
    print(oh)


bitch("daniels", age=44)
# dictionary unpacking
d = {"naam": "Harsha", "age": 18, "Rank": "Major"}
fuck(**d)
