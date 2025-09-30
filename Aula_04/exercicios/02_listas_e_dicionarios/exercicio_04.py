# 4. Escreva um programa que conta o número de ocorrências de cada 
# caractere em uma string usando um dicionário.
import string


texto = input("Texto: ").strip()

for pontuacao in string.punctuation:
    texto = texto.replace(pontuacao, "")

ocorrencias = {}
for caracter in texto.split():
    valor = ocorrencias.get(caracter.lower(), 0)
    ocorrencias[caracter.lower()] = valor + 1
print(ocorrencias)
