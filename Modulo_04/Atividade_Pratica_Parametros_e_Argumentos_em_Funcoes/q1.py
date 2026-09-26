"""
Atividade Prática - Parâmetros e Argumentos em Funções

Exercício 1 - Argumentos posicionais

Crie uma função chamada apresentar_jogador que receba:

    nome
    posicao

A função deve exibir uma mensagem semelhante a:

Jogador: Marta | Posição: Atacante

Faça a chamada da função passando os dois argumentos por posição.


Exemplo:

apresentar_jogador("Marta", "Atacante")
"""

def apresentar_jogador(nome: str, posicao: str):
    print(f"Jogador: {nome} | Posição: {posicao}")
    
    
apresentar_jogador("Marta", "Atacante")
apresentar_jogador("Marquinhos", "Zagueiro")