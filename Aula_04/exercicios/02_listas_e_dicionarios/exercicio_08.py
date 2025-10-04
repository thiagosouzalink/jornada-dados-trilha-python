"""
8. Ordenação Personalizada
Objetivo: Dada uma lista de dicionários representando pessoas, 
ordená-las pelo nome.
"""

pessoas = [
    {"nome": "Bob", "idade": 25},
    {"nome": "Alice", "idade": 30},
    {"nome": "Carol", "idade": 20}
]

pessoas.sort(key=lambda d: d["nome"])
print(pessoas)