"""
02. Filtrar Dados Acima de um Limite
"""
def filtrar_dados(lista: list[int | float], 
                  limite: int | float) -> list[int | float]:
    return [valor for valor in lista if valor > limite]

LIMITE = 4.5
lista = [2, 4, 3.5, 6, 8.3, 5.5, 6]

print(f"Dados filtrados: {filtrar_dados(lista, LIMITE)}")
