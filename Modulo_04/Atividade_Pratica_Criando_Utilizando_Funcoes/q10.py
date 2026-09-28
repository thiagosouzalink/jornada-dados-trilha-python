"""
Atividade Prática - Criando e Utilizando Funções

Exercício 10 - Sistema de Aprovação de Empréstimo

Você está desenvolvendo uma parte de um sistema bancário responsável por 
analisar solicitações de empréstimo.

O programa deverá utilizar várias funções, e cada uma terá uma 
responsabilidade específica.

1. Calcular comprometimento da renda

Crie uma função chamada calcular_comprometimento_renda() que receba:

    renda mensal;
    valor da parcela do empréstimo.

Ela deve calcular qual percentual da renda mensal seria comprometido pela 
parcela.

Use:

percentual = (parcela / renda) * 100


A função deve retornar esse percentual.


2. Analisar o empréstimo

Crie uma segunda função chamada analisar_emprestimo() que receba:

    renda mensal;
    valor solicitado;
    percentual de comprometimento da renda.

A função deve retornar uma das seguintes classificações:

"Aprovado"
"Análise manual"
"Recusado"


Utilize estas regras:

    Se o comprometimento da renda for maior que 40%, retorne "Recusado".
    Se o comprometimento for menor ou igual a 40%, mas o valor solicitado 
    for maior que 5 vezes a renda mensal, retorne "Análise manual".
    Caso contrário, retorne "Aprovado".



3. Calcular o total do pagamento

Crie uma terceira função chamada calcular_total_pagamento() que receba:

    valor da parcela;
    quantidade de parcelas.

Ela deve retornar o valor total que será pago ao final do empréstimo.

Exemplo:

Parcela: R$ 850.00
Quantidade: 24

Total pago: R$ 20400.00

4. Exibir o resultado final

Por fim, crie uma função chamada exibir_resultado() que receba:

    valor solicitado;
    percentual de comprometimento;
    total que será pago;
    resultado da análise.

Ela deve apenas exibir um resumo como:

--- Análise do empréstimo ---

Valor solicitado: R$ 15000.00
Comprometimento da renda: 28.3%
Total a pagar: R$ 20400.00

Resultado: Aprovado


Essa função não deve retornar nenhuma informação.


Requisitos

    Todas as funções devem possuir type hints.
    Todas devem possuir docstrings.
    calcular_comprometimento_renda() deve retornar float.
    analisar_emprestimo() deve retornar str.
    calcular_total_pagamento() deve retornar float.
    exibir_resultado() deve retornar None.
    Os cálculos devem acontecer dentro das funções responsáveis por eles.
    Não repita cálculos fora das funções.
    Os valores retornados pelas funções devem ser armazenados em 
    variáveis e reutilizados nas próximas etapas.
    A função exibir_resultado() deve apenas receber os resultados já 
    calculados e exibi-los.
    Não utilize *args, **kwargs, parâmetros com valores padrão ou outros 
    recursos ainda não vistos nesta aula.


Fluxo esperado

dados do empréstimo
↓
calcular comprometimento da renda
↓
analisar empréstimo
↓
calcular total do pagamento
↓
exibir resultado final


O objetivo é organizar um problema maior em funções menores, fazendo com 
que o retorno de uma etapa seja utilizado pelas próximas.
"""

def calcular_comprometimento_renda(
    renda_mensal: float, 
    parcela_emprestimo: float
) -> float:
    """Função que calcula percentual da renda mensal comprometido pela 
    parcela.

    Args:
        renda_mensal (float): Valor da renda mensal.
        parcela_emprestimo (float): valor da parcela do empréstimo.

    Returns:
        float: Percentual da renda mensal comprometido pela parcela
    """
    percentual = (parcela_emprestimo / renda_mensal) * 100
    return percentual


def analisar_emprestimo(
    renda_mensal: float,
    valor_solicitado: float,
    percentual_comprometimento: float
) -> str:
    """Função que faz uma classificação de resultado de acordo com a 
    análise do empréstimo.

    Args:
        renda_mensal (float): Valor da renda mensal
        valor_solicitado (float): Valor solicitado de empréstimo.
        percentual_comprometimento (float): Percentual da renda mensal 
                                            comprometido pela parcela

    Returns:
        str: Resultado da análise do empréstimo.
    """
    if percentual_comprometimento > 40:
        return "Recusado"
    
    proporcao_valor = valor_solicitado > (5 * renda_mensal)
    if percentual_comprometimento <= 40 and proporcao_valor:
        return "Análise manual"
    
    return "Aprovado"


def calcular_total_pagamento(
    parcela_emprestimo: float, 
    quantidade_parcelas: int
) -> float:
    """Função que calcula o valor total pago do empréstimo.

    Args:
        parcela_emprestimo (float): Valor da parcela do emprétimo.
        quantidade_parcelas (int): Quantidade de parcelas do empréstimo.

    Returns:
        float: Valor total pago do empréstimo.
    """
    total = parcela_emprestimo * quantidade_parcelas
    return total


def exibir_resultado(
    valor_solicitado: float,
    percentual_comprometimento: float,
    total_pago_emprestimo: float,
    resultado_analise: str
):
    """Função que exibi o resumo do empréstimo bancário.

    Args:
        valor_solicitado (float): Valor solicitado de empréstimo.
        percentual_comprometimento (float): Percentual da renda mensal 
                                            comprometido pela parcela
        total_pago_emprestimo (float): Valor total pago do empréstimo.
        resultado_analise (str): Resultado da análise do empréstimo.
    """
    mensagem = "--- Análise do empréstimo ---\n\n"\
               f"Valor solicitado: R$ {valor_solicitado:.2f}\n"\
               f"Comprometimento da renda: {percentual_comprometimento:.1f}%\n"\
               f"Total a pagar: R$ {total_pago_emprestimo:.2f}\n\n"\
               f"Resultado: {resultado_analise}\n"
               
    print(mensagem)

 
# extra: função para calcular o valor de cada parcela do empréstimo
def calcular_valor_parcela_emprestimo(
    valor_solicitado: float, 
    quantidade_parcelas: int,
    taxa_juros: float
) -> float:
    """Função que calcula o valor de cada parcela do empréstimo, utilizando
    o sistema price.

    Args:
        valor_solicitado (float): Valor solicitado de empréstimo.
        quantidade_parcelas (int): Quantidade de parcelas do empréstimo.

    Returns:
        float: Valor de cada parcela do empréstimo.
    """
    numerador = taxa_juros * (1 + taxa_juros) ** quantidade_parcelas
    denominador = (1 + taxa_juros) ** quantidade_parcelas - 1
    valor_parcela = valor_solicitado * numerador/denominador
    return valor_parcela



renda_mensal: float = 5000.00
valor_solictado_emprestimo = 7500.00
quantidade_parcelas_emprestimo: int = 5
taxa_juros: float = 0.02
parcela_emprestimo = calcular_valor_parcela_emprestimo(valor_solictado_emprestimo, 
                                                       quantidade_parcelas_emprestimo,
                                                       taxa_juros)
percentual_comprometimento = calcular_comprometimento_renda(renda_mensal, 
                                                            parcela_emprestimo)
analise_emprestimo = analisar_emprestimo(renda_mensal, 
                                         valor_solictado_emprestimo, 
                                         percentual_comprometimento)
total_pagamento_emprestimo = calcular_total_pagamento(parcela_emprestimo, 
                                                      quantidade_parcelas_emprestimo)
exibir_resultado(valor_solictado_emprestimo, 
                 percentual_comprometimento, 
                 total_pagamento_emprestimo, 
                 analise_emprestimo)