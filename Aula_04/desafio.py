"""
Questão: Desafio

Escreva um programa em Python que solicita ao usuário para digitar seu 
nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
O programa deve, então, imprimir uma mensagem saudando o usuário pelo 
nome e informando o valor do salário em comparação com o bônus recebido.
KPI do bônus = 1000 + salario * bônus

Refatorar nosso código usando Dicionário, Type Hint e Funcões.
"""
CONSTANTE_BONUS = 1000

def obter_nome(texto_entrada: str) -> str:
    while True:
        try:
            nome = input(texto_entrada).strip()
            if not len(nome):
                raise ValueError("O valor de nome está vazio.")
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
        except ValueError as e:
            print(e)
            print("Tente novamente...\n")
        else:
            return nome    

def obter_salario_mensal(texto_entrada: str) -> float:
    while True:
        try:
            try:
                salario_mensal = float(input(texto_entrada))
            except ValueError:
                raise ValueError("O valor de salário deve ser numérico.")
            if salario_mensal < 0:
                raise ValueError("O valor de salário não deve ser negativo.")
        except ValueError as e:
            print(e)
            print("Tente novamente...\n")
        else:
            return salario_mensal
        
def obter_percentual_bonus(texto_entrada: str) -> float:
    while True:
        try:
            try:
                percentual_bonus = float(input(texto_entrada))
            except ValueError:
                raise ValueError("O valor de bônus deve ser numérico.")
            if percentual_bonus < 0:
                raise ValueError("Valor de bônus não deve ser negativo.")
        except ValueError as e:
            print(e)
            print("Tente novamente...\n")
        else:
            return percentual_bonus
        
def calcular_bonus(constante_bonus: int|float, 
                   salario_mensal: float, 
                   percentual_bonus: float) -> float:
    bonus = constante_bonus + salario_mensal * percentual_bonus
    return bonus

def verificar_saida() -> bool:
    while True:
        try:
            saida = input("Deseja sair (sim/não): ").strip()
            if saida.lower() not in ("sim", "nao", "não"):
                raise ValueError("O valor de saída deve ser 'sim' ou 'não': ")
        except ValueError as e:
            print(e)
            print("Tente novamente...\n")
        else:
            if saida == "sim":
                return True
            return False

lista_dados = []
while True:
    dict_dados = {}
    dict_dados["nome"] = obter_nome("Digite seu nome: ")
    dict_dados["salario_mensal"] = obter_salario_mensal("Digite o valor do seu salário mensal: ")
    dict_dados["percentual_bonus"] = obter_percentual_bonus("Digite o valor do bônus recebido: ")
    dict_dados["bonus"] = calcular_bonus(
        CONSTANTE_BONUS, 
        dict_dados["salario_mensal"], 
        dict_dados["percentual_bonus"]
    )
    lista_dados.append(dict_dados)
    if verificar_saida():
        break

print("\n\n######### Dados #######")
for dados in lista_dados:
    print(f"Nome: {dados['nome']}")
    print(f"Salário Mensal: {dados['salario_mensal']}")
    print(f"Percentual Bônus: {dados['percentual_bonus']*100}%")
    print(f"Bônus: {dados['bonus']}\n")
    