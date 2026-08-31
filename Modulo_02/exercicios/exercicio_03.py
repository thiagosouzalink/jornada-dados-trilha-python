gols = "2"
novo_gol = gols + 1

print(novo_gol)

# 1. Qual erro ocorreu? 
# TypeError

# 2. Quais são os tipos dos valores envolvidos?
# str e int

# 3. Por que esses valores não podem ser utilizados dessa forma?
# Python tem tipagem forte, ele não pode somar str e int, pois ele não converte automaticamente para o mesmo tipo.

# 4. Corrija o programa para que o resultado exibido seja 3.
gols = "2"
novo_gol = int(gols) + 1

print(novo_gol)