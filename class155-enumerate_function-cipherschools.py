# helps to track the position of items in for loop
names = ["Harsha", "Elon", "Larry"]


def pos(l, target):

    for position, target in enumerate(names):
        if target == "Elon":
            return position
    return -1


print(pos(names, "Elon"))
print(pos(names, "Sai"))
