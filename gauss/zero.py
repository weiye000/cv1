import matplotlib.pyplot as plt
import math
import cv2 as cv
import numpy as np
img=cv.imread("textjojo.jpg",cv.IMREAD_COLOR)
h=img.shape[0]
w=img.shape[1]
zero_padding=np.zeros((h+2,w+2,3),dtype=np.int16)
for i in range(1,h+1):
    for j in range(1,w+1):
        zero_padding[i,j] =img[i-1,j-1]
plt.imshow(zero_padding[::,::,::-1])
plt.show()