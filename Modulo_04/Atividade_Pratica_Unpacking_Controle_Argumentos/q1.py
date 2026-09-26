"""
Atividade Prática - Unpacking e Controle de Argumentos

Exercício 14 - Unpacking com * e retorno


Considere a seguinte lista:

times = ["Brasil", "Argentina"]

Crie uma função chamada montar_confronto que receba dois parâmetros:

    time_a
    time_b


A função deve:

    Utilizar type hints nos parâmetros e no retorno.
    Possuir uma docstring explicando o que ela faz.
    Retornar uma string no formato Brasil x Argentina.

Depois, chame a função desempacotando a lista com *.

Você não deve acessar os valores manualmente com:

times[0]
times[1]


Exemplo esperado de uso:

confronto = montar_confronto(*times)
print(confronto)
"""

def montar_confronto(time_a: str, time_b: str) -> str:
    """Monta o confronto entre os times.

    Args:
        time_a (str): Primeiro time.
        time_b (str): Sefundo time.

    Returns:
        str: Confronto construído.
    """
    return f"{time_a} x {time_b}"


times = ["Brasil", "Argentina"]

confronto = montar_confronto(*times)
print(confronto)