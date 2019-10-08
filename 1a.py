import numpy as np
import cv2

def ex1a():
    img = cv2.imread("robo.jpg",cv2.IMREAD_COLOR)
    cv2.imshow('imagem',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
