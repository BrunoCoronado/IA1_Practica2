import os
from PIL import Image
import numpy as np

def obtenerImagenes(universidad):
    files = os.listdir('./imagenes/' + universidad)
    imagenes = []
    for file in files:
        pixeles = []
        image = Image.open('./imagenes/' + universidad + '/' + file)
        imagenes.append(np.append(np.asarray(image).reshape(-1), [1]))
    result = np.array(imagenes)
    np.random.shuffle(result)
    # return result.astype(float)
    result = result.astype(float).T

    # Se separa el conjunto de pruebas del de entrenamiento
    slice_point = int(result.shape[1] * 0.8)
    train_set = result[:, 0: slice_point]
    test_set = result[:, slice_point:]

    # Se separan las entradas de las salidas
    train_set_x_orig = train_set[0: 3, :]
    train_set_y_orig = np.array([train_set[3, :]])

    test_set_x_orig = test_set[0: 3, :]
    test_set_y_orig = np.array([test_set[3, :]])

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, ['Perdera', 'Ganara']