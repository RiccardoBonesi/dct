from scipy import fftpack
import numpy as np


def fftdct_wrapper(matrix):
    return fftpack.dct(matrix, norm='ortho')


def fftidct_wrapper(matrix):
    return fftpack.idct(matrix, norm='ortho')


def fft_dct_2d(matrix):
    first_dct = np.apply_along_axis(fftdct_wrapper, axis=1, arr=matrix)
    trasposed_matrix = first_dct.transpose()
    second_dct = np.apply_along_axis(fftdct_wrapper, axis=1, arr=trasposed_matrix)

    return second_dct.transpose()


# FFT inversa
def fft_idct_2d(matrix):
    first_dct = np.apply_along_axis(fftidct_wrapper, axis=1, arr=matrix)
    trasposed_matrix = first_dct.transpose()
    second_dct = np.apply_along_axis(fftidct_wrapper, axis=1, arr=trasposed_matrix)

    return second_dct.transpose()