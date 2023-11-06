import  cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread("textjojo_new.jpg",cv.IMREAD_COLOR)
h=img.shape[0]
w=img.shape[1]
img_copyedge=np.zeros((h+2,w+2,3),dtype=np.float32)
for i in range(1,h+1):
    for j in range(1,w+1):
        img_copyedge[i,j] =img[i-1,j-1]
for i in range(w):
    img_copyedge[0,i+1]=img[1,i]
    img_copyedge[h+1,i+1]=img[h-1,i]
for i in range(h):
    img_copyedge[i+1,0]=img[i,1]
    img_copyedge[i+1,w+1]=img[i,w-1]
img_copyedge[0,0]=img[0,0]
img_copyedge[0,w+1]=img[0,w-1]
img_copyedge[h+1,0]=img[h-1,0]
img_copyedge[h+1,w+1]=img[h-1][w-1]
plt.imshow(img[::,::,::-1])
plt.show()