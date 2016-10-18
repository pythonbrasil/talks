import cv2, numpy as np

camera = cv2.VideoCapture(1)
minimo = np.array([100,80,80])
maximo = np.array([130,255,255])

tecla = 0

while tecla != 27:  # 27 = ESC
    _, imagem = camera.read()
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    mascara = cv2.inRange(hsv, minimo, maximo)
    cv2.imshow("imagem", imagem)
    cv2.imshow("mascara",mascara)
    tecla = cv2.waitKey(33)   # 1000 ms / 30 fps = 33
    tecla = tecla & 0xEFFFFF  # tira modificadores


# 0 a 10 = vermelho
# 23 a 32 = amarelo (tente com minimo 23,110,110)
# 45 a 70 = verde
# 100 a 130 = azul
# 150 a 180 = vermelho
# > 180 = nada (max = 360/2)
