"""
Exercício 23: Calculadora Simples
Desenvolva uma calculadora simples que aceite duas entradas numéricas e 
um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões 
por zero e entradas não numéricas. Utilize if-elif-else para realizar a 
operação matemática baseada no operador fornecido. Imprima o resultado 
ou uma mensagem de erro apropriada.
"""
try:
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    operacao = input("Digite a operacao (+, -, *, /): ")
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else: 
        raise TypeError("Voce digitou uma operacao invalida.")
    print(f"{num1} {operacao} {num2} = {resultado:.2f}")
except ValueError:
    print("Os valores precisam ser numericos.")
except ZeroDivisionError:
    print("Não é possível dividir por zero")
except TypeError as e:
    print(e)