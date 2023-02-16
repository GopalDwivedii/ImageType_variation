import cv2
import matplotlib.pyplot as plt

img = cv2.imread('butterfly.webp')
# Loading the image

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_YCrCb2RGB)
img_rgb1 = cv2.cvtColor(img, cv2.COLOR_LUV2LRGB)
img_rgb2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

half = cv2.resize(img_gray, (780, 1080), fx=0.1, fy=0.1)
bigger = cv2.resize(img_rgb, (1040, 1080), fx=0.2, fy=0.2)
bigg1 = cv2.resize(img_rgb1, (720, 980), fx=0.3, fy=0.3)
bigg2 = cv2.resize(img_rgb2, (700, 500), fx=0.4, fy=0.4)

stretch_near = cv2.resize(img, (780, 1080),interpolation=cv2.INTER_LINEAR)

Titles = ["Original", "Half", "Bigger", "Interpolation Nearest","Experimental", "Nearest", "Nearest1"]
images = [img, half, bigger, stretch_near,bigg1, bigg2]
count = 6

for i in range(count):
    plt.subplot(2, 3, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
plt.show()
