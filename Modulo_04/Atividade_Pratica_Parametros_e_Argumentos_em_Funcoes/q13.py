"""
Atividade Prática - Parâmetros e Argumentos em Funções

Exercício 13 -  *args e **kwargs juntos

Crie uma função chamada:

registrar_partida(time_a, time_b, *eventos, **informacoes):

Os dois primeiros argumentos devem representar os times da partida.


Os argumentos posicionais extras devem representar eventos ocorridos 
durante o jogo.

Os argumentos nomeados extras devem representar outras informações sobre 
a partida.


Exemplo:

registrar_partida(
"Brasil",
"Argentina",
"Gol do Brasil",
"Cartão amarelo",
"Gol da Argentina",
estadio="Maracanã",
publico=70000
):


A função deve mostrar:

    Os dois times.
    Todos os eventos recebidos.
    Todas as informações adicionais.
"""

def registrar_partida(time_a, time_b, *eventos, **informacoes):
    print(f"Partida: {time_a} x {time_b}")
    print(" -> Eventos:")
    for evento in eventos:
        print(f"     - {evento}")
    print(f" -> Informações Adicionais:")
    for chave, valor in informacoes.items():
        print(f"     - {chave}: {valor}")
        

registrar_partida(
    "Brasil",
    "Argentina",
    "Gol do Brasil",
    "Cartão amarelo",
    "Gol da Argentina",
    estadio="Maracanã",
    publico=70000
)