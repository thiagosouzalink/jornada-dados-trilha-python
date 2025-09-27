"""
Questão: Desafio

Escreva um programa em Python que solicita ao usuário para digitar seu 
nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
O programa deve, então, imprimir uma mensagem saudando o usuário pelo 
nome e informando o valor do salário em comparação com o bônus recebido.
KPI do bônus = 1000 + salario * bônus

Integre na solução anterior um fluxo de While que repita o fluxo até que 
o usuário insira as informações corretas
"""
CONSTANTE_BONUS = 1000

while True:
    try:
        nome = input("Digite seu nome: ").strip()
        if not len(nome):
            raise ValueError("O valor de nome está vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
    except ValueError as e:
        print(e)
        print("Tente novamente...\n")
    else:
        break

while True:
    try:
        try:
            salario_mensal = float(input("Digite o valor do seu salário mensal: "))
        except ValueError:
            raise ValueError("O valor de salário deve ser numérico.")
        if salario_mensal < 0:
            raise ValueError("O valor de salário não deve ser negativo.")
    except ValueError as e:
        print(e)
        print("Tente novamente...\n")
    else:
        break
    
while True:
    try:
        try:
            percentual_bonus = float(input("Digite o valor do bônus recebido: "))
        except ValueError:
            raise ValueError("O valor de bônus deve ser numérico.")
        if percentual_bonus < 0:
            raise ValueError("Valor de bônus não deve ser negativo.")
    except ValueError as e:
        print(e)
        print("Tente novamente...\n")
    else:
        break
    

bonus = CONSTANTE_BONUS + salario_mensal * percentual_bonus
print(f"Olá {nome}, seu salário é {salario_mensal} e seu bônus é {bonus}")