import os
from PIL import Image
import numpy as np
from Logistic_Regression.Data import Data

def obtenerImagenes(universidad):
    universidades = ['Landivar', 'Mariano', 'Marroquin', 'USAC']
    imagenes = []

    for u in universidades:
        files = os.listdir('./imagenes/' + u)
        for file in files:
            pixeles = []
            image = Image.open('./imagenes/' + u + '/' + file)
            if universidad == u:
                imagenes.append(np.append(np.asarray(image).reshape(-1), [1]))
                # imagenes.append(np.append(u, [1]))
            else: 
                imagenes.append(np.append(np.asarray(image).reshape(-1), [0]))
                # imagenes.append(np.append(u, [0]))


    result = np.array(imagenes)
    np.random.shuffle(result)
    # return result.astype(float)
    result = result.astype(float).T

    # Se separa el conjunto de pruebas del de entrenamiento
    slice_point = int(result.shape[1] * 0.8)
    train_set = result[:, 0: slice_point]
    test_set = result[:, slice_point:]

    # Se separan las entradas de las salidas
    # train_set_x_orig = train_set[0: 49152, :]
    # train_set_y_orig = np.array([train_set[49152, :]])

    # test_set_x_orig = test_set[0: 49152, :]
    # test_set_y_orig = np.array([test_set[49152, :]])

    # train_set = Data(train_set[0: 49152, :], np.array([train_set[49152, :]]), 255)
    # test_set = Data(test_set[0: 49152, :], np.array([test_set[49152, :]]), 255)

    # return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig

    return Data(train_set[0: 49152, :], np.array([train_set[49152, :]]), 255), Data(test_set[0: 49152, :], np.array([test_set[49152, :]]), 255)

    # result = np.array(imagenes)
    # print(result.astype(str))
    # return [], [], [], [], ['Es ' + universidad, 'No es' + universidad]