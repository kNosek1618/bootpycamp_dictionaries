
d = dict(a=1, b=2, c=3)
d.clear()
print(d) # {}


d = dict(a=1, b=2, c=3)
c = d.copy()
print(c) # {'a': 1, 'b': 2, 'c': 3}
print(c == d) # True
print(c is d) # False


print(d.get('a')) # 1

print(d.get('c')) # 3