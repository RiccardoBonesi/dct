import time
import cv2
from my_dct import *
from fft import *


# confronta tempi di esecuzione MyDCT-FFT
def estimate_time(matrix_list):
    for m in matrix_list:
        start_time = time.time()
        my_dct_2d(m)
        end_time = time.time()
        elapsed_dct = round(end_time - start_time, 4)
        start_time = time.time()
        fft_dct_2d(m)
        end_time = time.time()
        elapsed_fft = round(end_time - start_time, 4)

        print("MyDCT elapsed: {} sec - FFT_DCT elapsed: {} sec".format(elapsed_dct, elapsed_fft))


# crea matrici quadrate per confronto in estimate_time()
def test_square_matrix():
    matrix_list = [np.random.random((50, 50)),
                   np.random.random((100, 100)),
                   np.random.random((150, 150)),
                   np.random.random((200, 200)),
                   np.random.random((250, 250)),
                   np.random.random((300, 300)),
                   np.random.random((350, 350)),
                   np.random.random((400, 400)),
                   np.random.random((450, 450)),
                   np.random.random((500, 500)),
                   np.random.random((550, 550)),
                   np.random.random((600, 600)),
                   np.random.random((650, 650)),
                   np.random.random((700, 700))]

    estimate_time(matrix_list)


# testa la mydct e la fft su casi di test del prof
def test_dct():
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

    # test_square_matrix()

    # test_dct()

    img = cv2.imread('artificial.bmp', 0)

    matrix = np.array(img, dtype=float)     # float is faster than int
    # print(matrix)

    print('Image loaded. Starting...')

    start = time.time()
    print('Starting MyDCT...')
    my_result = my_dct_2d(matrix)
    end = time.time()
    my_elapsed = round(end - start, 4)
    print('MyDCT finished. Time Elapsed = {}'.format(my_elapsed))
    print('Starting FFT...')
    start = time.time()
    fft_result = fft_dct_2d(matrix)
    end = time.time()
    fft_elapsed = round(end - start, 4)
    print('FFT finished. Time Elapsed = {}'.format(my_elapsed))

    similar_result = np.allclose(my_result, fft_result)
    print("MyDCT elapsed: {} sec - FFT_DCT elapsed: {} sec - Results are similar: {}"
          .format(my_elapsed, fft_elapsed, similar_result))

    print('FINE')






