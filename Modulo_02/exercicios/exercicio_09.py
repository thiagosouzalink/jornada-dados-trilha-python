try:
    nota = float(input("Digite a nota: "))
    
    if 0 <= nota <= 10:
        print(f"Nota registrada: {nota}")
    else:
        print("A nota deve estar entre 0 e 10.")
except ValueError:
    print("Valor inválido. Digite um número.")
    

    