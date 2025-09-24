"""
Exercício 25: Conversão de Tipo com Validação
Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
O programa deve converter a string de entrada em uma lista de números inteiros. 
Utilize try-except para tratar a conversão de cada número e validar que cada 
elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento 
não for um inteiro, imprima uma mensagem de erro. Se a conversão for 
bem-sucedida para todos os elementos, imprima a lista de inteiros.
"""
try:
    sequencia = input("Digite uma lista de valores separdos por virgula: ")
    lista_str = sequencia.split(",")
    lista_int = []
    for valor in lista_str:
        lista_int.append(int(valor))
    print(lista_int)
except ValueError:
    print("Os valores devem ser inteiros e separados por virgula")
