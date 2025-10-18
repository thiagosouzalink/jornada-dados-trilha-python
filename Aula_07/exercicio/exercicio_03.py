"""
03. Contar Valores Únicos em uma Lista
"""
def contar_valores_unicos(lista: any) -> int:
    print(set(lista))
    return len(set(lista))


lista = [1, "monitor", True, 2, 1, "mouse", "monitor", 0]
print(f"Total valores unicos: {contar_valores_unicos(lista)}")