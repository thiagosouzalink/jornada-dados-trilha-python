nome_selecao: str = "Holanda"
quantidade_vitorias: int = 2
aproveitamento: float = 0.77
selecao_classicada: bool = True

print(f"Nome da seleção: {nome_selecao}", type(nome_selecao))
print(f"Quantidade de vitórias: {quantidade_vitorias}", type(quantidade_vitorias))
print(f"Aproveitamento: {nome_selecao}", type(aproveitamento))
print(f"Seleção classificada? {nome_selecao}", type(selecao_classicada))

quantidade_vitorias: int = "3"
print(f"Quantidade de vitórias: {quantidade_vitorias}", type(quantidade_vitorias))

# Type hint não fixa um tipo para a variável, apenas sugere qual tipo apropriado para ela.