"""
Atividade Prática - Criando e Utilizando Funções

Exercício 5 - Processando um pedido

Você precisa criar duas funções para representar uma pequena parte de um 
sistema de pedidos.

A primeira função deve se chamar: calcular_valor_final()

Ela deve receber:

    preço unitário;
    quantidade;
    desconto em formato decimal.

Por exemplo, 0.10 representa 10% de desconto.

A função deve calcular e retornar o valor final do pedido após o desconto.

Depois, crie uma segunda função chamada: exibir_resumo_pedido()

Ela deve receber:

    número do pedido;
    valor final.


E exibir uma mensagem como: Pedido #1025 finalizado. Total: R$ 270.00

Requisitos:

    As duas funções devem possuir type hints.
    calcular_valor_final() deve retornar um float.
    exibir_resumo_pedido() deve retornar None.
    As duas funções devem possuir docstrings.
    O valor retornado por calcular_valor_final() deve ser passado como 
    argumento para exibir_resumo_pedido().
    Não faça o cálculo diretamente fora da função.
"""

def calcular_valor_final(
    preco_unitario: float, 
    quantidade: int, 
    desconto: float
) -> float:
    """Função que calcula valor final descontado do produto.

    Args:
        preco_unitario (float): Valor do preço unitário do produto.
        quantidade (int): Quantidade de produtos vendidos.
        desconto (float): Valor de desconto em forma decimal.

    Returns:
        float: Valor final do produto descontado.
    """
    preco = preco_unitario * quantidade
    valor_final = preco * (1-desconto)
    return valor_final

def exibir_resumo_pedido(numero_pedido: int, valor_final: float) -> None:
    """Exibi o resumo do pedido, com seu número e valor final.

    Args:
        numero_pedido (int): Núemro do pedido.
        valor_final (float): Valor final do produto.
    """
    print(f"Pedido #{numero_pedido} finalizado. Total: R$ {valor_final:.2f}")
    
    
valor = calcular_valor_final(7.50, 4, 0.1)
numero_pedido: int = 12345
exibir_resumo_pedido(numero_pedido, valor)
    
    
