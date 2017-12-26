import cv2
import numpy as np 
import os 


def problem1(dir_path): 
    dir_path_prob_1 = dir_path + '/input/' + 'ps1-input0.png'
    img = cv2.imread(dir_path_prob_1, 0)
    edges = cv2.Canny(img, 0, 250)
    dir_path_prob_1_save_path = dir_path + '/output/' + 'ps1-1-a-1.png'
    print(dir_path_prob_1_save_path)
    cv2.imwrite(dir_path_prob_1_save_path, edges)
    #cv2.imshow('image', edges)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows() 
    return edges

def problem2(edges): 
    pass 

dir_path = os.path.dirname(os.path.realpath(__file__)) + '/' + 'ps1_octave_template'
edges = problem1(dir_path)