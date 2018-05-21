import math
import numpy as np


def my_dct(array):
    size = array.size
    result = np.zeros(shape=size)

    for k in range(size):
        s = 1 if k != 0 else math.sqrt(0.5)
        norm_coeff = math.sqrt(2 / size) * s
        i_result = 0
        for n, x_n in enumerate(array):
            i_result += x_n * math.cos(
                math.pi * k * (2 * n + 1) / (2 * size))

        result[k] = norm_coeff * i_result

    return result


def my_dct_2d(matrix):
    first_dct = np.apply_along_axis(my_dct, axis=1, arr=matrix)
    trasposed_matrix = first_dct.transpose()
    second_dct = np.apply_along_axis(my_dct, axis=1, arr=trasposed_matrix)

    return second_dct.transpose()