"""
Atividade Prática - Unpacking e Controle de Argumentos

Exercício 16 - Unpacking com ** e argumentos nomeados


Considere o seguinte dicionário:

jogador = {"nome": "Marta","idade": 40,"posicao": "Atacante"}


Crie uma função chamada apresentar_jogador que receba:

    nome
    idade
    posicao


A função deve:

    Utilizar type hints em todos os parâmetros.
    Indicar através do type hint que a função não retorna nenhum valor.
    Possuir uma docstring.
    Exibir uma mensagem com os dados do jogador.


Chame a função desempacotando o dicionário com **.

Você não deve acessar manualmente:

jogador["nome"]
jogador["idade"]
jogador["posicao"]


Depois, responda em um comentário no código:

Por que as chaves do dicionário precisam possuir os mesmos nomes dos 
parâmetros da função?
"""

def apresentar_jogador(nome: str, idade: int, posicao: str) -> None:
    """Função que exibe informaçóes de um determinado jogador.
    
    Args:
        nome (str): Nome do jogador.
        idade (int): Idade do jogador.
        posicao (str): Posição do jogador.
    """
    print(f"Nome: {nome} | Idade: {idade} | Posição: {posicao}")
    
    
jogador = {"nome": "Marta","idade": 40,"posicao": "Atacante"}
apresentar_jogador(**jogador)

# O desempacotamento utilizando ** desempacota usando as chaves e valores do dicionários como argumentos nomeados.