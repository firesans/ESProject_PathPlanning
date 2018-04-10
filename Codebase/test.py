import numpy as np
import cv2
from matplotlib import pyplot as plt

imgR = cv2.imread('l.png',0)
imgL = cv2.imread('r.png',0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=87)
disparity = stereo.compute(imgL,imgR)

plt.imshow(disparity,'gray')
plt.show()
cv2.imwrite('sol.png',disparity)
