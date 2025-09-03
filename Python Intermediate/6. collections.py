import collections
from collections import Counter

# c = Counter('gallad')
# print(c)
# c = Counter(['a', 'b', 'c', 'd'])
# print(c)
# c = Counter({'a': 1, 'b': 2})
# print(c)
# c = Counter(cats=4, dogs=7)
# print(c)
# print(c['cats'])
# print(c['man'])
# print(list(c.elements()))


# c = Counter(a=4, b=2, c=0, d=-2)
# d = ['a', 'b', 'b', 'c']

# c.subtract(d)
# print(c)
# c.update(d)
# print(c)
# c.clear()
# print(c)


c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'b', 'c'])

print(c + d)
print(c - d)
print(c & d)
print(c | d)

