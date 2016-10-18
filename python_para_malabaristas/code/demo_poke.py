#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import time
import pokecv

modo_espelho = True  # inverte a imagem horizontalmente

# tecla pressionada (para esperar o ESC e sair)
tecla = 0

# ler stream da webcam
captura = cv2.VideoCapture(1)

while tecla != 27:  # tecla ESC
    _, imagem = captura.read()

    if modo_espelho:
        cv2.flip(imagem, 1, imagem)

    # HSV - hue (matiz), saturação, valor
    #   valores para H:
    #       0 a 10 = vermelho vivo
    #       23 a 32 = amarelo
    #       45 a 70 = verde
    #       100 a 130 = azul
    #       150 a 180 = vermelho azulado
    #       > 180 = nada (max = 360/2)
    #   valores para S e V:
    #       manter próximo de 0 no mínimo
    #       e próximo de 255 para o máximo
    minimo = np.array([100,80,80])
    maximo = np.array([150,255,255])
    cor_alvo_min = minimo
    cor_alvo_max = maximo

    # cópia da imagem em HSV para melhor filtrar a cor
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # obter somente a componente vermelha da imagem
    mascara = cv2.inRange(hsv, cor_alvo_min, cor_alvo_max)

    # identifica os contornos dos objetos vermelhos encontrados
    contornos, hierarquia = cv2.findContours(mascara,
                                             cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)

    cor_criatura = (0, 255, 255)  # amarelo

    # retângulos
    for contorno in contornos:
        if cv2.contourArea(contorno) > 200:  # filtra por tamanho
            # coordenadas iniciais, largura e altura do contorno
            ret_x, ret_y, ret_w, ret_h = cv2.boundingRect(contorno)
            centro_x = ret_x + int(ret_w/2)
            centro_y = ret_y + int(ret_h/2)
            raio = int(ret_w/2)
            poke = pokecv.Poke((centro_x, centro_y), raio)
            poke.draw_creature(imagem, cor_criatura)

    cv2.imshow("Poke!", imagem)
    tecla = cv2.waitKey(33)  # 1000ms / 30fps = 33
    tecla = tecla & 0xEFFFFF  # tira NumLock,Caps...
    # if key != -1: print key
