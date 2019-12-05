import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread('file/myPic.jpg')
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(grey_img, scaleFactor=1.1, minNeighbors=5)
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
resized = cv2.resize(img, (img.shape[1] // 5, img.shape[0] // 5))

cv2.imshow("Image_Detect", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
