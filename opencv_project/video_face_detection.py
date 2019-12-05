import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture('file/video.mp4')
while cap.isOpened():
    _,  img = cap.read()
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey_img, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
    resized = cv2.resize(img, (img.shape[1] // 3, img.shape[0] // 3))
    cv2.imshow('Video Face Detection', resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
