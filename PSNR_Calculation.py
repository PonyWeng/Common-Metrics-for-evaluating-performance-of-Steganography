import numpy as np
import math 
from PIL import Image


def psnr(target, ref):
    # target:目標影像  ref:參考影像 
    target_data = np.array(target)
    ref_data = np.array(ref)
    diff = ref_data - target_data
    diff = diff.flatten('C')
    mse = np.mean((target_data/1.0 - ref_data/1.0) ** 2 )

    return 10 * math.log10(255.0**2/mse)


img = Image.open('man.bmp')
img1 = Image.open('Stego.bmp')

print("PSNR=",psnr(img,img1))