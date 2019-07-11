import cv2
img=cv2.imread('D:\Comp_vis\standard_test_images\standard_test_images\livingroom.tif',cv2.IMREAD_COLOR)
img1=cv2.imread('D:\Comp_vis\standard_test_images\standcv2.ard_test_images\lena_color_512.tif',cv2.IMREAD_COLOR)
cv2.imshow('image',img)
cropped=img[70:70,240:340]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()