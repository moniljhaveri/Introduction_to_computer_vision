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


def problem2(edges, theta_bin, rho_bin):
    # part a
    if len(edges.shape) == 2:
        height, width = edges.shape
    else:
        height, width, _ = edges.shape

    theta_samples = int(180 / theta_bin)

    theta_list = np.linspace(-90.0, 90.0, num=theta_samples)

    rho_max = math.ceil(((height**2) + (width**2))**(1 / 2))
    rho_samples = int(rho_max / rho_bin)
    rho_list = np.linspace(0, rho_max, num=rho_samples)
    hought_arr = np.zeros((len(rho_list), len(theta_list)))
    edge_arr = np.nonzero(edges)
    for i, j in zip(*edge_arr):
        for theta_idx, theta in enumerate(theta_list):
            rho = i * np.cos(np.deg2rad(theta)) + j * np.sin(np.deg2rad(theta))
            rho_idx = int(round(rho / rho_bin))
            hought_arr[rho_idx][theta_idx] += 1

    img = Image.fromarray(hought_arr)
    img.show()
    return hought_arr


dir_path = os.path.dirname(os.path.abspath(
    __file__)) + '/' + 'ps1_octave_template'

edges = problem1(dir_path)
hought_arr = problem2(edges, 1, 1)
