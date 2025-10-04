# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário 
# {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total 
# da lista de compras.

# frutas = ["maçã", "banana", "cereja"] 
frutas = ["banana", "cereja", "maçã", "cereja", "banana", 
          "banana", "cereja", "cereja", "cereja", "maçã"]
frutas_precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

preco_total = 0
for fruta in frutas:
    preco_total += frutas_precos[fruta]
print(f"Preço total: {preco_total}")