# def average_finder(*args):
#     average =[]
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average
# print(average_finder([1,2,3],[4,5,6],[7,8,9]))

avg = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(avg([1,2,3],[7,8,9]))