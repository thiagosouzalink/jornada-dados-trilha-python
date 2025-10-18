import csv


def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """Lê um arquivo csv e retorna uma lista de dicionários.

    Args:
        nome_arquivo_csv (str): caminho completo do arquivo csv

    Returns:
        list[dict]: Lista de dicionários como cada linha do arquivo.
    """
    try:
        with open(nome_arquivo_csv, "r", encoding="utf-8") as arquivo:
            leitor_dict = csv.DictReader(arquivo)
            return [linha_dict for linha_dict in leitor_dict]
    except FileNotFoundError:
        print("Arquivo não foi encontrado.")
    except Exception as e:
        print(f"Não foi possível ler o arquivo: {e}")
    
        
def processar_dados(lista_dados: list[dict]) -> dict:
    """Obtém um diconário tendo como chave as categorias.

    Args:
        lista_dados (list[dict]): Lista de dicionários

    Returns:
        dict: Dicionário processado.
    """
    try:
        dict_processado = {}
        for dict_linha in lista_dados:
            categoria: str = dict_linha.pop("Categoria")
            if categoria not in dict_processado:
                dict_processado[categoria] = []
            dict_processado[categoria].append(dict_linha)
        return dict_processado
    except Exception as e:
        print(f"Não foi possível processar o arquivo: {e}")


def calcular_vendas_por_categoria(dicionario_processado: dict) -> dict:
    """Calcula a soma das vendas por categoria.

    Args:
        dicionario_processado (dict): Dicionário categorizado.

    Returns:
        dict: Dicionário de vendas por categoria.
    """
    try:
        total_vendas_categoria = {}
        for chave in dicionario_processado:
            total_vendas = 0
            for valor in dicionario_processado[chave]:
                quantidade = int(valor["Quantidade"])
                venda = float(valor["Venda"])
                total_vendas += quantidade * venda
            total_vendas_categoria[chave] = total_vendas
        return total_vendas_categoria
    except Exception as e:
        print(f"Não foi possível processar o arquivo: {e}")