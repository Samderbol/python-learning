import numpy as np

# 定义一个矩阵
A = np.array([[1, 5, 2], [3, 6, 4], [3, 7, 8]])

# 使用 Gauss-Jordan 消去法求解 A 的逆矩阵
A_inv = np.linalg.solve(A, np.eye(3))

# 打印 A 的逆矩阵
print(A_inv)
