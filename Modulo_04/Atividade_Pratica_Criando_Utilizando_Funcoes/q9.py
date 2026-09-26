"""
Atividade Prática - Criando e Utilizando Funções

Exercício 9 - Analisando uma entrega

Você está desenvolvendo uma pequena parte de um sistema de entregas.

Crie uma função chamada calcular_tempo_estimado() que receba:

    distância da entrega em quilômetros;
    velocidade média do veículo em km/h.


A função deve calcular e retornar o tempo estimado da entrega em horas.

Use: tempo = distancia / velocidade

Depois, crie uma função chamada classificar_entrega() que receba o tempo calculado e retorne:

"Entrega rápida" se o tempo for menor ou igual a 1;
"Entrega normal" se o tempo for maior que 1 e menor ou igual a 3;
"Entrega demorada" se o tempo for maior que 3.

Por fim, crie uma terceira função chamada exibir_resumo_entrega() que receba:

    o tempo estimado;
    a classificação.


Ela deve exibir algo como:

    Tempo estimado: 2.5 horas
    Classificação: Entrega normal



Requisitos:

    As três funções devem possuir type hints.
    calcular_tempo_estimado() deve retornar float.
    classificar_entrega() deve retornar str.
    exibir_resumo_entrega() deve retornar None.
    Todas devem possuir docstrings.
    O resultado de calcular_tempo_estimado() deve ser utilizado por classificar_entrega().
    Os resultados das duas primeiras funções devem ser utilizados por exibir_resumo_entrega().
    Cada função deve possuir apenas uma responsabilidade.
"""

def calcular_tempo_estimado(distancia: float, velocidade: float) -> float:
    """ função que calcula tempo estimado da entrega em horas.

    Args:
        distancia (float): Distância da entrega, em quilômetros.
        velocidade (float): Velocidade média do veículo, em km/h.

    Returns:
        float: Tempo estimado da entrega, em horas.
    """
    tempo = distancia / velocidade
    return tempo


def classificar_entrega(tempo: float) -> str:
    """Função que faz uma classificação do tempo de entrega.

    Args:
        tempo (float): Tempo estimado da entrega, em horas.

    Returns:
        str: Classificação do tempo de entrega.
    """
    if tempo <= 1:
        return "Entrega rápida"
    if tempo <= 3:
        return "Entrega normal"
    return "Entrega demorada"


def exibir_resumo_entrega(tempo: float, classificacao: str):
    """Função que exibe o resumo da entrega.

    Args:
        tempo (float): Tempo estimado da entrega, em horas.
        classificacao (str): Classificação do tempo de entrega.
    """
    print(f"Tempo estimado: {tempo} horas")
    print(f"Classificação: {classificacao}")
    
    

temmpo = calcular_tempo_estimado(10.0, 4.0)
classificacao = classificar_entrega(temmpo)
exibir_resumo_entrega(temmpo, classificacao)