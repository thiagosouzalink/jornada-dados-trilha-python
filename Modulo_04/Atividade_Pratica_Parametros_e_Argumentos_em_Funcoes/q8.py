"""
Atividade Prática - Parâmetros e Argumentos em Funções

Exercício 8 - Recebendo vários argumentos com *args


Crie uma função chamada listar_jogadores que receba uma quantidade 
variável de nomes utilizando *args.


def listar_jogadores(*jogadores):


A função deve percorrer os jogadores recebidos e exibir cada nome.


Teste a função com diferentes quantidades de argumentos:

listar_jogadores("Marta")listar_jogadores("Marta","Vini Jr","Alisson")
"""

def listar_jogadores(*jogadores):
    for jogador in jogadores:
        print(f"Jogador(a): {jogador}")
    print()
    
    
listar_jogadores("Marta")
listar_jogadores("Marta","Vini Jr","Alisson")