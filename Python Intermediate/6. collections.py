from collections import Counter

c = Counter('gallad')
print(c)
c = Counter(['a', 'b', 'c', 'd'])
print(c)
c = Counter({'a': 1, 'b': 2})
print(c)
c = Counter(cats=4, dogs=7)
print(c)
print(c['cats'])
print(c['man'])
print(list(c.elements()))