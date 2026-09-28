"""
Atividade Prática - Criando e Utilizando Funções

Exercício 2 - Identificando um produto

Crie uma função chamada exibir_produto() que receba:

    o nome de um produto;
    o preço do produto.


A função deve exibir uma mensagem no seguinte formato: 
Produto: Teclado | Preço: R$ 150.00

Depois, chame a função passando um produto e um preço como argumentos.

Requisitos:

    Utilize parâmetros.
    Adicione type hints nos parâmetros.
    A função deve retornar None.
"""

def exibir_produto(nome_produto: str, preco_produto: float):
    print(f"Produto: {nome_produto} | Preço: R$ {preco_produto:.2f}")
    

exibir_produto("Teclado", 150)
exibir_produto("Monitor", 550.50)