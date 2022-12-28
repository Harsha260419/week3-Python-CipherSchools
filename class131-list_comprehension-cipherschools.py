squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)
sq1 = [i**2 for i in range(1,11)]
print(sq1)
negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)
neg = [-i for i in range(1,11)]
print(neg)
names = ["Harsha","Elon Musk","Bill Gates","Steve Jobs"]
first_letter = []
for name in names:
    first_letter.append(name[0])
print(first_letter)
first_let = [name[0] for name in names]
print(first_let)
