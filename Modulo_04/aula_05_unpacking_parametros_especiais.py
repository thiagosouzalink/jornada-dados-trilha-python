"""
Aula 5 - Unpacking e Parâmetros Especiais
"""

# Unpacking (desempacotar) com *
def cadastrar_produto(
    nome: str,
    preco: float,
    estoque: int = 0
) -> None:
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque}")
    
    
# cadastrar_produto("Fone de Ouvido", 300.0, estoque=50)
produto = ["Teclado", 4500.0, 120]
produto2 = ("Notebook", 5000.0, 3)
# cadastrar_produto(
#     produto[0],
#     produto[1],
#     produto[2]
# )
# cadastrar_produto(*produto)
# cadastrar_produto(*produto2)


# Unpacking (desempacotar) com **
# cadastrar_produto(
#     nome="Mouse",
#     preco=300.0,
#     estoque=8
# )
produto3 = {
    "nome": "Mouse",
    "preco": 300.0,
    "estoque": 8
}
cadastrar_produto(**produto3)


# / - Parâmetros somente POSICIONAIS (tudo a esquerda)
def calcular_desconto(
    preco: float,
    desconto: float,
    / # Tudo que aparece antes da / deve ser passado como um argumento posicional
) -> float:
    return preco - (preco * desconto)

calcular_desconto(500, 0.10)
#calcular_desconto(preco=500, desconto=0.10)
#calcular_desconto(500, desconto=0.10)


def registrar_venda2(
    codigo: int,
    /,
    cliente: str
) -> None:
    print(codigo)
    print(cliente)
    
registrar_venda2(500, "Thiago")
registrar_venda2(500, cliente="Thiago")
# registrar_venda2(codigo=500, cliente="Thiago")


# * - Parâmetros somentos NOMEADOS (tudo a direita)
def exportar_relatorio(
    nome_arq: str,
    *,
    incluir_cabecalho: bool,
    compactar: bool
) -> None:
    print(nome_arq)
    print(incluir_cabecalho)
    print(compactar)
    
exportar_relatorio(
    "vendas.csv", 
    incluir_cabecalho=True, 
    compactar=True
)


# / e * juntos
def processar_pagamento(
    numero_pedido: int, # ARG. POSICIONAL
    valor: float,       # ARG. POSICIONAL
    /, # / -> separador que indica que tudo a esquerda deve ser passado como um argumento POSICIONAL
    forma_pagamento: str, # ARG. TANTO PODE SER POSICIONAL QUANTO NOMEADO
    *, # * -> separador que indica que tudo a direita deve ser passado como um argumento NOMEADO
    enviar_comprovante: bool = True # ARG. NOMEADO
) -> None:
    print(f"Pedido: {numero_pedido}")
    print(f"Valor: R$ {valor:.2f}")
    print(f"Pagamento: {forma_pagamento}")
    print(f"Enviar comprovante: {enviar_comprovante}")
    
# processar_pagamento(
#     1050,
#     500,
#     "Pix",
#     enviar_comprovante=True
# )


def funcao(
    a, # ARG. POSICIONAL
    b, # ARG. POSICIONAL
    /, # SEPARADOR (TUDO A ESQUERDA É UM ARGUMENTO OBRIGATÓRIAMENTE POSICIONAL)
    c, # RECEBE ARG. POSICIONAL OU NOMEADO
    d, # RECEBE ARG. POSICIONAL OU NOMEADO
    *args, # RECEBE ARG. POSICIONAL EXTRA (EMPACOTA NUMA TUPLA)
    e, # COMO O *ARGS JÁ CAPTURA OS ARGUMENTOS POSICIONAIS QUE SOBRAREM, O PARÂMETRO e E f FICA SENDO OBRIGATORIAMENTE COMO ARGUMENTOS NOMEADODS
    f,
    **kwargs # NOMEADOS RESTANTES (QUE VAO SER EMPACOTADOS COMO UM DICIONÁRIO)
):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print("args:", args)
    print("e:", e)
    print("f:", f)
    print("kwargs:", kwargs)


funcao(
    1,
    2,
    3,
    4,
    5,
    6,
    e=7,
    f=8,
    nome="Thiago",
    idade=37
)