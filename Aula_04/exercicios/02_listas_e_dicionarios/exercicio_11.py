"""
11. Atualização de Dados
Objetivo: Dada uma lista de dicionários representando produtos, 
atualizar o preço de um produto específico.
"""
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

id_ = int(input("ID: "))
preco = float(input("Novo preço: "))

produto_dict = {}
for produto in produtos:
    if produto["id"] == id_:
        produto["preço"] = preco
        break
print(produtos)
        