"""
An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right. The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.

Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. It does not matter if the mirror image is left-right or top-bottom.

Examples

id_mtrx(2) ➞ [
  [1, 0],
  [0, 1]
]

id_mtrx(-2) ➞ [
  [0, 1],
  [1, 0]
]

id_mtrx(0) ➞ []

def id_mtrx(n):
    identity_matrix = []
    if n == 0:
        return []
    elif n > 0:
        for i in range(n):
            row = []
            for j in range(n):
                if j == i:
                    row.append(1)
                else:
                    row.append(0)
            identity_matrix.append(row)
    return identity_matrix


print(id_mtrx(0))
"""

