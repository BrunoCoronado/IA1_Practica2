from FileManagement import File
from Logistic_Regression.Data import Data
from Logistic_Regression.Model import Model
from Logistic_Regression import Plotter
import numpy as np

train_set_usac, test_set_usac = File.obtenerImagenes('USAC')
train_set_landivar, test_set_landivar = File.obtenerImagenes('Landivar')
train_set_mariano, test_set_mariano = File.obtenerImagenes('Mariano')
train_set_marroquin, test_set_marroquin = File.obtenerImagenes('Marroquin')

model1 = Model(train_set_usac, test_set_usac, reg=False, alpha=0.001, lam=150, it=400)
model2 = Model(train_set_usac, test_set_usac, reg=False, alpha=0.002, lam=200, it=475)
model3 = Model(train_set_usac, test_set_usac, reg=False, alpha=0.0015, lam=200, it=525)
model4 = Model(train_set_usac, test_set_usac, reg=False, alpha=0.0025, lam=175, it=490)
model5 = Model(train_set_usac, test_set_usac, reg=False, alpha=0.003, lam=210, it=500)

model1.training()
model2.training()
model3.training()
model4.training()
model5.training()

Plotter.guardarModelo([model1, model2, model3, model4, model5], 'USAC.png')

model1 = Model(train_set_landivar, test_set_landivar, reg=False, alpha=0.001, lam=150, it=400)
model2 = Model(train_set_landivar, test_set_landivar, reg=False, alpha=0.002, lam=200, it=475)
model3 = Model(train_set_landivar, test_set_landivar, reg=False, alpha=0.0015, lam=200, it=525)
model4 = Model(train_set_landivar, test_set_landivar, reg=False, alpha=0.0025, lam=175, it=490)
model5 = Model(train_set_landivar, test_set_landivar, reg=False, alpha=0.003, lam=210, it=500)

model1.training()
model2.training()
model3.training()
model4.training()
model5.training()

Plotter.guardarModelo([model1, model2, model3, model4, model5], 'Landivar.png')



