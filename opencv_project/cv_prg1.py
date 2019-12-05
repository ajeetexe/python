import cv2

img = cv2.imread('file/image.jpg', 0)
resize = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
print(img)
print(img.shape)
cv2.imshow('baby', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
