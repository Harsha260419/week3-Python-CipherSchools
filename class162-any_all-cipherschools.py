numbers1 = [2,4,6,8]
numbers2 = [1,2,3,4,5,6,7]
evens1 = []
for num in numbers1:
    evens1.append(num%2==0)
print(evens1)
print(all([True,False,True]))

print(all([a%2==0 for a in numbers1]))
print(all([a%2==0 for a in numbers2]))
print(any([a%2==0 for a in numbers2]))
