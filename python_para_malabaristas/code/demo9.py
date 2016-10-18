import cv2, numpy as np

camera = cv2.VideoCapture(1)
minimo = np.array([100,80,80])
maximo = np.array([150,255,255])

tecla = 0

while tecla != 27:  # 27 = ESC
    _, imagem = camera.read()
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    mascara = cv2.inRange(hsv, minimo, maximo)
    contornos, _ = cv2.findContours(mascara.copy(),
                          cv2.RETR_LIST,
                          cv2.CHAIN_APPROX_SIMPLE)
    for contorno in contornos:
        x, y, w, h = cv2.boundingRect(contorno)
        cv2.rectangle(imagem, (x, y), (x + w, y + h),
                                (0, 255, 255), 2)    
    cv2.imshow("imagem", imagem)
    tecla = cv2.waitKey(33)   # 1000ms / 30fps = 33
    tecla = tecla & 0xEFFFFF  # tira NumLock,Caps...

# 0 a 10 = vermelho
# 23 a 32 = amarelo (tente com minimo 23,110,110)
# 45 a 70 = verde
# 100 a 130 = azul
# 150 a 180 = vermelho
# > 180 = nada (max = 360/2)
