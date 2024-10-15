
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:21:18 2024

@author: User
"""

import numpy as np
from PIL import Image

def calculate_uaci(image1_path, image2_path):
    # Load the images
    image1 = Image.open(image1_path).convert('L')  # Convert to grayscale
    image2 = Image.open(image2_path).convert('L')  # Convert to grayscale
    
    # Convert images to numpy arrays
    img1_array = np.array(image1)
    img2_array = np.array(image2)
    
    # Ensure the images are of the same size
    if img1_array.shape != img2_array.shape:
        raise ValueError("Images must have the same dimensions for UACI calculation.")
    
    # Calculate UACI
    m, n = img1_array.shape
    diff = np.abs(img1_array - img2_array)  # Absolute difference between pixels
    uaci = (np.sum(diff) / (m * n * 255)) * 100
    
    return uaci

# Example usage
image1_path = 'lake.bmp'
image2_path = 'lakepermutated2w.bmp'

uaci_value = calculate_uaci(image1_path, image2_path)
print(f"UACI: {uaci_value:.2f}%")
