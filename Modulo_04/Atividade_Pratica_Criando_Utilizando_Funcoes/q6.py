"""
Atividade Prática - Criando e Utilizando Funções

Exercício 6 - Convertendo temperatura

Crie uma função chamada converter_celsius_para_fahrenheit().

A função deve receber uma temperatura em Celsius e retornar o valor convertido para Fahrenheit.

Use a fórmula: fahrenheit = (celsius * 9 / 5) + 32

Depois, armazene o resultado em uma variável e imprima a temperatura convertida.

Requisitos:

    Receba a temperatura por parâmetro.
    Utilize type hint float.
    A função deve retornar um float.
    Utilize return.
    Adicione uma docstring explicando a função.


"""

def converter_celsius_para_fahrenheit(temperatura_celsius: float) -> float:
    """Função que converte uma temperatura em grau Celsius para Fahrenheit

    Args:
        temperatura_celsius (float): Temperatura em grau Celsius

    Returns:
        float: Temperatura em Fahrenheit
    """
    temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
    return temperatura_fahrenheit


celsius: float = 27
fahrenheit = converter_celsius_para_fahrenheit(celsius)
print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")

