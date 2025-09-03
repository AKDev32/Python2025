import collections
from collections import namedtuple

# Point = namedtuple('Point', 'x y z')

# newP = Point(3, 4, 5)
# print(newP)

# using dictionary

# Point = namedtuple('Point', {'x': 0, 'y': 0, 'z': 0})

# newP = Point(3, 4, 5)
# print(newP)

# Point = namedtuple('Point', {'x': 0, 'y': 0, 'z': 0})

# newP = Point(3, 4, 5)
# print(newP.x, newP.y, newP.z)

Point = namedtuple('Point', {'x': 0, 'y': 0, 'z': 0})

newP = Point(3, 4, 5)
print(newP.x, newP.y, newP.z)
print(newP[0])
print(newP._asdict())
print(newP._fields)
print(newP._replace(y = 6))

p2 = Point._make(['a', 'b', 'c'])
print(p2)