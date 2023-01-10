names = ['harsha','alex','luther']
def func(item):
    return len(item)
print(max(names,key=func))
student1 = [
    {"name":'harsha','score':99,'age':18},
    {"name":'alex','score':96,'age':19},
    {"name":'luther','score':83,'age':23}
]

print(max(student1,key=lambda item:item.get('score'))['name'])

student = {
    'harsha' : {'score':50,'age':18},
    'alex' : {'score':96,'age':19},
    'luther' : {'score':83,'age':23}
}

print(max(student,key=lambda item: student[item]['age']))