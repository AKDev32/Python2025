# Optional Paramter Tutorial #1

# def func (x = 1):
#     return x**2

# call = func(5)
# print(call)


# def func (word, freq=1):
#     print(word*freq)

# call = func('aman ', 10)


# def func (word, add = 5, freq=1):
#     print(word*(freq+add))

# call = func('aman ', 5, 3)


# Example

class car(object):
    def __init__(self, make, model, year, condition='New', kms= 0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll=True):
        if showAll:
            print("This car is %s, %s and %s, it %s and has %s kms." %(self.make, self.model, self.year, self.condition, self.kms))        
        else:
            print ("This car is %s %s from %s" %(self.make, self.model, self.year))            

whip = car("Ford", "Fusion", 2024)
whip.display(False)           