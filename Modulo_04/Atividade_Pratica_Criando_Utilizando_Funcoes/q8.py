"""
Atividade Prática - Criando e Utilizando Funções

Exercício 8 - Verificando uma meta de vendas

Crie uma função chamada calcular_percentual_meta() que receba:

    valor da meta;
    valor vendido.


A função deve calcular e retornar o percentual da meta que foi atingido.

Exemplo: percentual = calcular_percentual_meta(10000.0, 7500.0)
Resultado: 75.0

Depois, crie uma função chamada exibir_status_meta() que receba esse 
percentual.

Ela deve exibir: Meta atingida!
caso o percentual seja maior ou igual a 100.

Caso contrário, deve exibir: Meta ainda não atingida.

Requisitos:

    Utilize type hints.
    calcular_percentual_meta() deve retornar float.
    exibir_status_meta() deve retornar None.
    Utilize o valor retornado por uma função como argumento da outra.
    Adicione docstrings nas duas funções.
    Não repita o cálculo do percentual fora da função.
"""

def calcular_percentual_meta(
    valor_meta: float, 
    valor_vendido: float
) -> float:
    """Função que calcula o percentual atingido do valor vendido em relação
    a meta.

    Args:
        valor_meta (float): Valor da meta;
        valor_vendido (float): Valor vendido.

    Returns:
        float: Percentual em relaçao a meta.
    """
    percentual = (valor_vendido / valor_meta) * 100
    return percentual


def exibir_status_meta(percentual_meta: float):
    """Função que exibi o status de percentual da venda em relação a meta

    Args:
        percentual_meta (float): Percentual calculado da meta.
    """
    if percentual_meta >= 100:
        print("Meta atingida!")
    else:
        print("Meta ainda não atingida.")
        
        
percentual = calcular_percentual_meta(10000.0, 7500.0)
exibir_status_meta(percentual)