"""
17. Crie uma função que receba um número como argumento e retorne True 
se o número for primo e False caso contrário.
"""
import math


def retorna_bool_avaliando_numero_primo(numero: int) -> bool:
    if numero in [0, 1]:
        return False
    
    for valor in range(2, int(math.sqrt(numero)) + 1):
        if numero % valor == 0:
            return False

    return True

numeros = range(21)
print("Verificando quais números são primos:")
for numero in numeros:
    print(f"{numero}: {retorna_bool_avaliando_numero_primo(numero)}")