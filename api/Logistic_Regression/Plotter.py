from Logistic_Regression.Model import Model
import matplotlib.pyplot as chart

def guardarModelo(modelos, nombre):
    chart.clf()
    for modelo in modelos:
        chart.plot(modelo.bitacora, label=str(modelo.alpha))
    chart.ylabel('Costo')
    chart.xlabel('Iteraciones')
    legend = chart.legend(loc='upper center', shadow=True)
    chart.savefig(nombre)