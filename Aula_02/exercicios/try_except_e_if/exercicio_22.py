"""
Exercício 22: Verificador de Palíndromo
Crie um programa que verifica se uma palavra ou frase é um palíndromo 
(lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
Utilize try-except para garantir que a entrada seja uma string. 
Dica: Utilize a função isinstance() para verificar o tipo da entrada.
"""
try:
    frase = input("Digite uma frase: ").strip()
    if not isinstance(frase, str):
        raise
    frase = ("".join(frase.split())
               .replace(".", "")
               .replace(",", "")
               .replace("!", "")
               .replace("?", "")
               .replace("-", "")
               .replace("_", ""))
    if frase.lower() == frase.lower()[::-1]:
        print("A frase e um Palindromo.")
    else:
        print("A frase nao e um Palindromo.")
except:
    print("Frase precisa ser uma string")

