import cv2
import numpy as np

img = cv2.imread("lenna_small.png", 0)

kernel_size = 3
stride = 1
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

feature_map_size = ((img.shape[0] - kernel_size) / stride) + 1
feature_map = np.zeros((feature_map_size, feature_map_size))

for i in range(0, feature_map_size, stride):
    for j in range(0, feature_map_size, stride):
        feature_map[i, j] = np.sum(img[i:i+kernel_size, j:j+kernel_size] * kernel)

cv2.imwrite('convolved.png', feature_map)
