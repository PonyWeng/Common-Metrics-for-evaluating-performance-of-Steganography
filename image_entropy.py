import numpy as np
import cv2 

def calculate_entropy(image):
   
    hist, _ = np.histogram(image.flatten(), bins=256, range=(0,256))
    hist = hist / np.sum(hist)
    entropy = -np.sum(hist * np.log2(hist + 1e-10)) 
    return entropy

gray_image = cv2.imread('Final_Stego.bmp', cv2.IMREAD_GRAYSCALE)
entropy = calculate_entropy(gray_image)
print("Entropy of the gray image:", entropy)
