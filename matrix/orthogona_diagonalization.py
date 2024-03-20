import numpy as np                              #导入numpy
np.set_printoptions(precision=4, suppress=True) #设置输出精度
A=np.array([[2,2,-2],                           #设置矩阵A
            [2,5,-4],
            [-2,-4,5]])
v,P=np.linalg.eigh(A)                           #计算A的特征值和正交特征向量

is_orthogonal = np.allclose(np.dot(P.T,P ), np.eye(3)) #判断P是否正交

print(is_orthogonal)

print(v)                                   #输出特征值
print(P)                            #输出特征向量
print(P.T)                                    #输出P的转置
print(np.matmul(np.matmul(P.T,A),P))       #输出P^TAP
