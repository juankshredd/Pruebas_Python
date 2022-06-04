# importimg libraries
import cv2
import numpy as np

#reading image debe tener la ruta a la foto en la pc
img = cv2.imread("Pruebas_Python\Mini Proyectos Python JK\image to cartoon\_fotoEdilberto.jpg")

# edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
edges = cv2.adaptiveThreshold(gray, 225, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 3)

# Cartoonization
color = cv2.bilateralFilter(img, 13, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

img1 = cv2.imshow("image", img)
img2 = cv2.imshow("edges", edges)

img3 = cv2.imwrite("Cartoon1.png", edges)


cv2.waitKey(0)
cv2.destroyAllWindows()