
from PIL import Image
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2 

img = Image.open("Final_Stego.bmp")
analysis_img= img.copy()

customed_threshold = 100

for y in range(0,512,2):
    for x in range(0,512,2):
        p1= img.getpixel((x,y))
        p2= img.getpixel((x+1,y))
        p3= img.getpixel((x,y+1))
        p4= img.getpixel((x+1,y+1))

        Pval = (p1+p2+p3+p4)/4

        d1 = abs(p1 -Pval)
        d2 = abs(p2 -Pval)
        d3 = abs(p3 -Pval)
        d4 = abs(p4 -Pval)

        Fval = (d1+d2+d3+d4)/4

        

        if Fval>customed_threshold:
            analysis_img.putpixel((x,y),255)
            analysis_img.putpixel((x+1,y),255)
            analysis_img.putpixel((x,y+1),255)
            analysis_img.putpixel((x+1,y+1),255)
        else:
            analysis_img.putpixel((x,y),0)
            analysis_img.putpixel((x+1,y),0)
            analysis_img.putpixel((x,y+1),0)
            analysis_img.putpixel((x+1,y+1),0)


analysis_img.save("Complexility_analysis.bmp")

image=Image.open("Complexility_analysis.bmp")
plt.imshow(image)
plt.show()

# image = cv2.imread("Complexility_analysis.bmp")
# cv2.imshow("Result",image)
# cv2.waitKey(0)
# cv2.DestroyAllWindows()