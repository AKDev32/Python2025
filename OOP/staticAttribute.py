class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name

p1 = Person("Aman")
p2 = Person("Kumar")        

print(Person.number_of_people)