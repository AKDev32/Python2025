age = input ('Input your age');

if int(age) >= 16:
    print ('hey youre 16')
else:
    print ('your are younger than 16')    

height = input()

if int(height) < 1:
    print ('you cant ride, under 1m')
elif int(height) > 2:
    print ('you cant ride, over 2m')  
elif int(height) == 5:
    print('wow you are tall')      
else:
    print ('you can ride')