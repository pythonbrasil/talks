import cv2
camera = cv2.VideoCapture(1)
_, imagem = camera.read()
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
hsv[:,:,1] = -1  # saturacao maxima!
hsv[:,:,2] = -1  # valor maximo!
cor = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("cor",cor)
cv2.waitKey(0)
