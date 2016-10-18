import cv2

camera = cv2.VideoCapture(0)

_, imagem = camera.read()

cv2.imshow("normal", imagem)
cv2.imshow("menos", -imagem)
cv2.imshow("invertido", imagem[::-1])
cv2.waitKey(0)
