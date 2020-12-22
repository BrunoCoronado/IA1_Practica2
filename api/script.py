# import os
# from PIL import Image
# from numpy import asarray, squeeze, random, array
# import FileMa

# files_usac = os.listdir('./imagenes/USAC')
# files_landivar = os.listdir('./imagenes/Landivar')
# files_mariano = os.listdir('./imagenes/Mariano')
# files_marroquin = os.listdir('./imagenes/Marroquin')

# imagenes = []
# for file in files_usac:
#     pixeles = []
#     image = Image.open('./imagenes/USAC/' + file)
#     imagenes.append(asarray(image).reshape(-1))
# result = array(imagenes)
# random.shuffle(result)
# print(result.astype(float))
# # return imagenes.astype(float)

# # imagenes = []
# # for file in files_usac:
# #     pixeles = []
# #     image = Image.open('./imagenes/USAC/' + file)
# #     imagenes.append(asarray(image).reshape(-1))

# # print(len(imagenes))
# # print(len(imagenes[0]))
# print(len(result))
# print(len(result[0]))

# from FileManagement import File

# print(File.obtenerImagenes('USAC'))
# print(File.obtenerImagenes('Landivar'))
# print(File.obtenerImagenes('Mariano'))
# print(File.obtenerImagenes('Marroquin'))

from FileManagement import File
from Logistic_Regression.Data import Data
from Logistic_Regression.Model import Model
from Logistic_Regression import Plotter
import numpy as np

# Se obtienen los datos
train_set_x, train_set_y, test_set_x, test_set_y, classes = File.obtenerImagenes('USAC')


# Definir los conjuntos de datos
train_set = Data(train_set_x, train_set_y, 255)
test_set = Data(test_set_x, test_set_y, 255)

# Se entrenan los modelos
model1 = Model(train_set, test_set, reg=False, alpha=0.001, lam=150, it=400)
model1.training()

model2 = Model(train_set, test_set, reg=False, alpha=0.002, lam=200, it=475)
model2.training()

model3 = Model(train_set, test_set, reg=False, alpha=0.0015, lam=200, it=525)
model3.training()

model4 = Model(train_set, test_set, reg=False, alpha=0.0025, lam=175, it=490)
model4.training()

model5 = Model(train_set, test_set, reg=False, alpha=0.003, lam=210, it=500)
model5.training()

# Se grafican los entrenamientos
Plotter.show_Model([model1, model2, model3, model4, model5])