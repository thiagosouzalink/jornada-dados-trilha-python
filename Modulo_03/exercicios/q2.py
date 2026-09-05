"""
Exercício 2 — Estatísticas da Partida

Crie um programa que solicite ao usuário as seguintes informações de uma 
partida:

Seleção mandante
Seleção visitante
Gols da seleção mandante
Gols da seleção visitante

Armazene essas informações em um dicionário.

Depois:

Exiba todas as informações utilizando um for com .items().
Informe qual seleção venceu a partida.
Caso os gols sejam iguais, informe que a partida terminou empatada.

Desafio: utilize try/except para garantir que a quantidade de gols seja 
um número inteiro válido.
"""

try:
    selecao_mandante = input("Digite a seleção mandante: ").strip().title()
    selecao_visitante = input("Digite a seleção visitante: ").strip().title()
    
    gols_selecao_mandante = int(input("Digite a quantidade de gols da seleção mandante: "))
    gols_selecao_visitante = int(input("Digite a quantidade de gols da seleção visitante: "))
    
    informacoes_partida = {
        "seleção mandante": selecao_mandante,
        "seleção visitante": selecao_visitante,
        "gols seleção mandante": gols_selecao_mandante,
        "gols seleção visitante": gols_selecao_visitante
    }
    
    for chave, valor in informacoes_partida.items():
        print(f"{chave.title()}: {valor}")

    if informacoes_partida["gols seleção mandante"] > informacoes_partida["gols seleção visitante"]:
        print(f"\n{informacoes_partida['seleção mandante']} venceu a partida")
    elif informacoes_partida["gols seleção visitante"] > informacoes_partida["gols seleção mandante"]:
        print(f"\n{informacoes_partida['seleção visitante']} venceu a partida")
    else:
        print("\nPartida terminou empatada")
except ValueError:
    print("A quantidade de gols deve ser um número inteiro")