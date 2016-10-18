import cv2
import numpy as np

camera = cv2.VideoCapture(1)
minimo = np.array([100, 80, 80])
maximo = np.array([132, 255, 255])
_, imagem = camera.read()
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
mascara = cv2.inRange(hsv, minimo, maximo)
cv2.imshow("imagem", imagem)
cv2.imshow("mascara", mascara)
cv2.waitKey(0)

# 0 a 10 = vermelho
# 23 a 32 = amarelo (tente com minimo 23,110,110)
# 45 a 70 = verde
# 100 a 130 = azul
# 150 a 180 = vermelho
# > 180 = nada (max = 360/2)
