"""
20. Escreva uma função que receba um dicionário e retorne uma lista de 
chaves ordenadas
"""
def retorna_lista_com_chaves_ordendas(dicionario: dict) -> list:
    return sorted(list(dicionario.keys()))

dicionario = {"d": 1, "a": 5, "c": 2, "b": 3}
print(retorna_lista_com_chaves_ordendas(dicionario))