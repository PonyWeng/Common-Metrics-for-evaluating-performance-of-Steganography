# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:14:42 2024

@author: User
"""

import numpy as np
from PIL import Image

def calculate_npcr(image1_path, image2_path):
    # Load the images
    image1 = Image.open(image1_path).convert('L')  # Convert to grayscale
    image2 = Image.open(image2_path).convert('L')  # Convert to grayscale
    
    # Convert images to numpy arrays
    img1_array = np.array(image1)
    img2_array = np.array(image2)
    
    # Ensure the images are of the same size
    if img1_array.shape != img2_array.shape:
        raise ValueError("Images must have the same dimensions for NPCR calculation.")
    
    # Calculate NPCR
    m, n = img1_array.shape
    d = np.sum(img1_array != img2_array)  # Count differing pixels
    npcr = (d / (m * n)) * 100
    
    return npcr

# Example usage
image1_path = 'girl.bmp'
image2_path = 'girlpermutated2w.bmp'

npcr_value = calculate_npcr(image1_path, image2_path)
print(f"NPCR: {npcr_value:.2f}%")
