def func(names,**kwarg):
    if kwarg.get("reverse_str") == True:
        return [i[::-1].title() for i in names]
    print(list(names[i].title() for i in range(0,len(names))))
names = ['harsha', 'sai']
print(func(names, reverse_str = True))