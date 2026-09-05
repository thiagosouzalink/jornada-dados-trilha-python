"""
Exercício 1 — Cadastro de Figurinhas

Você foi contratado para desenvolver um sistema simples para controlar 
um álbum de figurinhas da Copa do Mundo.

O programa deve permitir que o usuário cadastre figurinhas até que ele 
digite a palavra "fim".

Ao final, exiba:

Todas as figurinhas cadastradas.
A quantidade total de figurinhas.
A primeira figurinha cadastrada.
A última figurinha cadastrada.

Desafio: não permita que o usuário cadastre uma figurinha vazia.
"""

continuar_cadastro: bool = True
album_figurinhas: list[str] = []

while continuar_cadastro:
    nome_figurinha = input("Digite o nome da figurinha | [fim] para finalizar: ").strip()
    
    if nome_figurinha == "":
        print("Não é permitido o cadastro de uma figurinha vazia.")
    elif nome_figurinha.lower() == "fim":
        continuar_cadastro = False
    else:
        album_figurinhas.append(nome_figurinha)

print("\nAs figurinhas cadastradas foram:")
for figurinha in album_figurinhas:
    print(f"- {figurinha.title()}")

print(f"\nQuantidade de figurinhas: {len(album_figurinhas)}")
print(f"A primeira figurinha cadastrada foi: {album_figurinhas[0].title()}")
print(f"A última figurinha cadastrada foi: {album_figurinhas[-1].title()}")