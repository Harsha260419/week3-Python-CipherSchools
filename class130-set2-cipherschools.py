s = {'a','b','c'}
# in key word to check if item is present in a set or not
if 'a' in s:
    print("present")
else:
    print("not present")

# for loop in sets

for items in s:
    print(items)

s1={1,2,3,4}
s2={3,4,5,6}
union_set = s1 | s2
intersection_set = s1 & s2
print(union_set)
print(intersection_set)
