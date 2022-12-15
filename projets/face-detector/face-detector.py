import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('ld.jpg')
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

print(faces_coordinates)

cv2.imshow('Face Detector App', grayscaled_img)
cv2.waitKey()




print('hello world !')