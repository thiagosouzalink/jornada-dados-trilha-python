# 16. Escreva um programa que avalie duas expressões booleanas inseridas 
# pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = bool(int(input("Digite um valor booleano (True 1, False 0): ")))
valor2 = bool(int(input("Digite outro valor booleano (True 1, False 0): ")))
resultado = valor1 and valor2
print(f"Operacao AND: {resultado}")