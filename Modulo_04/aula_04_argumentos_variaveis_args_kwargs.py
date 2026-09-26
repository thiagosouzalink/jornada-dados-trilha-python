"""
Aula 4 - Argumentos Variáveis com *args e **kwargs
"""

# *args
def calcular_total_modo_raiz(
    valor1: float,
    valor2: float,
    valor3: float
) -> float:
    return valor1 + valor2 + valor3

total = calcular_total_modo_raiz(89.90, 200.0, 510.0)
# print(total)

def calcular_total(*valores: float) -> float:
    # print(valores)
    return sum(valores)

total2 = calcular_total(89.90, 200.0, 510.0, 731.21, 922.2)
# print(total2)

def mostrar_produtos(*produtos: str) -> None:
    print(produtos)

# mostrar_produtos("Teclado", "Fone de Ouvido", "Mouse")

def calcular_total_pedido(*valores: float) -> float:
    # total = 0
    # print(valores)
    # for valor in valores:
    #     total += valor
        
    return sum(valores)

total3 = calcular_total_pedido(
    120.0,
    89.90,
    45.50,
    199.90,
    491.34
)

# print(f"Total do pedido: R${total:.2f}")


# Parâmetros Normais + *args
def registrar_pedido(
    numero_pedido: int,
    *produtos: str
) -> None:
    print(f"Pedido #{numero_pedido}")
    
    for produto in produtos:
        print(f"- {produto}")
        
# registrar_pedido(
#     1025,
#     "Notebook",
#     "Mouse",
#     "Fone de ouvido"
# )


# **kwargs
def cadastrar_cliente(**dados) -> None:
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    
# cadastrar_cliente(
#     nome="Thiago",
#     email="thiago@ehlegal.com",
#     cidade="Belém"
# )

# Parâmetros normais + **kwargs
def cadastrar_cliente2(
    nome: str,
    email: str,
    **dados_adicionais
) -> None:
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    
    for k, v in dados_adicionais.items():
        print(f"{k.capitalize()}: {v.capitalize()}")
        
# cadastrar_cliente2(
#     nome="Luiza",
#     email="luiza@élegal.com",
#     cidade="Recife",
#     estado="Pernambuco",
#     profissao="Engenheira de Dados"
# )


# *args e **kwargs juntos
def registrar_venda(
    cliente: str,
    *produtos: str,
    **dados_adicionais
) -> None:
    print(f"Cliente: {cliente}")
    
    print("\nProdutos")
    for produto in produtos:
        print(f"- {produto.capitalize()}")
        
    print("\nInformações da Venda")
    for k, v in dados_adicionais.items():
        print(f"{k.capitalize()}: {v}")
        
registrar_venda(
    "Thiago",
    "Notebook",
    "Telefone",
    "Mouse",
    forma_pagamento="pix",
    vendedor="João",
    entrega=True
)