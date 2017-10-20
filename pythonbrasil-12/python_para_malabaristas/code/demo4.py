import cv2, numpy as np
camera = cv2.VideoCapture(0)

min = np.array([0,0,80])
max = np.array([90,90,255])
_, imagem = camera.read()

mascara = cv2.inRange(imagem, min, max)
cv2.imshow("original", imagem)
cv2.imshow("filtro", mascara)
cv2.waitKey(0)
