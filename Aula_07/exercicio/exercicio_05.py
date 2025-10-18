"""
05. Calcular Desvio Padrão de uma Lista
"""
import math


def calcular_media(lista_numeros: list[int | float]) -> float:
    return sum(lista_numeros) / len(lista_numeros)

def calcular_variancia(lista_numeros: list[int | float]) -> float:
    media = calcular_media(lista_numeros)
    return sum([(n - media)**2 for n in lista_numeros]) / len(lista_numeros)

def calcular_desvio_padrao(lista_numeros: list[int | float]) -> float:
    return math.sqrt(calcular_variancia(lista_numeros))

numeros = [1.55, 1.7, 1.8]
print(f"Desvio Padrão: {calcular_desvio_padrao(numeros):.4f}")