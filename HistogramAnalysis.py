import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read the image (CoverImage or StegoImage)
img = cv2.imread('Final_Stego.bmp')

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert BGR to RGB for proper display in Matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display the image using Matplotlib
    plt.imshow(img_rgb)
    plt.axis('off')  # Hide axis
    plt.title("Image")  # Optional title
    plt.show()

    # Create histogram
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    # Generate histogram, value range is [0-255]
    plt.hist(img.ravel(), 256, [0, 256], density=False)

    # Show histogram results
    plt.title("Histogram")
    plt.show()
