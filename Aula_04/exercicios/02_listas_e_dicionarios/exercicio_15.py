"""
15. Contagem de Frequência de Itens
Objetivo: Dada uma string, contar a frequência de cada caractere usando 
um dicionário.
"""
string = "Penso, logo existo"
caracters_quantidade = {}
for caracter in string:
    quantidade = caracters_quantidade.get(caracter.lower(), 0)
    caracters_quantidade[caracter.lower()] = quantidade + 1
print(caracters_quantidade)