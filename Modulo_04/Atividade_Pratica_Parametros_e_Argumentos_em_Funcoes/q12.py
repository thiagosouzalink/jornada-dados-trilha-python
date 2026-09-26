"""
Atividade Prática - Parâmetros e Argumentos em Funções

Exercício 12 - Parâmetro normal e **kwargs


Crie uma função chamada:

cadastrar_time(nome, **informacoes)

O nome do time deve ser obrigatório.


As demais informações podem variar de uma chamada para outra.


Exemplo:

cadastrar_time("Brasil", tecnico="Carlo Ancelotti", continente="América do Sul" ,titulos=5)


A função deve mostrar o nome do time e depois todas as informações 
adicionais recebidas.
"""

def cadastrar_time(nome, **informacoes):
    print(f"Time: {nome}")
    for chave, valor in informacoes.items():
        print(f" - {chave}: {valor}")
        
        
cadastrar_time("Brasil", tecnico="Carlo Ancelotti", continente="América do Sul" ,titulos=5)