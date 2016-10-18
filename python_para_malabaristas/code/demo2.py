import cv2

camera = cv2.VideoCapture(0)

_, imagem = camera.read()

print imagem

print len(imagem[0]), len(imagem)

print imagem[0][0]
