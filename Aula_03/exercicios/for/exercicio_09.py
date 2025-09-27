"""
9. Extração de Subconjuntos de Dados
Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.
"""
numeros = [1, 9, 8, 6, 21, 36, 45, 2, 7, 32]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)