"""
Questão: Desafio

Escreva um programa em Python que solicita ao usuário para digitar seu 
nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
O programa deve, então, imprimir uma mensagem saudando o usuário pelo 
nome e informando o valor do salário em comparação com o bônus recebido.
KPI do bônus = 1000 + salario * bônus
"""
try:
    CONSTANTE_BONUS = 1000
    nome = input("Digite seu nome: ").strip()
    if nome.isdigit():
        raise ValueError("O valor de nome deve ser uma string.")
    if not len(nome):
        raise ValueError("O valor de nome está vazio.")
except ValueError as e:
    print(e)
else:
    try:
        salario_mensal = float(input("Digite o valor do seu salário mensal: "))
        percentual_bonus = float(input("Digite o valor do bônus recebido: "))
    except ValueError:
        print("Os valores de salário e bônus devem ser numéricos.")
    else:
        bonus = CONSTANTE_BONUS + salario_mensal * percentual_bonus
        print(f"Olá {nome}, seu salário é {salario_mensal} e seu bônus é {bonus}")