import numpy as np

# 数组合并 注：np.array不是矩阵，只是一个数的序列，需要在用A[:,np.newaxis]给列上加一个维度

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]
C = np.vstack((A, B))  # 垂直合并
D = np.hstack((A, B))  # 水平合并

print('A:')
print(A)
print('B:')
print(B)
print('C:')
print(C)
print('D:')
print(D)

print('A[np.newaxis,:]  is')
print(A[np.newaxis, :])

print('A[:,np.newaxis]  is')
print(A[:, np.newaxis])

E = np.concatenate((A, B, B, A), axis=1)  # 多个数组合并

print('E:')
print(E)

# 数组分割

print('A:')
A = np.arange(12).reshape((3, 4))
print(A)

print(np.split(A, 2, axis=1))  # 等量分割

print(np.array_split(A, 3, axis=1))  # 不等量分割
