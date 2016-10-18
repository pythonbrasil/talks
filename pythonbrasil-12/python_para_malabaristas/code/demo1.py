import cv2

camera = cv2.VideoCapture(0)

_, imagem = camera.read()

cv2.imshow("", imagem)
cv2.waitKey(2000)

cv2.imwrite("foto.jpg", imagem)
