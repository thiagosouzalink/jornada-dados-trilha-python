try:
    idade = int(input("Informe o valor da idade: "))
    print("Idade registrada com sucesso.")
except ValueError:
    print("Digite a idade utilizando apenas números.")