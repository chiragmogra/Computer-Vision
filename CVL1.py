import cv2
img=cv2.imread('D:\Comp_vis\standard_test_images\standard_test_images\livingroom.tif',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''import matplotlib.pyplot as plt
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.show()''' # optional way to present image
# save this image file
cv2.imwrite('mmgray.png',img)
