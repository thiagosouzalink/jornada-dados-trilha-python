# 10. Escreva um programa que calcule a área de um círculo, recebendo o 
# raio como entrada.
import math


raio = float(input("Digite o valor do raio do circulo: "))
area = math.pi * raio**2
print(f"Area do circulo com raio {raio}: {area:.2f}")