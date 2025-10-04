"""
16. Escreva uma função que receba uma lista de números e retorne a soma 
de todos os números.
"""

def somar_numeros_lista(lista_numeros: list) -> int | float:
    return sum(lista_numeros)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = somar_numeros_lista(numeros)
print(soma)