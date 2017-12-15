import cv2 
import numpy as np 
import os 

def prob_1(): 
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

def pixel_switcher(img, swap_1, swap_2):  
    #switches the pixels in an image 
    #img is mat 
    #swap_1 is a color layer defined as an integer
    #swap_2 is a color layer defined as an integer
    
    mat_1 = img[:,:,swap_1]
    mat_2 = img[:,:,swap_2] 
    # there is a more pythonic way to do this 
    img[:,:,swap_1] = mat_2
    img[:,:,swap_2] = mat_1
    return img

def prob_2(): 
    # a 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_dog = dir_path + "/output/" + "ps0-1-a-1.png"
    dir_save_dog = dir_path + "/output/" + "ps0-2-a-1.png"
    img = cv2.imread(dir_dog, 1)
    cv2.imshow('original', img)
    img = pixel_switcher(img, 0, 2) 
    cv2.imshow('problem 2a', img)
    cv2.imwrite(dir_save_dog, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

    # b 
    dir_save_dog = dir_path + "/output/" + "ps0-2-b-1.png"
    mono_img = img[:,:,1]
    cv2.imshow('problem 2b', mono_img)
    cv2.imwrite(dir_save_dog, mono_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

    # c 
    dir_save_dog = dir_path + "/output/" + "ps0-2-c-1.png"
    img = cv2.imread(dir_dog, 1)
    mono_img = img[:,:,2]
    cv2.imshow('problem 2c', mono_img)
    cv2.imwrite(dir_save_dog, mono_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    return

def prob_3(): 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_dog = dir_path + "/output/" + "ps0-1-a-1.png"
    dir_veg = dir_path + "/output/" + "ps0-1-a-2.png"
    dir_save = dir_path + "/output/" + "ps0-3-a-1.png"
    img_dog = cv2.imread(dir_dog, 1)
    d_height, d_width, _ = img_dog.shape
    mid_height_lower_bound = int(d_height/2 - 100)
    mid_height_higher_bound = int(d_height/2 +  100)
    mid_width_lower_bound = int(d_width/2 - 100)
    mid_width_higher_bound = int(d_width/2 +  100)
    print(mid_height_lower_bound, mid_height_higher_bound, mid_width_lower_bound, mid_width_higher_bound)
    img_dog = img_dog[mid_height_lower_bound:mid_height_higher_bound, mid_width_lower_bound:mid_width_higher_bound, 1]
    img_veg = cv2.imread(dir_veg, 1)
    v_height, v_width, _ = img_veg.shape
    img_veg = img_veg[:, :, 1]
    img_veg[mid_height_lower_bound:mid_height_higher_bound, mid_width_lower_bound:mid_width_higher_bound] = img_dog
    cv2.imshow('problem 3', img_veg)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    cv2.imwrite(dir_save, img_veg)
    return

prob_3()
