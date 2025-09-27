"""
15. Processamento de Dados com Condição de Parada
Objetivo: Processar itens de uma lista até encontrar um valor específico 
que indica a parada.
"""
itens = ["Monitor", "Teclado", "Mouse", "break", "Cooler"]
parada = "break"
contador = 0

while True:
    item = itens[contador]
    if item.lower() == parada:
        break
    print(f"Item Processado: {item}")
    contador += 1
print("Processamento concluído.")