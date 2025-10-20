from pathlib import Path

import pandas as pd


def extrair_dados_e_consolidar(pasta_json: str) -> pd.DataFrame:
    arquivos_json = Path(pasta_json).glob("*.json")
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df = pd.concat(df_list, ignore_index=True)
    return df


def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


def carregar_dados(df: pd.DataFrame, formato_saida: list[str], pasta_saia: str):
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        formato_saida (list[str]): _description_

    Raises:
        ValueError: _description_
    """
    formato_saida = [formato.lower() for formato in formato_saida]
    if "csv" not in formato_saida and "parquet" not in formato_saida:
        raise ValueError("Formato deve ser .csv, .parquet ou os dois")
    
    if "csv" in formato_saida:
        arquivo_saida = Path(pasta_saia) / "dados.csv"
        df.to_csv(arquivo_saida, sep=";", index=False)
        
    if "parquet" in formato_saida:
        arquivo_saida = Path(pasta_saia) / "dados.parquet"
        df.to_parquet(arquivo_saida, index=False)
        
        
def pipeline_calcular_kpi_de_vendas_consolidado(
    pasta_entrada: str, 
    pasta_saida: str, 
    formato_saida: list[str]
) -> None:
    df = extrair_dados_e_consolidar(pasta_entrada)
    df_calculado = calcular_kpi_de_total_de_vendas(df)
    formato_saida = ["CSV", "parquet"]
    carregar_dados(df_calculado, formato_saida, pasta_saida)
        

    
    