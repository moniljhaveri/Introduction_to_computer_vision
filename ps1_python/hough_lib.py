import cv2
import numpy as np
import os
import math
from PIL import Image


def hough_arr(edges, theta_bin, rho_bin):
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
    return hought_arr


def hough_peaks(H, num_peaks):
    pass
