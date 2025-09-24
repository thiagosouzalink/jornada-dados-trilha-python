"""
Exercício 24: Classificador de Números
Escreva um programa que solicite ao usuário para digitar um número. 
Utilize try-except para assegurar que a entrada seja numérica e utilize 
if-elif-else para classificar o número como "positivo", "negativo" ou 
"zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
"""
try:
    numero = int(input("Digite um valor inteiro: "))
    if numero > 0:
        resultado1 = "positivo"
    elif numero < 0:
        resultado1 = "negativo"
    else:
        resultado1 = "zero"
    if numero % 2 == 0:
        resultado2 = "par"
    else: 
        resultado2 = "impar"
    print(f"O valor {numero} é {resultado1} e {resultado2}")
except ValueError:
    print("O valor precisa ser um numero inteiro.")
