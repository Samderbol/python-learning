import numpy as np

vectors = np.array([[-0.0745, -0.9399, 0.3333],
                   [-0.6863, 0.2908, 0.6667],
                   [-0.7235, -0.1791, -0.6667]])

norms = np.linalg.norm(vectors, axis=1)

print(norms)

dot_products = np.dot([-0.0745,-0.6863, -0.7235],
                   [-0.9399, 0.2908, -0.1791])

print('dot_products:', dot_products)

