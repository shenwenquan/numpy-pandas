import numpy as np

a = np.arange(4)

print(a)

b = a
c = a
d = b
e = a.copy()
a[0] = 11

print(a)
print(b)
print(c)
print(d)
print(e)
