"""
06. Encontrar Valores Ausentes em uma Sequência
an = a1 + (n-1)*r
r = (an - a1) / (n-1)
"""


def obter_valores_ausentes_sequencia(lista_numerica: list[int]) -> list[int]:
    if not lista_numerica:
        return []
    sequencia_esperada = range(min(lista_numerica), max(lista_numerica)+1)
    valores_ausentes = set(sequencia_esperada) - set(lista_numerica)
    return sorted(list(valores_ausentes))

lista = [1, 2, 3, 5, 6, 8, 9, 10]
sequencia_esperada = obter_valores_ausentes_sequencia(lista)
print(f"Valores ausentes na sequência {lista} -> {sequencia_esperada}")
