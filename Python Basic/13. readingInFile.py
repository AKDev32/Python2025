file = open(r'c:\Users\amank\OneDrive\Desktop\Projects\Python\Python Basic\file.txt', 'r')
f = file.readlines()



# newList = []
# for line in f:
#     if line[-1] == '\n':
#         newList.append(line[:-1])
#     else:
#         newList.append(line)
# print(newList)    


# Automatically remove the \n

newList = []
for line in f:
    newList.append(line.strip())

print (newList)    


# with open("file.txt", "r") as f:
#     lines = f.readlines()
#     print(lines)


# filepath: c:\Users\amank\OneDrive\Desktop\Projects\Python\Python Basic\13. readingInFile.py
# file = open(r'c:\Users\amank\OneDrive\Desktop\Projects\Python\Python Basic\file.txt', 'r')
# print(file.read())
# file.close()