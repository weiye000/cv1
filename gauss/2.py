import numpy as np
import matplotlib.pyplot as plt
import math
import cv2 as cv
def guasskernel(size,sigma):
    
    guasskernel=np.zeros((size,size),np.float32)
    for i in range(size):
        for j in range(size):
            norm=math.pow(i-size//2,2)+pow(j-size//2,2)
            guasskernel[i,j]=math.exp(-norm/(2*math.pow(sigma,2)))
    sum=np.sum(guasskernel)
    kernel=guasskernel/sum
    return kernel
def guass(img):
    h=img.shape[0]
    w=img.shape[1]
    img1=np.zeros((h,w),np.uint8)
    kernel=guasskernel(3,1.0)
    for i in range(1,h-1):
        for j in range(1,w-1):
            sum=0
            for k in range(-1,2):
                for l in range(-1,2):
                    sum+=img[i+k,j+l]*kernel[k+1,l+1]
            img1[i,j]=int(sum)
    return img1
if __name__ == '__main__':
    img=cv.imread("textjojo_new.jpg")
    img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img_guass=guass(img_gray)
    plt.subplot(111)
    plt.imshow(img_guass,cmap='gray')
    plt.title("guass filtering")
    plt.show()




