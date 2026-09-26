"""
Atividade Prática - Parâmetros e Argumentos em Funções

Exercício 9 - Trabalhando com os valores de *args


Crie uma função chamada somar_gols que receba uma quantidade indefinida 
de números utilizando *args.


A função deve retornar a soma de todos os valores recebidos.


Exemplo:

total = somar_gols(2, 1, 3, 2)
print(total)


Resultado esperado:
8
"""

def somar_gols(*gols) -> int:
    return sum(gols)


total = somar_gols(2, 1, 3, 2)
print(total)