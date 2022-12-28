def rev_babe(ls):
    l1 = [element[::-1] for element in ls]
    return l1 # and by the way you don't have to create l1 variable you can directly return this >> [element[::-1] for element in ls]
ls = list(input("enter favorite singer names with space:").split(" "))
print(ls)
print(rev_babe(ls))