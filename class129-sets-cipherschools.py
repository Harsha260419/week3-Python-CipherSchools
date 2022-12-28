#sets
#unordered collection of unique items
s={1,2,3,4,2}
# print(s[1])
l=[1,2,3,4,555,6,7,77,7]
# remove duplicate
s2=list(set(l))
print(s2)
# add to sets
s.add(6)
s.add(6)
print(s)
# remove from the sets
s.remove(3)
print(s)
# s.remove(444) #you'll get a key error because this doesn't exist in the set
s.discard(444) #this is will also not do anything but it won't show any error as remove showed
print(s)
# clear
s.clear()
print(s)
s1=s.copy()
print(s1)
#  you cannot store lists, dictionaries in sets
q={(1,2),3}
print(q)
