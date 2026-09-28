"""
Atividade Prática - Parâmetros e Argumentos em Funções

Exercício 3 - Argumentos nomeados

Crie uma função chamada cadastrar_jogador que receba:

    nome
    idade
    posicao


Faça a chamada utilizando argumentos nomeados e passe os valores em uma 
ordem diferente da definida na função.


Exemplo:
cadastrar_jogador(posicao="Goleiro", nome="Alisson", idade=33)
"""

def cadastrar_jogador(nome: str, idade: int, posicao: str):
    print(f"Jogador: {nome} | Idade: {idade} | Posição: {posicao}")
    
    
cadastrar_jogador(posicao="Goleiro", nome="Alisson", idade=33)