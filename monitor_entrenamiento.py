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
    pass


# ==========================================
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA)
# ==========================================

if __name__ == "__main__":
    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")