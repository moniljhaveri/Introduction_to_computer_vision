import cv2 
import numpy as np 
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

dir_path_dog = dir_path + "/input/" + "dog.png"
dir_path_veggies = dir_path + "/input/" + "veggies.png"
img_dog = cv2.imread(dir_path_dog, 1)
img_veggies = cv2.imread(dir_path_veggies, 1)
cv2.imshow('image_veggies', img_veggies)
cv2.imshow('image_dog', img_dog)
cv2.waitKey(0)
cv2.destroyAllWindows() 

dir_save_dog = dir_path + "/output/" + "ps0-1-a-1.png"
dir_save_veggies = dir_path + "/output/" + "ps0-1-a-2.png"
cv2.imwrite(dir_save_dog, img_dog)
cv2.imwrite(dir_save_veggies, img_veggies)

