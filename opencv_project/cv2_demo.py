import cv2

im_g = cv2.imread('file/Green_Dice.png', 1)
print(im_g)
cv2.imwrite('file/file.png',im_g)
