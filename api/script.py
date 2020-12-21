import os
from PIL import Image
from numpy import asarray, squeeze

files_usac = os.listdir('./imagenes/USAC')
files_landivar = os.listdir('./imagenes/Landivar')
files_mariano = os.listdir('./imagenes/Mariano')
files_marroquin = os.listdir('./imagenes/Marroquin')

imagenes = []
for file in files_usac:
    pixeles = []
    image = Image.open('./imagenes/USAC/' + file)
    data = asarray(image)
    for filas in data:
        for pixel in filas:
            pixeles.append(pixel)
    imagenes.append(pixeles)

print(len(imagenes))
print(len(imagenes[0]))