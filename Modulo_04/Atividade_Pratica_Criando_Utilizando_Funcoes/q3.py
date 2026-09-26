"""
Atividade Prática - Criando e Utilizando Funções

Exercício 3 - Calculando o valor de uma compra

Crie uma função chamada calcular_total() que receba:

    o preço de um produto;
    a quantidade comprada.


A função deve calcular e retornar o valor total da compra.

Exemplo:

total = calcular_total(50.0, 3)
print(total)

Resultado esperado: 150.0

Requisitos:

    preco deve possuir type hint float.
    quantidade deve possuir type hint int.
    A função deve indicar que retorna um float.
    Utilize return para devolver o resultado.
"""

def calcular_total(preco: float, quantidade: int) -> float:
    return preco * quantidade


total = calcular_total(50.0, 3)
print(total)

total = calcular_total(25.5, 5)
print(total)