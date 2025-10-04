"""
13. Filtragem de Dados em Dicionário
Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com 
quantidade maior que 0.
"""
estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_maior_que_zero = {
    produto: quantidade 
    for produto, quantidade in estoque.items() 
    if quantidade > 0
}
print(estoque_maior_que_zero)