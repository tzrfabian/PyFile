import numpy as np
import sys

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# print(matrix)
# print(type(matrix))

# matriks = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matriks)

# var_list = [[1,2,3],[4,5,6],[7,8,9]]
# var_array = numpy.array([[1,2,3],[4,5,6],[7,8,9]])

# print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
# print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)

# <nama-var> = [[<default-var> for j in range(<m>)] for  i in range(<n>)]
# matrix = [[j for j in range(1,5)] for i in range(3)]
# print(matrix)

# var_mat = [[1, 2, 3, 4, 5],
#            [6, 7, 8, 9, 10],
#            [11, 12, 13, 14, 15],
#            [16, 17, 18, 19, 20],
#            [21, 22, 23, 24, 25]]
# # <namamatriks>[<nbaris>][<nkolom>]
# print(var_mat[4][2])

# var_mat = [[5, 0], 
#            [1,-2]]
# def_mat = [[0 for j in range(2)] for i in range(2)]
# for i in range(len(var_mat)):
#     for j in range(len(var_mat[0])):
#         def_mat[i][j] = var_mat[i][j]*2

# print(def_mat)

# Matrix's Operation using numpy

var_mat = np.array([[5, 0],
                    [1,-2]])

result = var_mat*3
print(result)