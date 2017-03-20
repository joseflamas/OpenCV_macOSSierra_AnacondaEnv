import cv2
import numpy as np

images_data_path = '/Users/memo/_sublime/OpenCV/tests/data/images/'

img = cv2.imread( images_data_path + 'flor.png')


px = img[100,100]
print(px)

# accessing only blue pixel
blue = img[100,100,0]
print(blue)


img[100,100] = [255,255,255]
print(img[100,100])

# accessing RED value
img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)


print(img.shape)
print(img.size)
print(img.dtype)

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

b = img[:,:,0]
img[:,:,2] = 0

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF #esc
    if k == 27:
        break

cv2.destroyAllWindows()