# Exercício será tipar o desafio da aula 03

CONSTANTE_BONUS: int = 1000

while True:
    try:
        nome: str = input("Digite seu nome: ").strip()
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
            salario_mensal: float = float(
                input("Digite o valor do seu salário mensal: ")
            )
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
            percentual_bonus: float = float(
                input("Digite o valor do bônus recebido: ")
            )
        except ValueError:
            raise ValueError("O valor de bônus deve ser numérico.")
        if percentual_bonus < 0:
            raise ValueError("Valor de bônus não deve ser negativo.")
    except ValueError as e:
        print(e)
        print("Tente novamente...\n")
    else:
        break
    

bonus: float = CONSTANTE_BONUS + salario_mensal * percentual_bonus
print(f"Olá {nome}, seu salário é {salario_mensal} e seu bônus é {bonus}")