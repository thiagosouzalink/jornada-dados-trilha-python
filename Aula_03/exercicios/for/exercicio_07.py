"""
7. Normalização de Dados
Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.

Valor Normalizado = (Valor Original - Valor Mínimo) / (Valor Máximo - Valor Mínimo)
"""
valores = [2, 32, 40, 5, 8, 9, 32, 6, 21, 60, 48, 8, 30, 21, 27]
valor_minimo = min(valores)
valor_maximo = max(valores)

valores_normalizados = []
for valor in valores:
    valor_normalizado = (valor - valor_minimo) / (valor_maximo - valor_minimo)
    valores_normalizados.append(round(valor_normalizado, 4))
    
print(f"Valores: {valores}")
print(f"Valores Normalizados: {valores_normalizados}")
    