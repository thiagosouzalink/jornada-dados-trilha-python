"""
01. Calcular Média de Valores em uma Lista
"""
from typing import Union


def calcular_media_lista(lista_numeros: list[int | float]) -> float:
    return sum(lista_numeros) / len(lista_numeros)

lista = [2, 5, 8, 4]
print(f"Media: {calcular_media_lista(lista):.2f}")