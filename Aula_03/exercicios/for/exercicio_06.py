"""
6. Contagem de Palavras em Textos
Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
"""
texto = input("Texto: ").strip()
palavras = texto.lower().split()

dicionario_palavras = {}
for palavra in palavras:
    if palavra in dicionario_palavras:
        dicionario_palavras[palavra] += 1
    else:
        dicionario_palavras[palavra] = 1
print("\n\nImprimindo cada palavra e sua quantidade de ocorrências:")
for palavra, quantidade in dicionario_palavras.items():
    print(f"Palavra: {palavra}\tQuantidade: {quantidade}")