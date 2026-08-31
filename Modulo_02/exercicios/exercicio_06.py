numero = 10
jogador = "Rodrygo"

# msg = "O jogador" + jogador + "veste a camisa" +  numero
# TypeError: can only concatenate str (not "int") to str

msg = "O jogador " + jogador + " veste a camisa " +  str(numero)
print(msg)

# A conversão foi necessária porque o python não consegue concatenar str (jogador) com int (numero)