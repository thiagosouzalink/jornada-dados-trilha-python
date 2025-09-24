# 17. Crie um programa que receba dois valores booleanos do usuário e 
# retorne o resultado da operação OR.
valor1 = bool(int(input("Digite um valor booleano (True 1, False 0): ")))
valor2 = bool(int(input("Digite outro valor booleano (True 1, False 0): ")))
resultado = valor1 or valor2
print(f"Operacao OR: {resultado}")