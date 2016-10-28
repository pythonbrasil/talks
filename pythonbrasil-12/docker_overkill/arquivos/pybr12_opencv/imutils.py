import numpy as np
import cv2


def translate(image, x, y):

    # matriz de translacao tem que ser do tipo float
    # na primeira linha o ultimo numero diz quantos px vao sofrer o shift
    # pra direita ou esquerda (valores positivos - direita, valores negativos -
    # esquerda
    # na segunda linha, ultimo numero diz quantos px vao sofrer o shift
    # pra cima ou baixo (valores positivos - baixo, valores negativos - cima)
    M = np.float32([[1, 0, x], [0, 1, y]])
    # funcao que faz a translacao, imagem a ser transformada, matriz de traslacao,
    # altura da imagem a ser modificada,
    # largura da imagem a ser modificada
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted


def rotate(image, angle, center=None, scale=1.0):

    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):

    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized
