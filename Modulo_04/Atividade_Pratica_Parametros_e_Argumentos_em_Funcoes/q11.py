"""
Atividade Prática - Parâmetros e Argumentos em Funções

Exercício 11 - Recebendo argumentos nomeados com **kwargs


Crie uma função chamada mostrar_jogador que receba uma quantidade variável 
de argumentos nomeados utilizando **kwargs.


def mostrar_jogador(**dados):


Faça uma chamada semelhante a:

mostrar_jogador(nome="Marta", idade=40, posicao="Atacante")


Dentro da função, percorra os dados recebidos e mostre cada chave junto 
com seu respectivo valor.
"""

def mostrar_jogador(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}") 
        
        
mostrar_jogador(nome="Marta", idade=40, posicao="Atacante")