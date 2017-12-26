import cv2
import numpy as np
import os
import math
from PIL import Image


def problem1(dir_path):
    dir_path_prob_1 = dir_path + '/input/' + 'ps1-input0.png'
    img = cv2.imread(dir_path_prob_1, 0)
    edges = cv2.Canny(img, 0, 250)
    dir_path_prob_1_save_path = dir_path + '/output/' + 'ps1-1-a-1.png'
    cv2.imwrite(dir_path_prob_1_save_path, edges)
    return edges


def problem2(edges, theta_bin, d_bin):
    height, width = edges.shape
    numTheta = math.ceil(181 / theta_bin)
    d_len = math.ceil(((height**2) + (width**2))**(1 / 2))
    numD = math.ceil(d_len)
    hought_arr = np.zeros((numD, numTheta))
    theta_arr = []
    edge_arr = [(i, j) for i in range(height)
                for j in range(width) if edges[i, j]]

    for i, j in edge_arr:
        theta = np.arctan2(i, j)
        theta_ang = math.floor(theta * (180 / np.pi))
        p = math.floor(i * np.sin(theta) + j * np.cos(theta))
        hought_arr[p, theta_ang] += 1

    print(np.amax(hought_arr))


dir_path = os.path.dirname(os.path.abspath(
    __file__)) + '/' + 'ps1_octave_template'

edges = problem1(dir_path)
problem2(edges, 1, 1)
