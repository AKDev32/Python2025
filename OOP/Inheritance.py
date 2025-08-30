# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print ("Meow")   


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#        print("bark")      


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")    

    def speak(self):
        print("I don't know what I say")        
        
class Cat(Pet):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
        

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass


p = Pet("Aman", 19)
p.show()
p.speak()
c = Cat("Raj", 20, 'black and white')
c.show()
c.speak()
d = Dog("Kumar", 21)
d.show()
d.speak()
f = Fish("Bubble", 10)
f.speak()

