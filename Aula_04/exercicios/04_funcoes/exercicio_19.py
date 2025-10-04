"""
19. Implemente uma função que receba dois argumentos: uma lista de números e 
um número. A função deve retornar todas as combinações de pares na lista 
que somem ao número dado
"""
def somar_pares_numero_com_numeros(numero: int, lista_numeros: list[int]) -> list[int]:
    return [numero + numero_lista for numero_lista in lista_numeros]
    
    
numero = 2
numeros = [1, 4, 13, 8, 2]
soma = somar_pares_numero_com_numeros(numero, numeros)
print(soma)

