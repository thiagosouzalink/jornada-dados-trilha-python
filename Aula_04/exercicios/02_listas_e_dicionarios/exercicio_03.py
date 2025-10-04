# 3. Crie um dicionário para armazenar informações de um livro, incluindo 
# título, autor e ano de publicação. Imprima cada informação.

livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano de publicacao": 1899
}

for chave, valor in livro.items():
    print(f"{chave.title()}: {valor}")