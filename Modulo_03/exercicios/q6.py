"""
Exercício 6 - Desafio Final — Sistema da Copa do Mundo

Desenvolva um programa para cadastrar partidas da Copa do Mundo.

O programa deverá permanecer em execução até que o usuário decida encerrá-lo.

Para cada partida, solicite:

Seleção mandante
Seleção visitante
Gols da seleção mandante
Gols da seleção visitante

Cada partida deverá ser armazenada em um dicionário, e todos os 
dicionários deverão ser armazenados em uma lista.

Ao finalizar o cadastro, exiba:

A quantidade de partidas cadastradas.
Todas as partidas registradas.
Quantas partidas terminaram empatadas.
A partida com o maior número total de gols.
A média de gols por partida.

Requisitos:

Utilize listas e dicionários.
Utilize while para controlar o cadastro.
Utilize for para percorrer as partidas.
Utilize if, elif e else para identificar o resultado de cada jogo.
Utilize try/except para validar os gols informados.
Utilize len() para calcular a quantidade de partidas cadastradas.
"""

partidas: list[dict[str, str|int]] = []

continuar: bool = True
quantidade_empates: int = 0
total_gols: int = 0
maior_numero_gols: int = 0
partidas_maior_numero_gols: list[str] = []

try:
    while continuar:
        selecao_mandante = input("Digite a seleção mandante: ").strip().title()
        selecao_visitante = input("Digite a seleção visitante: ").strip().title()
        gols_selecao_mandante = int(input("Digite o número de gols da seleção mandante: "))
        gols_selecao_visitante = int(input("Digite o número de gols da seleção visitante: "))
        while gols_selecao_mandante < 0 or gols_selecao_mandante < 0:
            print("O número de gols deve ser positivo.")
            gols_selecao_mandante = int(input("Digite o número de gols da seleção mandante: "))
            gols_selecao_visitante = int(input("Digite o número de gols da seleção visitante: "))
        
        
        partidas.append(
            {"Seleção mandante": selecao_mandante,
             "Seleção visitante": selecao_visitante,
             "Gols da seleção mandante": gols_selecao_mandante,
             "Gols da seleção visitante": gols_selecao_visitante}
        )
        
        opcao_continuar = input("Deseja continuar cadastrando? [não] para sair e qualquer outra tecla para continuar: ").strip().lower()
        if opcao_continuar in ["não", "nao"]:
            continuar = False
    
    # A quantidade de partidas cadastradas.
    total_partidas_cadastradas = len(partidas)
    print(f"\nTotal de partidas cadastradas: {total_partidas_cadastradas}")
    
    for i in range(0, len(partidas)):
        # Todas as partidas registradas.
        print(f"partida {i+1}: {partidas[i]['Seleção mandante']} x {partidas[i]['Seleção visitante']}")
        for chave, valor in partidas[i].items():
            print(f"  - {chave}: {valor}")
        
        # Obter número de partidas empatadas.
        if partidas[i]["Gols da seleção mandante"] == partidas[i]["Gols da seleção visitante"]:
            quantidade_empates += 1
        
        # Obter partida(s) com maior número de gols
        gols_partida = partidas[i]["Gols da seleção mandante"] + partidas[i]["Gols da seleção visitante"]
        if gols_partida > maior_numero_gols:
            maior_numero_gols = gols_partida
        
        # Obter o total de gols
        total_gols += gols_partida
    
    # Quantas partidas terminaram empatadas.
    print(f"Total de empates: {quantidade_empates}")

    # A partida com o maior número total de gols.
    for partida in partidas:
        qtd_gols = partida["Gols da seleção mandante"] + partida["Gols da seleção visitante"]
        if qtd_gols == maior_numero_gols:
            confronto = f"{partida['Seleção mandante']} x {partida['Seleção visitante']}"
            partidas_maior_numero_gols.append(confronto)
    print(f"Partida(s) com maior número de gols: {', '.join(partidas_maior_numero_gols)}")
    
    # A média de gols por partida.
    media_gols = total_gols / total_partidas_cadastradas
    print(f"Média de gols por partida: {media_gols:.2f}")
    
except ValueError:
    print("A quantidade de gols deve ser um número inteiro")
    