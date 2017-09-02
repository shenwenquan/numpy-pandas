import numpy as np

# 向量的加减法
print('*' * 50)
a = np.array([10, 20, 30, 40])
b = np.arange(4)

print(a)
print(b)
print(a - b)
print(a + b)

# 向量的平方,三角
print('*' * 50)
print(b)
print(b ** 2)
print(10 * np.sin(b))
print(b < 3)

# 矩阵的乘法
print('*' * 50)
a = np.array([[1, 1], [0, 1]])
b = np.arange(4).reshape(2, 2)

print(a)
print(b)

print(a * b)
print(np.dot(a, b))

# 随机生成的矩阵
print('*' * 50)
a = np.random.random((2, 4))
print(a)

print('sum', np.sum(a))
print('max:', np.max(a))
print('min:', np.min(a))

print('sum,axis=1:', np.sum(a, axis=1))
print('max,axis=0:', np.max(a, axis=0))
print('min:axis=1', np.min(a, axis=1))

# 计算矩阵的最值索引
print('*' * 50)
A = np.arange(2, 14).reshape(3, 4)
print(A)
print('min_index:', np.argmin(A))
print('max_index:', np.argmax(A))
print('avg1:', np.mean(A))
print('avg2:', np.average(A))
print('avg3:', A.mean())
print('median:', np.median(A))
print('cumsum:', np.cumsum(A))
print('diff:', np.diff(A))  # 累差
print('nonzero:', np.nonzero(A))  # 将行和列的索引分开，形成两个数组
print('sort:', np.sort(A))
print('transpose:', np.transpose(A))  # 同A.T
print('T:', A.T)
print('AT*A:', (A.T).dot(A))
print('clip:', np.clip(A, 5, 9))  # 所有小于5都等于5，所有大于9都变成9
