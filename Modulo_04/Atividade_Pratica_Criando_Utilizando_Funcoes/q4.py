"""
Atividade Prática - Criando e Utilizando Funções

Exercício 4 - Calculando a média de avaliações

Uma plataforma armazena três avaliações dadas por usuários para um produto.

Crie uma função chamada calcular_media_avaliacoes() que receba três notas 
e retorne a média entre elas.

Depois, utilize o resultado retornado pela função para exibir a média 
das avaliações

Requisitos:

    Utilize parâmetros e argumentos.
    Adicione type hints.
    Utilize return.
    Adicione uma docstring explicando o que a função recebe e o que retorna.
    Guarde o resultado da função em uma variável antes de exibi-lo.
"""

def calcular_media_avaliacoes(
    nota1: float, 
    nota2: float, 
    nota3: float
) -> float:
    """Função que recebe três notas e retorna a média entre as notas.

    Args:
        nota1 (float): Valor da nota 1
        nota2 (float): Valor da nota 2
        nota3 (float): Valor da nota 3

    Returns:
        float: Média das notas
    """
    return (nota1 + nota2 + nota3) / 3


media = calcular_media_avaliacoes(9, 7, 8)
print(media)
    
    