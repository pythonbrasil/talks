#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import time

modo_espelho = True  # inverte a imagem horizontalmente

# tecla pressionada (para esperar o ESC e sair)
tecla = 0

# ler stream da webcam
captura = cv2.VideoCapture(1)

# quantidade de arremessos
arremessos = 0

# linha verde
altura_linha = 240

visivel = False  # a bola está na tela?
abaixo = False   # abaixo da linha?
acima = False    # ou acima dela?

# momento da última iteração
ultima_vez = time.time()

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
    cor_alvo_min = np.array([0, 90, 90])
    cor_alvo_max = np.array([10, 255, 255])

    # cópia da imagem em HSV para melhor filtrar a cor
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # obter somente a componente vermelha da imagem
    mascara = cv2.inRange(hsv, cor_alvo_min, cor_alvo_max)

    # identifica os contornos dos objetos vermelhos encontrados
    contornos, hierarquia = cv2.findContours(mascara,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)

    # desenha linha
    cv2.line(imagem,
             (0, altura_linha), (800, altura_linha),  # início e fim
             (0, 255, 0),  # cor verde
             thickness=3)

    # retângulos
    for contorno in contornos:
        if cv2.contourArea(contorno) > 200:  # filtra por tamanho
            visivel = True
            # coordenadas iniciais, largura e altura do contorno
            ret_x, ret_y, ret_w, ret_h = cv2.boundingRect(contorno)
            cv2.rectangle(imagem, (ret_x, ret_y),  # ponto inicial
                          (ret_x + ret_w,          # final x+largura,
                           ret_y + ret_h),         # _     y+altura
                          (0, 255, 255), 2)        # cor e espessura

    # onde está a bola?
    if visivel:
        if ret_y < altura_linha:
            acima = True
        else:
            abaixo = True
            acima = False  # o ponto inicial é abaixo da linha

    # conta os arremessos
    # se a bola já foi vista abaixo e acima da linha,
    # usuário teve sucesso no arremesso.
    if acima and abaixo:
        if time.time() - ultima_vez > 4:  # se demorar mais de 4s,
            arremessos = 0                # zera a contagem
        arremessos += 1
        ultima_vez = time.time()
        abaixo = False
        acima = False

    # mostra contagem
    cv2.putText(imagem,
                '%02d' % arremessos,  # formato 00, com zero à esquerda
                (500, 70),  # localização - alinhada abaixo à esquerda
                cv2.FONT_HERSHEY_TRIPLEX,  # fonte grossa (tripla)
                3, (255, 0, 0))  # tamanho e cor da fonte

    cv2.imshow('ocarneiro/conta-bolas', imagem)
    # cv2.imshow('Resultado', resultado)

    tecla = cv2.waitKey(33)  # 1000ms / 30fps = 33
    tecla = tecla & 0xEFFFFF  # tira NumLock,Caps...
    # if key != -1: print key
