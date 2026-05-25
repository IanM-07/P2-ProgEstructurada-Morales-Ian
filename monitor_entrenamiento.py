"""
Nombre del Alumno: Ian Morales
Matrícula: UX25II023
Fecha: 25/05/2026
Examen Segundo Parcial - Programación Estructurada
"""

# ==========================================
# 1. IMPORTACIÓN DE BIBLIOTECAS ESTÁNDAR
# ==========================================

import datetime
import math
import random
import statistics
import sys

# ==========================================
# 2. DEFINICIÓN DE CONSTANTES
# ==========================================

MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO = 0.95

# ==========================================
# 3. FUNCIONES DEFINIDAS POR EL USUARIO
# ==========================================

def obtener_info_sistema():
    """
    Usa la biblioteca 'sys' para validar el entorno de ejecución.
    """

    print("\n=== INFORMACIÓN DEL SISTEMA ===")

    print("Plataforma:", sys.platform)

    print("Versión de Python:")

    print(sys.version)

    print("Argumentos del sistema:")

    print(sys.argv)


def simular_metricas_entrenamiento(cantidad_epochs):
    """
    Usa las bibliotecas 'random' y 'datetime' para simular los datos de entrenamiento.
    """

    print("\n=== SIMULACIÓN DE ENTRENAMIENTO ===")

    inicio = datetime.datetime.now()

    fecha_formateada = inicio.strftime("%d/%m/%Y %H:%M:%S")

    print("Inicio del entrenamiento:", fecha_formateada)

    lista_loss = []

    eventos = [
        "Epoch exitoso",
        "Gradiente inestable",
        "Actualización de pesos"
    ]

    for epoch in range(cantidad_epochs):

        loss = round(random.uniform(0.1, 1.0), 3)

        probabilidad = round(random.random(), 3)

        evento = random.choice(eventos)

        lista_loss.append(loss)

        print("\nEpoch:", epoch + 1)
        print("Loss:", loss)
        print("Probabilidad de éxito:", probabilidad)
        print("Evento:", evento)

    fin = datetime.datetime.now()

    diferencia = fin - inicio

    print("\nTiempo total del entrenamiento:", diferencia)

    return lista_loss


def analizar_rendimiento(lista_loss):
    """
    Usa la biblioteca 'statistics' para analizar el comportamiento del entrenamiento.
    """

    print("\n=== ANÁLISIS DE RENDIMIENTO ===")

    media = statistics.mean(lista_loss)

    desviacion = statistics.stdev(lista_loss)

    mediana = statistics.median(lista_loss)

    print("Media del loss:", round(media, 3))

    print("Desviación estándar:", round(desviacion, 3))

    print("Mediana del entrenamiento:", round(mediana, 3))

    if media >= UMBRAL_ERROR_CRITICO:

        print("\nERROR CRÍTICO DETECTADO")

        sys.exit()


def calcular_rmse(predicciones, reales):
    """
    Usa la biblioteca 'math' para calcular el Root Mean Squared Error (RMSE).
    """

    print("\n=== CÁLCULO RMSE ===")

    suma = 0

    for i in range(len(predicciones)):

        diferencia = reales[i] - predicciones[i]

        cuadrado = math.pow(diferencia, 2)

        suma += cuadrado

    media = suma / len(predicciones)

    rmse = math.sqrt(media)

    epochs_redondeados = math.ceil(rmse)

    print("RMSE:", round(rmse, 3))

    print("Epochs redondeados:", epochs_redondeados)


# ==========================================
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA)
# ==========================================

if __name__ == "__main__":

    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")

    obtener_info_sistema()

    lista_loss = simular_metricas_entrenamiento(MAX_EPOCHS)

    analizar_rendimiento(lista_loss)

    predicciones = [0.8, 0.7, 0.9, 0.6]

    reales = [1.0, 0.9, 1.0, 0.8]

    calcular_rmse(predicciones, reales)

"""
CUESTIONARIO DE ANÁLISIS DE BIBLIOTECAS

1. En datetime.datetime.now(), datetime es la clase que viene de la biblioteca datetime y now() es el método que usamos para obtener la fecha y hora actual. Esto se relaciona con las bibliotecas externas porque usamos herramientas ya hechas por Python en lugar de programarlas desde cero.

2. La diferencia es que cuando usamos import math debemos escribir math.sqrt() o math.pow() para usar las funciones. En cambio, si usamos from math import sqrt, podemos escribir solo sqrt(). En el código usé import math para identificar mejor de qué biblioteca viene cada funcion.

3. Primero la función de simulación genera los valores de loss y los guarda en una lista. Después esa lista se manda a la función de análisis para calcular estadísticas. Y al final, se usan listas de predicciones y valores reales para calcular el RMSE y medir el error.

4. Utilicé listas para guardar los valores de loss, los eventos y también las predicciones y valores reales. Las elegi ya que pueden guardar muchos datos e implementar ciclos facilmente, con variables simples esto seria mas complicado.

5. No tuve que hacer manualmente la fórmula de la desviación estándar porque la biblioteca statistics ya incluye la función stdev(). Esto se relaciona con la abstracción porque Python ya tiene estas herramientas preparadas para no tener que pasar por toda una logica extensa.
"""