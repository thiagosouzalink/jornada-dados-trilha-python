"""
10. Divisão de Dados em Grupos
Objetivo: Dada uma lista de valores, dividir em duas listas: uma para 
valores pares e outra para ímpares.
"""
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if not valor % 2]
impares = [valor for valor in valores if valor % 2]

print(f"Pares: {pares}")
print(f"Impares: {impares}")