import cv2

camera = cv2.VideoCapture(1)

tecla = 0

while tecla != 27:  # 27 = ESC
    _, imagem = camera.read()
    cv2.imshow("imagem", imagem)
    tecla = cv2.waitKey(33)   # 1000ms / 30 fps = 33
    tecla = tecla & 0xEFFFFF  # tira modificadores
