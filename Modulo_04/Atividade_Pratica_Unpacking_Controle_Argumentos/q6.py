"""
Atividade Prática - Unpacking e Controle de Argumentos

Exercício 19 - Parâmetros somente nomeados com *


Crie uma função chamada criar_jogador com a seguinte assinatura:

def criar_jogador(nome: str,*,posicao: str,numero: int,titular: bool = False) -> str:...


A função deve:

    Possuir uma docstring.
    Utilizar type hints.
    Utilizar um valor padrão para titular.
    Retornar uma string com os dados do jogador.

O parâmetro nome pode ser informado por posição.

Os parâmetros após * devem ser informados pelo nome.


Faça uma chamada válida:

jogador = criar_jogador("Marta",posicao="Atacante",numero=10)
print(jogador)


Depois, faça outra chamada informando:

titular=True


Por fim, tente executar:

criar_jogador("Marta","Atacante",10)


Observe o erro e explique em um comentário por que posicao e numero não 
podem ser passados por posição.
"""

def criar_jogador(
    nome: str,
    *,
    posicao: str,
    numero: int,
    titular: bool = False
) -> str:
    """Exibe informações de um(a) determinado(a) jogador(a).
    
    Os valores de posicao, numero e titular devem ser transmitidos
    obrigatoriamente como argumentos nomeados.

    Args:
        nome (str): Nome do jogador(a).
        posicao (str): Posição do jogador(a).
        numero (int): Número da camisa do jogador(a).
        titular (bool, optional): Informa sobre sua titularidade 
                                  Defaults to False.

    Returns:
        str: Informações do jogador(a).
    """
    info = f"Nome: {nome} | Posição: {posicao} | Número: {numero} | Titular: {titular}"
    return info


jogador = criar_jogador("Marta",posicao="Atacante",numero=10)
print(jogador)

jogador = criar_jogador("Marta",posicao="Atacante",numero=10, titular=True)
print(jogador)

criar_jogador("Marta","Atacante",10)
"""
O caracter * na assinatura da função criar_jogador especifica que todos
os valores após ele devem ser obrigatoriamente argumentos nomeados.
"""