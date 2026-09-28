"""
Atividade Prática - Unpacking e Controle de Argumentos

Exercício 18 - Parâmetros somente posicionais com /


Crie uma função chamada registrar_placar com a seguinte assinatura:

def registrar_placar(time_a: str,time_b: str,/,gols_a: int,gols_b: int) -> str:...


A função deve:

    Possuir uma docstring.
    Utilizar os type hints indicados.
    Retornar uma string contendo o placar da partida.
    Exigir que time_a e time_b sejam passados somente por posição.
    Permitir que gols_a e gols_b sejam passados por posição ou pelo nome.


Faça uma chamada válida utilizando:

resultado = registrar_placar("Brasil","Argentina",gols_a=2,gols_b=1)
print(resultado)


Depois, tente:

registrar_placar(time_a="Brasil",time_b="Argentina",gols_a=2,gols_b=1)


Observe o erro e explique em um comentário qual é a função do / na assinatura.
"""

def registrar_placar(
    time_a: str,
    time_b: str,
    /,
    gols_a: int,
    gols_b: int
) -> str:
    """Função que recebe o duelo entre dois times e o número de gols de
    cada um, construíndo assim seu placar.
    
    Os valores representando os nomes de cada time devem ser transmitidos
    obrigatoriamente como valores posicionais.

    Args:
        time_a (str): Nome do time A.
        time_b (str): Nome do time B.
        gols_a (int): Número de gol(s) marcado(s) pelo time A.
        gols_b (int): Número de gols(s) marcado(s) pelo time B
 
    Returns:
        str: Informação final do duelo.
    """
    info_duelo = f"{time_a} {gols_a} x {gols_b} {time_b}"
    return info_duelo


resultado = registrar_placar("Brasil","Argentina",gols_a=2,gols_b=1)
print(resultado)

registrar_placar(time_a="Brasil",time_b="Argentina",gols_a=2,gols_b=1)
"""
O caracter / na assinatura da função informa que todos os parâmetros 
anteriores a ele devem ser obrigatoriamente posicionais.
"""

