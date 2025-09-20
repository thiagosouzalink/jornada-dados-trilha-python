"""
Questão: Cálculo de Bônus com Entrada do Usuário

Escreva um programa em Python que solicita ao usuário para digitar seu 
nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
O programa deve, então, imprimir uma mensagem saudando o usuário pelo 
nome e informando o valor do salário em comparação com o bônus recebido.
KPI do bônus = 1000 + salario * bônus
"""
CONSTANTE_BONUS = 1000
nome = input("Digite seu nome: ")
salario_mensal = float(input("Digite ovalor do seu salário mensal: "))
percentual_bonus = float(input("Digite o valor do bônus recebido: "))

bonus = CONSTANTE_BONUS + salario_mensal * percentual_bonus

print(f"Olá {nome}, seu salário é {salario_mensal} e seu bônus é {bonus}")
 

