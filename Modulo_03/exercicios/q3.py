"""
Exercício 3 — Seleções Classificadas

Durante a fase de grupos, várias seleções foram sendo classificadas.

Peça ao usuário para informar o nome de 8 seleções.

Armazene essas seleções em um set.

Ao final:

Exiba todas as seleções classificadas.
Informe quantas seleções diferentes foram cadastradas.

Depois pergunte ao usuário o nome de uma seleção e informe se ela está 
classificada utilizando o operador in.

Desafio: explique por que, mesmo digitando uma seleção repetida, ela 
aparece apenas uma vez no conjunto.
"""

selecoes_classificadas = set()
for i in range(1,9):
    selecao = input(f"Digite a seleção {i}: ").strip().title()
    selecoes_classificadas.add(selecao)
    
for selecao in selecoes_classificadas:
    print(f"Seleção classificada: {selecao}")

print(f"Foram informadas {len(selecoes_classificadas)} seleções diferentes")

selecao = input("Digite o nome de uma seleção: ").strip().title()

if selecao in selecoes_classificadas:
    print(f"\n{selecao} está classificado(a)")
else:
    print(f"\n{selecao} não está classificado(a)")
    
# Sets não permitem valores duplicados, por isso apenas valores únicos serão apresentados