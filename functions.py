import numpy as np

def rescale(A: np.array) -> np.array:
    arr = np.array(A)
    if np.amin(A) <= 0:
        arr = A + abs(np.amin(A)) + 1
    return arr

ma = np.array([[-1, 2, 0], [-3, 10, -8], [-7, -7, -7]])
print(ma)
print('\n')
print(rescale(ma))