"""
Atividade Prática - Parâmetros e Argumentos em Funções

Exercício 7 - Alterando apenas um valor padrão

Crie uma função chamada configurar_camisa que receba:

nome
numero
tamanho="M"
cor="amarela"


Faça uma chamada informando uma cor diferente, mas mantendo o tamanho 
padrão.


Exemplo:

configurar_camisa("Marta", 10, cor="azul")


Observe como o argumento nomeado permite alterar cor sem precisar passar 
um novo valor para tamanho.
"""

def configurar_camisa(
    nome: str,
    numero: int,
    tamanho: str = "M",
    cor: str = "amarela"
):
    print(f"Nome: {nome} | Número: {numero} | Tamanho: {tamanho} | Cor: {cor}")
    
    
configurar_camisa("Marta", 10, cor="azul")