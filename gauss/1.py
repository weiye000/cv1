import numpy as np
import sys

import matplotlib.pyplot as plt
kernel_size= 5 #optional
sigma=1 #optional
sigma_3=sigma*3
X=np.linspace(-sigma_3,sigma_3,kernel_size)
Y=np.linspace(-sigma_3,sigma_3,kernel_size)
x,y=np.meshgrid(X,Y)
guass_1=1/((2*np.pi)**0.5*sigma)*np.exp(-(x**2+y**2)/(2*sigma**2))
Z=guass_1.sum()
guass_2=(1/Z)*guass_1
plt.imshow(guass_2,cmap='gray',origin='lower',extent=[-sigma_3,sigma_3,-sigma_3,sigma_3])
plt.xlabel("X");plt.ylabel("Y")
plt.show()
