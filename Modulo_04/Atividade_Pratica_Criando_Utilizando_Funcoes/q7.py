"""
Atividade Prática - Criando e Utilizando Funções

Exercício 7 - Calculando consumo médio

Um veículo percorreu determinada distância utilizando uma quantidade de 
combustível.

Crie uma função chamada calcular_consumo_medio() que receba:

    distância percorrida em quilômetros;
    quantidade de litros utilizados.


A função deve retornar quantos quilômetros o veículo percorreu por litro.

Exemplo: consumo = calcular_consumo_medio(420.0, 35.0)
Resultado: 12.0

Depois, crie uma segunda função chamada exibir_consumo() que receba o 
resultado e exiba: Consumo médio: {resultado} km/l

Requisitos:

    As duas funções devem possuir type hints.
    calcular_consumo_medio() deve retornar float.
    exibir_consumo() deve retornar None.
    As duas funções devem possuir docstrings.
    O resultado da primeira função deve ser passado como argumento para 
    a segunda.
"""

def calcular_consumo_medio(
    distancia_percorrida: float, 
    quantidade_litros: float
) -> float:
    """Função que calcula o consumo médio.

    Args:
        distancia_percorrida (float): Distância percorrida em quilômetros.
        quantidade_litros (float): Quantidade de litros utilizados.

    Returns:
        float: Consumo médio.
    """
    consumo_medio = distancia_percorrida / quantidade_litros
    return consumo_medio


def exibir_consumo(consumo_medio: float):
    """Função que exibe o consumo médio.

    Args:
        consumo_medio (float): Valor do consumo médio (km/l)
    """
    print(f"Consumo médio: {consumo_medio:.2f} km/l")


consumo = calcular_consumo_medio(420.0, 35.0)
exibir_consumo(consumo)
