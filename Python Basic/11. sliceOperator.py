# slice operator

fruits = ['apple', 'banana', 'orange']
text = 'Hello I like python'

print (text[15])  # the letter that is in 15 index which is t
# print (text[start: stop: step])
print (text[0:5])  
print (text[::3])

# For insertion at any place of the list

# fruits[0:0] = 'b'   # insert at the beganing of the list
# print (fruits)

# fruits[1:1] = 'c'   # insert at the first postion of the list
# print (fruits)

fruits[3:3] = 'd'
print(fruits)