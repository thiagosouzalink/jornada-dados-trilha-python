"""
Atividade Prática - Parâmetros e Argumentos em Funções

Exercício 4 - Posicionais e nomeados juntos

Crie uma função chamada registrar_gol que receba:

    jogador
    time
    minuto


Na chamada da função:

    Passe jogador por posição.
    Passe time por posição.
    Passe minuto pelo nome.


A função deve exibir uma mensagem semelhante a:

Vini Jr marcou para o Brasil aos 34 minutos.
"""

def registrar_gol(jogador: str, time: str, minuto: int):
    print(f"{jogador} marcou para o {time} aos {minuto} minutos.")
    

registrar_gol("Vini Jr", "Brasil", minuto=34)