import numpy as np
a = [[1,0,0],[-2,5,-2],[-2,4,-1]]
 
 
c = np.linalg.eig(a)
eig_values = c[0]
 
p = c[1]
 
f = np.dot(np.dot(np.linalg.inv(p),a),p)
f = np.around(f,decimals=2)

print(f)