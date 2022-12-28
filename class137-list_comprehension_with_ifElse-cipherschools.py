def partial(l):
    return [i*2 if i%2==0 else -i for i in l]
print(partial(range(1,11)))