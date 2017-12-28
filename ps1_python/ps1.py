import cv2
import numpy as np
import os
import math
from PIL import Image
from hough_lib import hough_peaks
from hough_lib import hough_arr


def problem1(dir_path):
    dir_path_prob_1 = dir_path + '/input/' + 'ps1-input0.png'
    img = cv2.imread(dir_path_prob_1, 0)
    edges = cv2.Canny(img, 0, 250)
    dir_path_prob_1_save_path = dir_path + '/output/' + 'ps1-1-a-1.png'
    cv2.imwrite(dir_path_prob_1_save_path, edges)
    return edges


dir_path = os.path.dirname(os.path.abspath(
    __file__)) + '/' + 'ps1_octave_template'

edges = problem1(dir_path)
hough_array = hough_arr(edges, 10, 1)

hough_peaks(hough_array, 1)
