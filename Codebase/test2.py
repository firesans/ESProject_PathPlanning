from numpy import array
import numpy as np
import cv2
img = cv2.imread('sol.png',0)
res = cv2.resize(img, dsize=(50, 37), interpolation=cv2.INTER_CUBIC)
arr = array(res)

for i in range(len(arr)):
	for j in range(len(arr[i])):
		if (arr[i][j] >= 2.0):
			arr[i][j] = int(1)
		else:
			arr[i][j] = int(0)

for i in range(len(arr)):
	ind = []
	for j in range(len(arr[i])):
		if arr[i][j] != 0:
			ind.append(j)
	print(ind)
	parity = 1; 
	for j in range(len(ind)-1):
		for k in range(ind[j],ind[j+1]):
			arr[i][k] = int(parity)
		parity = parity!=1

np.savetxt('file.txt', arr.astype(int), fmt='%i', delimiter=',')
