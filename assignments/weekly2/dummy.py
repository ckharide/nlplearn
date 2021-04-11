import numpy as np
a = np.array([1, 0])
b = np.array([2, 5])

cosine_similarity = np.dot(a,b) / np.linalg.norm(a-b)
print(cosine_similarity)

cosine_similarity = np.dot(a,b) / np.linalg.norm(a) ** np.linalg.norm(b)