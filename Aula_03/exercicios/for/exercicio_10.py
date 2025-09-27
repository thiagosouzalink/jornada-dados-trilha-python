"""
10. Agregação de Dados por Categoria
Objetivo: Dado um conjunto de registros de vendas, calcular o total de 
vendas por categoria.
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]
"""
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_vendas_categoria = {}
for venda in vendas:
    if venda["categoria"] not in total_vendas_categoria:
        total_vendas_categoria[venda["categoria"]] = venda["valor"]
    else:
        total_vendas_categoria[venda["categoria"]] += venda["valor"]
print(total_vendas_categoria)