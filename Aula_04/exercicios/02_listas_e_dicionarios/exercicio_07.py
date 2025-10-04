"""
7. Filtragem de Dados
Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são 
maiores ou iguais a 18.
"""
idades = [19, 12, 9, 18, 22, 36, 1, 60, 8, 26]
maior_igual_18 = [idade for idade in idades if idade >= 18]
print(maior_igual_18)