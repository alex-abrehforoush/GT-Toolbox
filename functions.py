import numpy as np
#from main import cclear

def inputGameMatrix() -> np.ndarray:
    M = int(input("Enter the number of rows: "))
    N = int(input("Enter the number of columns: "))
    
    # Initialize matrix
    matrix = []
    print("Enter the entries rowwise...")
    
    # For user input
    for i in range(M):          # A for loop for row entries
        a =[]
        for j in range(N):      # A for loop for column entries
            a.append(int(input("Enter element at row " + str(i) + " and column " + str(j) + '\n')))
        matrix.append(a)
    return matrix
#tester for inputGameMatrix
# mat = inputGameMatrix()
# for i in range(6):
#     for j in range(2):
#         print(mat[i][j], end = " ")
#     print()

def rescale(A: np.array) -> np.array:
    arr = np.array(A)
    if np.amin(A) <= 0:
        arr = A + abs(np.amin(A)) + 1
    return arr
# tester for rescale
# ma = np.array([[-1, 2, 0], [-3, 10, -8], [-7, -7, -7]])
# print(ma)
# print('\n')
# print(rescale(ma))