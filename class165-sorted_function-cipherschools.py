fruits = ['grapes','mango','apple']

guitars = [
    {'model' : 'yamaha f310','price':8400},
    {'model' : 'yamaha faith neptune','price':50000},
    {'model' : 'yamaha taylor','price':450000}
]


print(sorted(guitars, key= lambda item : item['price'], reverse=True))