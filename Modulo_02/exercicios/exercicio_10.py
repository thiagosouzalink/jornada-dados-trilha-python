continuar = True

while continuar:
    try:
        gols = int(input("Quantos gols a seleção marcou? "))
        
        if gols < 0:
            print("A quantidade de gols não pode ser negativa.\n")
        else:
            print(f"Quantidade de gols registrada: {gols}")
            continuar = False
    except ValueError:
        print("Entrada inválida.\n")
        