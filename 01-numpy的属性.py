import numpy as np

print('*' * 50)
# 创建二维矩阵
array = np.array([[1, 2, 3],
                  [2, 3, 4]],
                 dtype=np.float)

print(array)
print('number of dim:', array.ndim)
print('shape:', array.shape)
print('size:', array.size)
print('dtype:', array.dtype)

print('*' * 50)
# 创建全为0的二维矩阵
a = np.zeros((3, 4))
print(a)

print('*' * 50)
# 创建全为1的二维矩阵
a = np.ones((3, 4), dtype=np.int16)
print(a)

print('*' * 50)
# 创建为空的二维矩阵
a = np.empty((3, 4), dtype=np.int16)
print(a)

print('*' * 50)
# 创建一个范围的向量，还可以指定步长
a = np.arange(10, 20, 2)
print(a)

a = np.arange(12)
print(a)

a = np.arange(1, 13).reshape((3, 4))
print(a)

print('*' * 50)
# 创建一个范围的线段，可以指定段数
a = np.linspace(1, 10, 6)
print(a)
print(a.reshape(2, 3))
