'''
COMPUTER GRAPHICS LAB ASSIGNMENT 01

PROFESSOR : Taesoo Kwon
TA : Jungho Kim

Author :
    Hanyang University
    Department of Computer Science & Engineering
    Gaon Choi(2019009261)
'''

import numpy as np

if __name__ == "__main__":
    # A. Create a 1d array M with values ranging from 2 to 26 and print M.
    M = np.arange(2, 26 + 1)
    print(M) ; print()

    # B. Reshape M as a 5x5 matrix and print M.
    M = M.reshape(5, 5)
    print(M) ; print()

    # C. Set the first column of the matrix M to 0 and print M.
    M[::, 0] = 0
    print(M) ; print()

    # D. Assign M^2 to the M and print M.
    M = M @ M
    print(M) ; print()

    # E. Now, let's consider the first row of matrix M as vector v. Calculate the magnitude of the vector v and print it.
    '''
    i.  Hint: |x| = sqrt(x_1^2 + x_2^2 + ... + x_n^2)
    ii. Hint: Use np.sqrt()
    '''
    v = M[0, ::]
    print(np.sqrt(v.dot(v)))    # x_1^2 + x_2^2 + ... + x_n^2 == v.dot(v)
                                # inner product
    