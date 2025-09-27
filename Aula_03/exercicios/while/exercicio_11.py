"""
11. Leitura de Dados até Flag
Objetivo: Ler dados de entrada até que uma palavra-chave específica 
("sair") seja fornecida.
"""
while True:
    entrada = input("Entrada ('sair' para encerrar): ").strip()
    if entrada.lower() == "sair":
        break
    