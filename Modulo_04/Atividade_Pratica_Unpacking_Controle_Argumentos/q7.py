"""
Atividade Prática – Unpacking e Controle de Argumentos

Exercício 20 – Desafio final: trabalhando com todos os tipos de argumentos


Crie uma função chamada registrar_jogo com a seguinte assinatura:

def registrar_jogo(
mandante: str,visitante: str,
/,
competicao: str,
*eventos: str,
estadio: str,
encerrado: bool = True,
**informacoes
) -> dict:


A função deve possuir uma docstring completa explicando:

    O objetivo da função.
    O que cada parâmetro representa.
    O que a função retorna.


A função também deve seguir estas regras:

    mandante e visitante devem ser informados somente por posição.
    competicao pode ser passada por posição ou pelo nome.
    *eventos deve receber uma quantidade variável de eventos da partida.
    estadio deve obrigatoriamente ser informado pelo nome.
    encerrado deve possuir True como valor padrão.
    **informacoes deve receber informações adicionais da partida.


Dentro da função, crie e retorne um dicionário contendo:

    Mandante.
    Visitante.
    Competição.
    Eventos.
    Estádio.
    Situação da partida.
    Informações adicionais.

Teste a função com:

partida = registrar_jogo(
"Brasil",
"Argentina",
"Copa do Mundo",
"Gol do Brasil",
"Cartão amarelo",
"Substituição",
estadio="Maracanã",
publico=70000,
transmissao="TV"
)
print(partida)


Depois, considere os seguintes dados:

times = ["França", "Espanha"]
dados = {"estadio": "Stade de France","publico": 65000,"transmissao": "Streaming"}


Faça uma segunda chamada utilizando:

    *times para desempacotar os dois primeiros argumentos.
    Uma competição informada normalmente.
    Dois ou mais eventos posicionais.
    **dados para desempacotar as informações nomeadas.


Ao final, escreva comentários identificando o papel de cada elemento da 
assinatura:

/
*eventos
estadio
encerrado=True
**informacoes


Explique também a diferença entre:

*eventos

na definição da função e:

*times

na chamada, assim como a diferença entre:

**informacoes

na definição e:

**dados

na chamada.
"""

def registrar_jogo(
mandante: str,
visitante: str,
/,
competicao: str,
*eventos: str,
estadio: str,
encerrado: bool = True,
**informacoes
) -> dict:
    """Registra informações de uma determinada partida.
    
     Mandante e visitante devem ser informados somente por posição.

    Args:
        mandante (str): Equipe mandante;
        visitante (str): Equipe visitante.
        competicao (str): Nome da competição.
        *eventos (str): Quantidade variável de eventos da partida.
        estadio (str): Nome do estádio onde a partida foi realizada.
        encerrado (bool, optional): Informa se a partida foi encerrada 
                                    normalmente. Defaults to True.
        **informacoes: Demais informações adicionais sobre a partida.

    Returns:
        dict: Informações sobre a partida
    """
    info = {
        "Mandante": mandante,
        "Visitante": visitante,
        "Competição": competicao,
        "Eventos": eventos,
        "Estádio": estadio,
        "Encerrado": encerrado,
        "Informações": informacoes
    }
    return info


partida = registrar_jogo(
"Brasil",
"Argentina",
"Copa do Mundo",
"Gol do Brasil",
"Cartão amarelo",
"Substituição",
estadio="Maracanã",
publico=70000,
transmissao="TV"
)
print(partida)


times = ["França", "Espanha"]
dados = {"estadio": "Stade de France","publico": 65000,"transmissao": "Streaming"}
partida = registrar_jogo(
    *times,
    "Eurocopa",
    "Gol da França",
    "Gol da Espanha",
    **dados
)
print(partida)

"""
*eventos: Recebe vários argumentos posicionais como eventos

*times: Desempacotamento dos valores da lista time como argumentos

**informacoes: Inúmeros arqgumentos nomeados passados para a função

** dados: desempacotamento do dicionário como arqgumentos nomeados para a
função
"""