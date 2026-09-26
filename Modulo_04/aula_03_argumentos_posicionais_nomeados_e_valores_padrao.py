"""
Aula 3 - Argumentos Posicionais, Nomeados e Valores Padrão
"""

def cadastrar_produto(
    nome:str,
    preco: float,
    estoque: int
) -> None:
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque} unidades")
    
    
def cadastrar_produto2(
    nome:str,
    preco: float,
    estoque: int,
    ativo: bool = True
) -> None:
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque} unidades")
    print(f"Ativo: {ativo}")

# Argumento Posicional
cadastrar_produto(
    "Mouse",      
    200.50, 
    50    
)

# Argumetos Nomeados
cadastrar_produto(
    preco=200.50,
    estoque=50,
    nome="Mouse"
)

cadastrar_produto2("Mouse", 200.50, 50)