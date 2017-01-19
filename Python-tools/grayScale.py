import cv2

i = 0

for i in range(0):
    image = cv2.imread(str(i) + ".jpg", cv2.IMREAD_GRAYSCALE)
    
    cv2.imwrite(str(i) + ".jpg", image)
