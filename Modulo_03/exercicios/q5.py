"""
Exercício 5 — Ranking de Artilheiros

Crie uma lista de dicionários para armazenar informações de jogadores.

O programa deverá perguntar quantos jogadores o usuário deseja cadastrar.

Para cada jogador, solicite:

Nome
Seleção
Quantidade de gols

Cada jogador deverá ser armazenado como um dicionário dentro da lista.

Ao final:

Exiba todos os jogadores cadastrados.
Informe qual jogador marcou mais gols.
Informe a média de gols dos jogadores cadastrados.

Desafio: utilize try/except para validar a quantidade de gols informada 
pelo usuário.
"""

informacoes_jogadores: list[dict[str, str]] = []
maximo_gols = 0
total_gols = 0
media = 0
jogador_mais_gols: list[str] = []

try:
    quantidade_jogadores = int(input("Digite quantos jogadores deseja cadastrar: "))
    
    if quantidade_jogadores > 0:  
        for i in range(0, quantidade_jogadores):
            nome = input("\nDigite o nome do jogador: ").strip().title()
            selecao = input("Digite a seleção do jogador: ").strip().title()
            quantidade_gols = int(input("Digite a quantidade de gols do jogador: "))
            informacoes_jogadores.append({
                "Nome": nome,
                "Seleção": selecao,
                "Quantidade de gols": quantidade_gols
            })
        
        print("\nJogadores cadastrados:")
        for i in range(0, len(informacoes_jogadores)):
            print(f"Jogador {i+1}:")
            for chave, valor in informacoes_jogadores[i].items():
                print(f"  - {chave}: {valor}")
            
            # Verificar a quantiade máxima de gols marcados
            if informacoes_jogadores[i]["Quantidade de gols"] > maximo_gols:
                maximo_gols = informacoes_jogadores[i]["Quantidade de gols"]
            
            total_gols += informacoes_jogadores[i]["Quantidade de gols"]
            
        for dict_jogador in informacoes_jogadores:
            if dict_jogador["Quantidade de gols"] == maximo_gols:
                jogador_mais_gols.append(dict_jogador["Nome"])
                
        print(f"\njogador(es) com mais gols: {','.join(jogador_mais_gols)} ({maximo_gols})")
        print(f"Média de gols: {total_gols/len(informacoes_jogadores):.2f}")
                
    else:
        print("Não foi cadastrado nenhum jogador")
except ValueError:
    print("Quantidade de jogadores ou número de gols deve ser um número inteiro.")