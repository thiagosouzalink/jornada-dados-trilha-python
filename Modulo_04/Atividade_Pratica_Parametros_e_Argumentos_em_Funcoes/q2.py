"""
Atividade Prática - Parâmetros e Argumentos em Funções

Exercício 2 - A ordem dos argumentos

Crie uma função chamada mostrar_partida que receba:

    mandante
    visitante

A função deve exibir os dois times no formato:

Brasil x Argentina


Faça as seguintes chamadas:

mostrar_partida("Brasil", "Argentina")mostrar_partida("Argentina", "Brasil")


Observe como a ordem dos argumentos posicionais altera o resultado.
"""

def mostrar_partida(mandante: str, visitante: str):
    print(f"{mandante} x {visitante}")
    

mostrar_partida("Brasil", "Argentina")
mostrar_partida("Argentina", "Brasil")