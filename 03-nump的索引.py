import numpy as np

print('*' * 50)
A = np.arange(3, 15)
print(A)

print(A[3])

print('*' * 50)
A = A.reshape(3, 4)
print('A:', A)
print('A[2]:', A[2])
print('A[1][1]:', A[1][1])  # 是一样的效果
print('A【1，1】', A[1, 1])
print('A[0, :]', A[0, :])

print('for:row')
for row in A:
    print(row)

print('for:column')
for col in A.T:
    print(col)

print('for:item')
for item in A.flat:
    print(item)
