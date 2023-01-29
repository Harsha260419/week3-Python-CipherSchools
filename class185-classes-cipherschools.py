class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age  
    p1 = Person('Harsha', 'Sai', 18)
    p2 = Person('Jenna', 'Ortega', 20)
    
    print(p1.first_name)