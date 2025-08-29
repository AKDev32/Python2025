var = 9
loop = True
newVar = 23

def func (x):
    # newVar = 7
    # print(var)
    # print(newVar)
    global loop
    loop = 7

    if x == 5:
        return newVar
    
def otherFunc() :
    newVar = 5
    print (newVar)    
    
# otherFunc()
loop = False
# func(2)
print(loop)