# from PIL import Image
import numpy as np
import math
import time
import cv2
from scipy import fftpack


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


def fftdct_wrapper(matrix):
    return fftpack.dct(matrix, norm='ortho')


def fftidct_wrapper(matrix):
    return fftpack.idct(matrix, norm='ortho')


def fft_dct_2d(matrix):
    first_dct = np.apply_along_axis(fftdct_wrapper, axis=1, arr=matrix)
    trasposed_matrix = first_dct.transpose()
    second_dct = np.apply_along_axis(fftdct_wrapper, axis=1, arr=trasposed_matrix)

    return second_dct.transpose()


def fft_idct_2d(matrix):
    first_dct = np.apply_along_axis(fftidct_wrapper, axis=1, arr=matrix)
    trasposed_matrix = first_dct.transpose()
    second_dct = np.apply_along_axis(fftidct_wrapper, axis=1, arr=trasposed_matrix)

    return second_dct.transpose()


def validate():
    array = np.array([231, 32, 233, 161, 24, 71, 140, 245])

    result = my_dct(array)

    print(result)

    test = np.array([[231, 32, 233, 161, 24, 71, 140, 245], [247, 40, 248, 245, 124, 204, 36, 107],
                      [234, 202, 245, 167, 9, 217, 239, 173], [193, 190, 100, 167, 43, 180, 8, 70],
                      [11, 24, 210, 177, 81, 243, 8, 112], [97, 195, 203, 47, 125, 114, 165, 181],
                      [193, 70, 174, 167, 41, 30, 127, 245], [87, 149, 57, 192, 65, 129, 178, 228]])

    dct2_result = my_dct_2d(test)
    print(dct2_result)
    py_dct2_result = fft_dct_2d(test)
    print(py_dct2_result)

    print(np.allclose(dct2_result, py_dct2_result))


if __name__ == "__main__":
    # load image
    # img = Image.open("big_tree.bmp")
    img = cv2.imread('artificial.bmp', 0)

    # test matrix prof
    # validate()

    matrix = np.array(img)

    start = time.time()
    my_result = my_dct_2d(matrix)
    end = time.time()
    my_elapsed = round(end - start, 4)
    start = time.time()
    fft_result = fft_dct_2d(matrix)
    end = time.time()
    fft_elapsed = round(end - start, 4)

    similar_result = np.allclose(my_result, fft_result)
    print("MyDCT elapsed: {} sec - FFT_DCT elapsed: {} sec - Results are similar: {}"
          .format(my_elapsed, fft_elapsed, similar_result))


    print('ok')






